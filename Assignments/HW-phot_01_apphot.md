This is a continuation from [master-frame making homework](./HW-preproc_01_mkmaster.md) and [BDFC preprocessing homework](./HW-preproc_02_BDFC.md).

## Goals

**I am assuming you are familiar with python ``pathlib`` and ``astropy.io.fits`` by now.**

* Using **ysfitsutilpy** and **ysphotutilpy**:
  * Find asteroid in the FITS file
  * Do (circular) aperture photometry to stars and object
  * Find the standardized magnitude of the object
  * Plot the light curve of the asteroid.



## Instructions

**You need at least ~ 1 GB of free space on your computer.**

1. Install ``regions``: 

```
$ conda install -c astropy regions
```

Run the following before you run any code below.

```python
%config InlineBackend.figure_format = 'retina'

from pathlib import Path
import numpy as np
from scipy.optimize import curve_fit

from astropy.nddata import CCDData
from astropy.io import fits
from astropy.time import Time
from astropy.table import hstack, vstack
from astropy import units as u
from astropy.stats import sigma_clip

import ysfitsutilpy as yfu
import ysphotutilpy as ypu
import ysvisutilpy as yvu

from matplotlib import pyplot as plt
from matplotlib import rcParams
from matplotlib import gridspec


def linf(x, a, b):
    return a*x + b

def mkreg(stars, ephem, rap_arcsec, output, 
          c_star='green', c_target='red', width=2, font="helvetica 10 normal roman"):
    globstr = 'global color=green dashlist=8 3 width=2 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\n'
    apstr = 'circle({},{},{}") # width={:.0f}, color={:s}, text={{{:s}}}\n'
    anstr = 'annulus({},{},{}",{}") # width={:.0f}, color={:s}, text={{{:s}}}\n'
    with open(output, 'w+') as ff:
        ff.write("# Region file format: DS9 version 4.1\n")
        ff.write(globstr.format(c_star))
        ff.write('fk5\n')
        
        ff.write(apstr.format(
            ephem["RA"],
            ephem["DEC"],
            rap_arcsec,
            width,
            c_target,
            "Target"
        ))
        for i, row in enumerate(stars):
            ff.write(apstr.format(
                row["RAJ2000"], 
                row["DEJ2000"], 
                rap_arcsec, 
                width, 
                c_star,
                f"#{i + 1:02.0f} (R = {row['Rmag']:.2f})"
            ))
            
            
def plotting(ax_l, ax_r, ax_c, phot_stars, phot_targ, m_min=13.5, m_max=16.1):
    errbfmt = dict(marker='x', ls='', capsize=5, elinewidth=0.5)

    for ax in [ax_l, ax_r, ax_c]:
        ax.cla()
    try:
        ax_c2.cla()
    except UnboundLocalError:
        pass

    m_true = phot_stars["Rmag"]
    m_inst = phot_stars["mag"]
    e_m_true = phot_stars["e_Rmag"]
    e_m_inst = phot_stars["merr"]
    color = phot_stars["grcolor"]
    e_color = phot_stars["e_grcolor"]
    Z = m_true - m_inst
    e_Z = np.sqrt(e_m_true**2 + e_m_inst**2)
    s_Z = np.std(Z, ddof=1)  # standard deviation
    m_Z = np.mean(Z)         # Simple mean
    Z_fit = np.average(Z, weights=(1/e_Z**2))
    e_Z_fit = np.sqrt(1 / np.sum(1/e_Z**2))

    mm = np.linspace(m_min, m_max, 2)  # grid
    cc = np.linspace(color.min(), color.max(), 2)  # grid
    p_ll, _ = curve_fit(linf, m_true, m_inst, sigma=e_m_inst, absolute_sigma=True)
    p_cz, _ = curve_fit(linf, color, Z, sigma=e_Z, absolute_sigma=True)

    ax_l.errorbar(m_true, m_inst, xerr=e_m_true, yerr=e_m_inst, **errbfmt)
    ax_l.plot(mm, linf(mm, *p_ll), 'k-', label=f"y={p_ll[0]:.4f}x + {-p_ll[1]:.3f}")
    ax_l.plot(mm, mm - Z_fit, 'r-', label=f"y=x + {Z_fit:.3f} (see right)")
    ax_l.axhline(phot_targ['mag'], color='g', label="target")
    ax_l.set(
        ylabel="R$_\mathrm{inst}$", 
        title="Linearity Curve"
    )
    ax_l.legend(loc=2, framealpha=0, fontsize=10)
    for j, (x_i, y_i) in enumerate(zip(m_true, m_inst)):
        ax_l.text(x=x_i, y=y_i, s=j+1)

    ax_r.errorbar(m_true, Z, yerr=e_Z, **errbfmt)
    ax_r.axhline(Z_fit, color='r', ls='-', lw=1)
    ax_r.axhline(Z_fit + e_Z_fit, color='r', ls='--', lw=1, label=None) 
    ax_r.axhline(Z_fit - e_Z_fit, color='r', ls='--', lw=1, label=None)
    ax_r.axhline(m_Z + s_Z, color='b', ls=':', lw=1, label=None) 
    ax_r.axhline(m_Z - s_Z, color='b', ls=':', lw=1, label=None)
    ax_r.set(xlabel="R from PS1 g/r (Tonry+ 2012)",
             ylabel="R - R$_\mathrm{inst}$",
             xlim=(m_min, m_max),
             ylim=(Z_fit - 1, Z_fit + 1)
            )
    for j, (x_i, y_i) in enumerate(zip(m_true, Z)):
        ax_r.text(x=x_i, y=y_i, s=j+1)

    ax_c.errorbar(color, Z, yerr=e_Z, xerr=e_color, **errbfmt)
    ax_c.axhline(Z_fit, color='r', ls='-', lw=1, label=f"wieghted avg = {Z_fit:.3f}")
    ax_c.axhline(Z_fit + e_Z_fit, color='r', ls='--', lw=1, label=f"err = {e_Z_fit:.3f}") 
    ax_c.axhline(Z_fit - e_Z_fit, color='r', ls='--', lw=1, label=None)
    ax_c.axhline(m_Z, color='b', ls='-', lw=1, label=f"simple avg = {m_Z:.3f}")
    ax_c.axhline(m_Z + s_Z, color='b', ls=':', lw=1, label=f"std = {s_Z:.3f}") 
    ax_c.axhline(m_Z - s_Z, color='b', ls=':', lw=1, label=None)
    ax_c.plot(cc, linf(cc, *p_cz), 'k-')
    ax_c.legend(loc=2, framealpha=0, ncol=2)
    ax_c.set(xlabel="g - r from PS1",
             title="Z = R - R$_\mathrm{inst}$ = (k + k''X)C + (zero + k'X)")

    ax_c2 = ax_c.twinx()
    ax_c2.plot(np.nan, np.nan, 'k-',
               label=f"y={p_cz[0]:.3f}x + {p_cz[1]:.3f}")
    ax_c2.legend(loc=4)
    ax_c2.axis('off')

    for j, (x_i, y_i) in enumerate(zip(color, Z)):
        ax_c.text(x=x_i, y=y_i, s=j+1)

    yvu.linticker(
        [ax_l, ax_r, ax_c],
        xmajlockws=[0.5, 0.5, 0.2],
        xminlockws=[0.1, 0.1, 0.1],
        ymajlockws=[0.5, 0.5, 0.1],
        yminlockws=[0.1, 0.1, 0.05]
    )

    plt.tight_layout()
    
    result = dict(
        linSlope=p_ll[0],
        linInter=p_ll[1], 
        colorSlope=p_cz[0],
        colorInter=p_cz[1],
        Zpt=Z_fit,
        e_Zpt=e_Z_fit,
        Zavg=m_Z,
        Zstd=s_Z
    )
    return result
        
USEFUL_KEYS = ["DATE-OBS", "FILTER", "OBJECT", "EXPTIME", "IMAGETYP",
               "AIRMASS", "XBINNING", "YBINNING", "CCD-TEMP", "SET-TEMP",
               "OBJCTRA", "OBJCTDEC", "OBJCTALT"]

TOPPATH = Path("original")  # the directory you saved the FITS files
REDDIR = TOPPATH/"reduced"
REDDIR.mkdir(parents=True, exist_ok=True)
allfits = list(REDDIR.glob("*.fits"))

gain_original = 1.36
rdnoise_original = 9.0 
bin_area = 4*4
gain = gain_original*bin_area
rdnoise = rdnoise_original * np.sqrt(bin_area)
```



## Problems

2 points each, unless specified.



### 1. Query

1. Make a summary table of all the raw FITS files, sort by ``DATE-OBS`` k.
   * Hint: ``summary = yfu.make_summary(allfits, keywords=USEFUL_KEYS, sort_by='DATE-OBS')``
2. Find the middle time of the exposure.
   * Hint: ``midtimes = Time(summary["DATE-OBS"], format='isot') + summary["EXPTIME"]*u.s/2``

3. Query the ephemerides of 2005 UD at ``midtimes``, set the output (such as astropy Table or pandas DataFrame) to ``eph``.

   ```python
   # One possible way is to use ysphotutilpy
   snuo = dict(lon=126.954, lat=37.455, elevation=150)
   q = ypu.HorizonsDiscreteEpochsQuery(
       targetname="155140",  # permanent designation of 2005 UD
       location=snuo,
       epochs=midtimes.jd
   )
   q.query()
   eph = q.query_table
   # display the table by eph
   ```

4. Make a summary table of all the reduced FITS files, and combine it with ``eph``. Then save as ``"20191012_2005UD.csv"``.

   ```python
   summary = hstack([summary, eph])
   summary.to_pandas().to_csv(TOPPATH/"20191012_2005UD.csv", index=False)
   ```

   * NOTE: ~~``summary.to_pandas()`` is required because if you just save with astropy table, there's a [known bug for Windows users](https://github.com/astropy/astropy/issues/5126)~~ It seems fixed but I haven't tested.

5. Open any FITS file using DS9. Go to ``Analysis`` → ``Catalog`` → ``Optical`` → ``URAT1``. Click ``rmag`` in the dropdown menu of ``Sort``. In the table, click on the rows which have available ``rmag`` values. Stars with ``rmag < 10`` is too bright, and those with ``rmag > 16`` is too faint. (I confirmed | I didn't confirm)

6. Open any FITS file using DS9 or ginga. Find the rough FWHM of stars. I found ~ 3 pixel is a reasonable FWHM value since the stars are elongated. (I confirmed | I didn't confirm)

7. Now, test to the 5-th element of the ``summary``. Query stars:

   ```python
   fwhm = 3                  # Check this from, e.g., ginga, a priori.
   fwhm_arcsec = fwhm * 1.2  # 1.2 arcsec/pixel
   
   row = summary[5]
   fpath = Path(row['file'])
   print(fpath)
   ccd = yfu.load_ccd(fpath)
   err = yfu.make_errmap(ccd)
   hdr = ccd.header
   
   # Query sidereal objects (PS1)
   cent_coord = yfu.center_radec(header=hdr, center_of_image=True)
   rad = yfu.fov_radius(header=hdr, unit=u.deg)
   
   # Initialize PanSTARRS1 class
   ps1 = ypu.PanSTARRS1(
       ra=cent_coord.ra.value, 
       dec=cent_coord.dec.value, 
       radius=rad,
       column_filters={'rmag':'10.0..16.0', 'e_rmag':'<0.10'}
   )
   isnear = ypu.organize_ps1_and_isnear(
       ps1=ps1,
       header=hdr,
       bezel=50,
       group_crit_separation=6*fwhm,
       select_filter_kw=dict(filter_names=['g', 'r'], n_mins=5),
       drop_by_Kron=True,
       calc_JC=True  # This uses g-r color, so both g and r must not be removed.
   )
   stars = ps1.queried
   
   print(isnear)
   # type ``stars`` to display the table
   ```

8. Quickly confirm the positions of the stars in python:

   ```python
   targ_xy = ypu.get_xy(hdr, row["RA"], row["DEC"])
   ap_targ, _ = ypu.circ_ap_an(targ_xy, fwhm=fwhm, f_ap=10)
   ap_stars, _ = ypu.circ_ap_an([stars["x"], stars["y"]], fwhm=fwhm, f_ap=10)
   
   fig, axs = plt.subplots(1, 1, figsize=(8, 5), 
                           sharex=False, sharey=False, gridspec_kw=None)
   yvu.norm_imshow(axs, ccd, zscale=True)
   ap_stars.plot(axs)
   ap_targ.plot(axs, color='r')
   plt.tight_layout()
   fig.align_ylabels(axs)
   fig.align_xlabels(axs)
   plt.show()
   ```

9. Make a ``.reg`` file. Open DS9, open the FITS file. Go to ``Regions`` →``Load Regions...`` → Find the file you saved from the code below. Then check if the positions of the stars and target are as expected. Attach a screenshot.

   ```python
   regpath = fpath.parent/f"{fpath.stem}.reg"
   mkreg(stars, row, 2.*fwhm_arcsec, regpath)
   ```

* In real research, you need these (.reg file) kind of log files all the time, because for some reason your code may have a problem (bug, typo, etc), and the results do not look realistic. Then you have to open the raw file, reduced file, plot this region file, look into the ephemerides file, etc, to find out where you made a mistake.

### 2. Aperture photometry

Rigorously speaking, the centroid position of the star should be re-calculated as we did in the lecture notes (e.g., using ``DAOStarFinder`` and "match" the stars). Here, I will skip that part. Also I will assume all the PSFs of the stars and target are circular, which is visually not very satisfactory. If you are interested in, please refer to the [online appendix of Ishiguro, Bach, Geem et al. 2020](https://nbviewer.jupyter.org/github/ysBach/IshiguroM_etal_155140_2005UD/blob/master/photometry/Photometer.ipynb). As of 2020-05-31, you may download the "report" files [here](https://www.dropbox.com/sh/4ke0pwqyngcdg6e/AAChOyyw3cQNfHfQOZfi1oBAa?dl=0) to see how the outcome looks like.



1. Do the aperture photometry to stars and target:

   ```python
   ap_stars, an_stars = ypu.circ_ap_an([stars["x"], stars["y"]], fwhm=fwhm, f_ap=2, f_in=4, f_out=6)
   ap_targ, an_targ = ypu.circ_ap_an(targ_xy, fwhm=fwhm, f_ap=2, f_in=4, f_out=6)
   
   phot_targ = ypu.apphot_annulus(ccd=ccd, aperture=ap_targ, annulus=an_targ, error=err)
   
   phot_stars = ypu.apphot_annulus(ccd=ccd, aperture=ap_stars, annulus=an_stars, error=err)
   phot_stars = hstack([phot_stars, stars]).to_pandas()
   phot_stars.to_csv(fpath.parent/f"{fpath.stem}_stars.csv", index=False)
   # use phot_stars and phot_targ to display the tables. 
   ```

2. What is the meaning of ``f_in=4``? (you may look at ``ypu.circ_ap_an?``)

3. Plot the linearity, residual, and color-dependency plots:

   ```python
   fig = plt.figure(figsize=(12, 6))
   gs = gridspec.GridSpec(3, 3)
   # NOTE: Z = R - R_inst = zp + 1st ext
   ax_l = fig.add_subplot(gs[:2, 0])                # Linearity plot
   ax_r = fig.add_subplot(gs[2, 0], sharex=ax_l)    # residual plot
   ax_c = fig.add_subplot(gs[:, 1:])                # C(g-r) VS Z plot
   
   plotting(ax_l, ax_r, ax_c, phot_stars, phot_targ)
   ```

4. Let's do the whole process to all the FITS files:

   ```python
   fwhm = 3                  # Check this from, e.g., ginga, a priori.
   near = []
   phot_targs = []
   apkw = dict(fwhm=fwhm, f_ap=2, f_in=4, f_out=6)
   
   fig = plt.figure(figsize=(12, 6))
   gs = gridspec.GridSpec(3, 3)
   # NOTE: Z = R - R_inst = zp + 1st ext
   ax_l = fig.add_subplot(gs[:2, 0])                # Linearity plot
   ax_r = fig.add_subplot(gs[2, 0], sharex=ax_l)    # residual plot
   ax_c = fig.add_subplot(gs[:, 1:])                # C(g-r) VS Z plot
   
   for row in summary:
       ### Set paths for loading and saving
       fpath = Path(row['file'])
       regpath = fpath.parent/f"{fpath.stem}.reg"
       starspath = fpath.parent/f"{fpath.stem}_stars.csv"
       figpath = fpath.parent/f"{fpath.stem}.pdf"
   
       print(fpath, f'(RA, DEC) = ({row["RA"]:.5f}, {row["DEC"]:+.5f}) [deg]')
       
       ### load CCD and calcualte errors
       ccd = yfu.load_ccd(fpath)
       hdr = ccd.header
       err = yfu.make_errmap(ccd, gain_epadu=gain, rdnoise_electron=rdnoise)
   
       
       ### Query sidereal objects (PS1)
   
       # Position of the telescope FOV center (RA/DEC of the pixel at the center)
       try:
           cent_coord = yfu.center_radec(header=hdr, center_of_image=True)
       except ValueError: # some files do not have correct WCS... my bad (ysBach 2020-05-31 21:31:25)
           continue
       # FOV radius
       rad = yfu.fov_radius(header=hdr, unit=u.deg)
   
       # Initialize PanSTARRS1 class
       ps1 = ypu.PanSTARRS1(
           ra=cent_coord.ra.value, 
           dec=cent_coord.dec.value, 
           radius=rad,
           column_filters={'rmag':'10.0..16.0', 'e_rmag':'<0.10'}
       )
       
       # Organize PanSTARRS1 query result.
       isnear = ypu.organize_ps1_and_isnear(
           ps1=ps1,
           header=hdr,
           bezel=50,
           group_crit_separation=6*fwhm,
           select_filter_kw=dict(filter_names=['g', 'r'], n_mins=5),
           drop_by_Kron=True,
           calc_JC=True  # This uses g-r color, so both g and r must not be removed.
       )
       stars = ps1.queried
   
       # Check if any object near to our target
       if isnear:
           near.append(fpath)
   
       ### Make DS9 region file
       mkreg(stars, row, 2.*fwhm_arcsec, regpath)
       
       ### Do photometry
       
       # Make apertures
       targ_xy = ypu.get_xy(hdr, row["RA"], row["DEC"])
       ap_stars, an_stars = ypu.circ_ap_an([stars["x"], stars["y"]], **apkw)
       ap_targ, an_targ = ypu.circ_ap_an(targ_xy, **apkw)
   
       # photometry for target
       phot_targ = ypu.apphot_annulus(
           ccd=ccd, 
           aperture=ap_targ, 
           annulus=an_targ, 
           error=err)
   
       # photometry for stars
       phot_stars = ypu.apphot_annulus(ccd=ccd, aperture=ap_stars, annulus=an_stars, error=err)
       phot_stars = hstack([phot_stars, stars]).to_pandas()
       phot_stars.to_csv(starspath, index=False)
   
       ### Find Z value
       # Plot curves & get zero-point fitting result
       res = plotting(ax_l, ax_r, ax_c, phot_stars, phot_targ)
       phot_targ["file"] = row["file"]
       phot_targ["nstar"] = len(phot_stars)
       for k, v in res.items():
           phot_targ[k] = v
   
       # Targetocentric time: the time when the light departed the target
       phot_targ["target_jd"] = (Time(row["datetime_jd"], format='jd') + row["lighttime"]*u.s).jd
       
       # Standardized magnitude
       phot_targ["mstd"] = phot_targ["mag"] + phot_targ["Zpt"]
       phot_targ["e_mstd"] = np.sqrt(phot_targ["merr"]**2 + phot_targ["e_Zpt"]**2)
       
       # Reduced magnitude (error is same as e_mstd)
       phot_targ["mred"] = phot_targ["mstd"] - 5*np.log10(row['r']*row['delta'])
   
       # Include all minor details for debugging purpose:
       for c in row.columns:
           phot_targ[c] = row[c]
       
       plt.savefig(figpath)
       
       phot_targs.append(phot_targ)
   ```

   * NOTE: Because of the problem of matplotlib, your computer may suffer memory problem. So please be careful (backup your data before running the above code block) just in case. If that happens, you may remove the code lines which does "plotting" in the ``plotting`` function, and remove all matplotlib related code lines.
   * NOTE: If you want, you may save figure as png, but that consumes much larger disk space than PDF when enough dpi is used (e.g., ``plt.savefig("~~.png", dpi=300)``). 

5. In solar system sciences, we use "reduced magnitude", which is "the magnitude of the identical object under the identical geometric configuration, if the Sun-asteroid distance is 1 au and the observer-asteroid distance is 1 au". From Pogson's formula, derive the relationship between the reduced and standardized magnitude and justify the code in the previous question (no need to show derivation) (I did | I didn't).



### 3. Light Curve

1. Plot the light curve. What is the rough rotational period of this asteroid? Note that an asteroid should show two-peak-two-trough shape, unlike such as variable star. 

   ```python
   phot_targs_tab = vstack(phot_targs)
   
   phot_targs_tab.write(TOPPATH/"20191012_2005UD_phot.csv")
   
   baddata = sigma_clip(phot_targs_tab["mred"], sigma=2., maxiters=5).mask
   baddata |= phot_targs_tab["e_mstd"] > 0.1
   
   x = phot_targs_tab["target_jd"]
   x = (x - x.min()) * 24  # to hours
   y = phot_targs_tab["mred"]
   yerr = phot_targs_tab["e_mstd"]
   
   fig, axs = plt.subplots(1, 1, figsize=(8, 5), 
                           sharex=False, sharey=False, gridspec_kw=None)
   axs.errorbar(x[~baddata], y[~baddata], yerr=yerr[~baddata], 
                ls='', capsize=3, marker='o', color='k',
                label="data")
   axs.errorbar(x[baddata], y[baddata], yerr=yerr[baddata], 
                ls='', capsize=3, marker='x', color='r', 
                label=f"bad data (N = {np.count_nonzero(baddata)})")
   axs.legend()
   axs.set(xlabel="Time (hr)", ylabel=r"Reduced $\mathrm{R_C}$ magnitude")
   yvu.linticker(axs, xmajlockws=1, xminlockws=0.2, ymajlockws=0.1, yminlockws=0.05)
   plt.tight_layout()
   fig.align_ylabels(axs)
   fig.align_xlabels(axs)
   plt.show()
   ```

2. Use the similar code, but now "fold" the light curve based on  your estimated rotational period. 

   * Hint: you may add only one single line such as ``x = x%<your estimated rotational period>``.

3. Find the rotational period (or simply check the one you obtained above) with interacitve ipython (I did | I didn't):

   ```python
   from ipywidgets import interact, interactive, fixed, interact_manual
   import ipywidgets as widgets
   
   def plot_lc(prot):
       x = phot_targs_tab["target_jd"]
       x = (x - x.min()) * 24  # to hours
       y = phot_targs_tab["mred"]
       yerr = phot_targs_tab["e_mstd"]
       x = x%prot
   
       fig, axs = plt.subplots(1, 1, figsize=(8, 5), 
                           sharex=False, sharey=False, gridspec_kw=None)
       ax = axs
       ax.errorbar(x[~baddata], y[~baddata], yerr=yerr[~baddata], 
                    ls='', capsize=3, marker='o', color='k',
                    label="data")
       ax.errorbar(x[baddata], y[baddata], yerr=yerr[baddata], 
                    ls='', capsize=3, marker='x', color='r', 
                    label=f"bad data (N = {np.count_nonzero(baddata)})")
       ax.legend()
       ax.set(xlabel="Time (hr)", ylabel=r"Reduced $\mathrm{R_C}$ magnitude")
       yvu.linticker(ax, xmajlockws=1, xminlockws=0.2, ymajlockws=0.1, yminlockws=0.05)
       plt.tight_layout()
       fig.align_ylabels(ax)
       fig.align_xlabels(ax)
       plt.show()
       
       
   s_p = widgets.SelectionSlider(description="Rotational Period [hr]", 
                                 options=np.arange(5, 5.5, 0.01))    
   
   interact(plot_lc, prot=s_p)
   ```

4. To understand the causes of largely scattered data, we may overplot the airmass, s_Z (standard deviation of Z values) and linSlope (linearity curve slope when slope is not fixed to 1). Plot it and see some "scattered" magnitudes are caused by one or more of these (I checked|I didn't check).

   ```python
   errbfmt = dict(capsize=0, elinewidth=0.5, ls='')
   dummy = ([np.nan], [np.nan])
   cols = ['k', 'r', 'g', 'b']
   x = phot_targs_tab["target_jd"]
   x = (x - x.min()) * 24  # to hours
   y = phot_targs_tab["mred"]
   yerr = phot_targs_tab["e_mstd"]
   airmass = phot_targs_tab['airmass']
   dlinSlope = 1 - phot_targs_tab["linSlope"]
   Zstd = phot_targs_tab["Zstd"]
   
   fig, axs = plt.subplots(1, 1, figsize=(10, 6))
   ax = axs
   ax.errorbar(x, y, yerr=yerr, **errbfmt,
               label="data", marker='o', color='k', mfc='none',
               alpha=0.3)
   ax.plot(*dummy, 'r.', label="airmass")
   ax.plot(*dummy, 'g+', label="zpStd")
   ax.plot(*dummy, 'bx', label="1 - linSlope")
   
   for i, xpos in enumerate(x):
       ax.axvline(xpos, lw=0.1, color=cols[i%len(cols)])
   
   ax_a = ax.twinx()
   ax_a.plot(x, airmass, 'r.', alpha=0.3)
   ax_a.set_ylabel("airmass", color='r')
   ax_a.tick_params('y', colors='r')
   
   ax_s = ax.twinx()
   ax_s.spines["right"].set_position(("axes", 1.1))
   ax_s.plot(x, Zstd, 'g+')
   ax_s.set_ylabel("Std of Z", color='g')
   ax_s.tick_params('y', colors='g')
   
   ax_l = ax.twinx()
   ax_l.spines["right"].set_position(("axes", 1.2))
   ax_l.plot(x, dlinSlope, 'bx')
   ax_l.set_ylabel("1 - linSlope", color='b')
   ax_l.tick_params('y', colors='b')
   
   
   ax.set(ylim=(17.9, 16.8),
          xlabel="Time (hr)", 
          ylabel="Reduced Magnitude")
   ax.legend(loc=1, ncol=4, bbox_to_anchor=(1, -0.1))
       
   yvu.linticker(ax, xmajlockws=1, xminlockws=0.2, ymajlockws=0.1, yminlockws=0.05, 
                 xmajgrids=False, xmingrids=False)
   ```



### 4. Some Science

1. Consider a spherical asteroid of diameter D is viewed at opposition (full-moon phase). The albedo at the opposition at the wavelength of interest is p. If the asteroid is located at 1 au from the Sun and 1 au from the observer, what is the relationship between D, p, and the magnitude H (called the "absolute magnitude" in solar system sciences)? Say the Sun has magnitude m at the wavelength.
   * Answer: $ D = \frac{2 \,\mathrm{au} \times 10^{m/5}}{\sqrt{p}} \times 10^{-H/5} $. In V-band, using 1 au = 1.496e+8 km and m=-26.74, we can calculate the numerator 1342 km. But historically, people use D ~ 1329 km/sqrt(p) * 10^(-H/5)^. 1329 is anyway within the error-range of V_sun.
2. Our target 2005 UD was observed near the opposition (see ``alpha``, the Sun-target-observer angle in the ephemerides), so our standardized magnitude is roughly the absolute magnitude H in R-band. From multi-band photometry, we know it has V-R color of 0.35. What is the H of 2005 UD in V-band?
3. From polarimetric observations, we also know the p value in V-band is roughly 0.10 +/- 0.01 from some empirical relationships. What is the diameter and rough error-bar of 2005 UD?
4. For a rigid body of ellipsoidal shape with axes ``a > b = c`` (prolate) with spin axis parallel to c, what is the smallest rotational period for a particle at the farthest tip of the equator to be bounded to the gravity? Assume a constant bulk mass density ρ. (I did | I didn't)
   * Hint: ``GM/a^2 = aω^2 = (2π/P)^2*a``, ``M = 4πab^2ρ/3`` and solve for P. 
   * Answer: $ P = \frac{a}{b} \times \sqrt{\frac{3\pi}{G\rho}} $ [sec] or $ P = 2.334 \times \frac{a}{b} \times \left( \frac{\rho}{\mathrm{2,000 kg/m^3}} \right)^{-1/2} $ [hour]
5. Say we observed 2005 UD perpendicular to its spin axis (sub-observer's point on the equator). Also assume 2005 UD was a prolate ellipsoid with spin axis parallel to c. From the light curve, the oscillation amplitude was 0.3 mag. What is the ratio a/b?
   * Hint: Use Pogson's formula, and note that the observed flux is proportional to the projected area of the asteroid.
6. Now assume the bulk mass density ρ=2,000 kg/m3 for 2005 UD. Is this rotating fast enough so that the particles can "escape" from the asteroid? (yes | no)



If I use all the data from 2018-10-12 (which is 17 GB) and 2018-10-13 using much detailed photometry, our research group could obtain the following light curve with the following results (Ishiguro, Bach, Geem et al., 2020, in prep):

![](figs/asteroid_light_curve.png)

```
Period[day]: 0.218282 +/- 0.000092
Amplitude[mag]: 0.293
Mean magnitude[mag]: 17.182 at 2018-10-12, 17.189 at 2018-10-13
```







