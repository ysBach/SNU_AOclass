from pathlib import Path

import ysfitsutilpy as yfu
# https://github.com/ysBach/ysfitsutilpy
# You may also need astropy, numpy, and scipy. If you have FITSIO installed
# (https://github.com/esheldon/fitsio), the FITS io speed will be boosted by ~ 10-20x.
import ysphotutilpy as ypu
# https://github.com/ysBach/ysphotutilpy
# You may also need astropy, numpy, and scipy. Also you need SEP (https://github.com/kbarbary/sep) for
# background estimation in the last part (color image making)
from astropy.io import fits
from astropy.visualization import make_lupton_rgb

import astroalign as aa


def iterator(it):
    try:
        from tqdm import tqdm
        toiter = tqdm(it)
    except ImportError:
        toiter = it
    return toiter


comb_kw = dict(combine="med", memlimit=8.e+9, overwrite=True)

# ********************************************************************************************************** #
# *                                              MAKE SUMMARY                                              * #
# ********************************************************************************************************** #
summary = yfu.make_summary("*.fit", output="summary.csv")

# ********************************************************************************************************** #
# *                                            MAKE MASTER BIAS                                            * #
# ********************************************************************************************************** #
_ = yfu.imcombine("calibration*bias.fit", output="mbias.fits", **comb_kw)

# ********************************************************************************************************** #
# *                                            MAKE MASTER DARK                                            * #
# ********************************************************************************************************** #
_ = yfu.group_combine(summary, type_key=["IMAGETYP"], type_val=["Dark Frame"],
                      group_key=["EXPTIME"], fmt="mdark_{:03.0f}s", **comb_kw)

_mdarkpaths = list(Path(".").glob("mdark*.fits"))
for _mdarkpath in _mdarkpaths:
    yfu.bdf_process(_mdarkpath, mbiaspath="mbias.fits", output=f"b_{_mdarkpath.name}")

# ********************************************************************************************************** #
# *                                            MAKE MASTER FLAT                                            * #
# ********************************************************************************************************** #
_flatpaths = list(Path(".").glob("skyflat*.fit"))
# -- First, save after bias and dark subtraciton
for _flatpath in _flatpaths:
    exptime = yfu.load_ccd(_flatpath).header["EXPTIME"]
    mdarkpath = Path(f"b_mdark_{exptime:03.0f}s.fits")
    # Bias and dark subtract
    output = Path(f"bd_{_flatpath.stem}.fits")
    if not output.exists():
        _ = yfu.bdf_process(_flatpath, mbiaspath="mbias.fits", mdarkpath=mdarkpath, output=output)

# -- Second, combine after normalization
#   If no normalization is done, the output will be severely affected by the brightest flat frame since
#   they are "sky" flats during the sunset.
_ = yfu.group_combine(summary, type_key=["IMAGETYP"], type_val=["Flat Field"],
                      group_key=["FILTER"], fmt="mflat_{:s}", **comb_kw, scale="avg_sc", scale_to_0th=False)
# scale_to_0th=False : Scale (normalize) each frame by its own average. If it is set to True (default
# of IRAF, for instance), i-th image is normalized by avg{0-th image}/avg{i-th image} so that all the
# images have mean identical to the 0-th image.

# ********************************************************************************************************** #
# *                                            REDUCE EACH FRAME                                           * #
# ********************************************************************************************************** #
_fitspaths = list(Path(".").glob("M1*.fit"))
for _fitspath in _fitspaths:
    hdr = yfu.load_ccd(_fitspath).header
    exptime = hdr["EXPTIME"]
    filtername = hdr["FILTER"]
    mdarkpath = Path(f"b_mdark_{exptime:03.0f}s.fits")
    mflatpath = Path(f"mflat_{filtername}.fits")
    # Bias and dark subtract
    output = Path(f"bdf_{_fitspath.stem}.fits")
    if not output.exists():
        _ = yfu.bdf_process(_fitspath, mbiaspath="mbias.fits", mdarkpath=mdarkpath, mflatpath=mflatpath,
                            output=output)

# ********************************************************************************************************** #
# *                                   COMBINE EACH FRAME AFTER "ALIGNING"                                  * #
# ********************************************************************************************************** #
filternames = ["Oiii", "Ha", "Sii"]
# Maybe one can boost the speed by ~ 2x by finding xy position of sources in the ref image and use it later.
#   See https://quatrope.github.io/astroalign/ (cell In [5]).
ref = yfu.load_ccd(Path("bdf_M1-0001Ha.fits")).data.byteswap().newbyteorder()

for filt in filternames:
    print(filt)
    fpaths = list(Path(".").glob(f"bdf_M1-*{filt}.fits"))
    fpaths.sort()
    # frames[fpath] = (ccd.data).byteswap().newbyteorder()

    # `a` stands for "aligned"
    yfu.load_ccd(fpaths[0]).write(f"a{fpaths[0].name}", overwrite=True)

    # .byteswap().newbyteorder() is needed. If not, the following error occurs:
    #   ValueError: Big-endian buffer not supported on little-endian compiler
    for fpath in iterator(fpaths[1:]):
        frame = yfu.load_ccd(fpath).data.byteswap().newbyteorder()
        img_aligned, footprint = aa.register(frame, ref, detection_sigma=5, min_area=5, max_control_points=50)
        reg = fits.PrimaryHDU(data=img_aligned)
        reg.header["FILTER"] = filt
        reg.writeto(f"a{fpath.name}", overwrite=True)

yfu.group_combine("abdf_M1*", group_key=["FILTER"], fmt="combined_M1_{:s}", **comb_kw)


def sub_bkg(fpath):
    ccd = yfu.load_ccd(fpath)
    bkg = ypu.sep_back(ccd, box_size=256, filter_size=7)
    return ccd.data - bkg.back(), bkg.back()


o, ob = sub_bkg("combined_M1_Oiii.fits")
h, hb = sub_bkg("combined_M1_Ha.fits")
s, sb = sub_bkg("combined_M1_Sii.fits")

rgb_default = make_lupton_rgb(o, h, s, filename="M1_rgb_default.jpeg")
plt.imshow(rgb_default, origin='lower')
plt.imshow(make_lupton_rgb(ob, hb, sb), origin='lower')

rgb = make_lupton_rgb(o, h, s, Q=10, stretch=0.5, filename="M1_rgb.jpeg")
plt.imshow(rgb, origin='lower')
