## Goals

**I am assuming you are familiar with python ``pathlib`` and ``astropy.io.fits`` by now.**

* Use ``astropy.io.fits`` and ``pathlib`` to rename FITS files using the header information.
* Using **ysfitsutilpy**:
  * Make a summary file.
  * Select bias, dark, flat, and object frames automatically using the header information.
  * Combine calibration frames to make master bias, dark, and flat.



## Instructions

**You need at least ~ 1 GB of free space on your computer.**

### 1. Install

For installation of ysfitsutilpy, go to [https://github.com/ysBach/ysfitsutilpy](https://github.com/ysBach/ysfitsutilpy).

After the first installation, you should always update it by

```
$ git pull && python setup.py install
```

and restart your python kernel.

### 2. Download data

Download ``155140_2005UD_20181012_SNUO.zip`` from our Tutorial_Data (see README of this repo) and unzip this.

### 3. Start of the code

Run the following before you run any code below.

```python
from pathlib import Path
import numpy as np
from astropy.nddata import CCDData
from astropy.io import fits
from astropy.time import Time

import ysfitsutilpy as yfu

USEFUL_KEYS = ["DATE-OBS", "FILTER", "OBJECT", "EXPTIME", "IMAGETYP",
               "AIRMASS", "XBINNING", "YBINNING", "CCD-TEMP", "SET-TEMP",
               "OBJCTRA", "OBJCTDEC", "OBJCTALT"]

TOPPATH = Path(?)  # the directory you saved the FITS files
ORIGDIR = TOPPATH/"archive"
RAWDIR = TOPPATH/"raw"
CALDIR = TOPPATH/"calib"
ORIGDIR.mkdir(parents=True, exist_ok=True)
RAWDIR.mkdir(parents=True, exist_ok=True)
CALDIR.mkdir(parents=True, exist_ok=True)
```



## Explanation on data

The data you will download are photometric observation data at SNU Astrophysical Observatory (SAO or SNUO) using 1-m telescope on 2018-10-12. The object was (155140) 2005 UD, an asteroid thought to be a "sibling" of asteroid (3200) Phaethon (Phaethon is the asteroid responsible for Geminid meteoride). Other information such as filter or exposure time, please look into the header by yourself.

The data available from the tutorial data are **NOT** the original data. The original data from SNUO 1m telescope is in ``.fit`` format (not ``.fits``) and is 33MB in ``int16``, and it will become 67MB after flat fielding (``float32``), which is too large a file size. Therefore, I binned the data (4x4) by averaging, and the pixel scale changed from 0.31"/pix to 1.2"/pix. The FWHM is around 1"-2", this is slightly undersampled but still useful. The data size now is reduced by factor of 16, so each frame is ~2MB and flat fielding will yield ~4MB files. Also the WCS information is applied to the FITS file.

<details><summary>I used the following code for reducing the file size (click)</summary>
<p>
**Please do not run this code by yourself**.



```python
import ysfitsutilpy as yfu
from pathlib import Path
from astropy.io import fits

def iterator(it):
    try:
        from tqdm import tqdm
        toiter = tqdm(it)
    except ImportError:
        toiter = it
    return toiter


def make_astrometry_script(allpaths, output=Path("astrometry.sh"),
                           log=Path("astrometry.log"), 
                           indexdir=Path('.'), cfg=Path("astrometry.cfg")):

    str_time = (r'current_date_time="`date +%Y-%m-%d\ %H:%M:%S`";'
                + 'echo $current_date_time;')
    str_mv = "mv {} {}/input.fits"
    str_wcs = ("solve-field {}/input.fits -N {}"
               + " --ra {} --dec {}"
               + " --nsigma 15 --downsample 2"
               + " --radius 0.2 -u app -L 1.20 -U 1.26"
               + " --cpulimit 300 --no-plot --overwrite --no-remove-lines")
    if not Path(cfg).exists():
        print(f"astrometry config not found at {cfg} you specified.\n"
             + f"Making it at path {cfg} using "
             + f"the index directory ({indexdir}) you specified.")
        str_cfg = """
# This is a config file for the Astrometry.net 'astrometry-engine'
# program - it contains information about where indices are stored,
# and "site policy" items.

# Check the indices in parallel?
#
# -if the indices you are using take less than 2 GB of space, and you have at least
#  as much physical memory as indices, then you want this enabled.
#
# -if you are using a 64-bit machine and you have enough physical memory to contain
#  the indices you are using, then you want this enabled.
# 
# -otherwise, leave it commented-out.

inparallel

# If no scale estimate is given, use these limits on field width.
# minwidth 0.1
# maxwidth 180

# If no depths are given, use these:
#depths 10 20 30 40 50 60 70 80 90 100

# Maximum CPU time to spend on a field, in seconds:
# default is 600 (ten minutes), which is probably way overkill.
cpulimit 300

# In which directories should we search for indices?
add_path {:s}

# Load any indices found in the directories listed above.
autoindex

## Or... explicitly list the indices to load.
#index index-219
#index index-218
#index index-217
#index index-216
#index index-215
#index index-214
#index index-213
#index index-212
#index index-211
#index index-210
#index index-209
#index index-208
#index index-207
#index index-206
#index index-205
#index index-204-00
#index index-204-01
#index index-204-02
#index index-204-03
#index index-204-04
#index index-204-05
#index index-204-06
#index index-204-07
#index index-204-08
#index index-204-09
#index index-204-10
#index index-204-11
#index index-203-00
#index index-203-01
#index index-203-02
#index index-203-03
#index index-203-04
#index index-203-05
#index index-203-06
#index index-203-07
#index index-203-08
#index index-203-09
#index index-203-10
#index index-203-11
#index index-202-00
#index index-202-01
#index index-202-02
#index index-202-03
#index index-202-04
#index index-202-05
#index index-202-06
#index index-202-07
#index index-202-08
#index index-202-09
#index index-202-10
#index index-202-11
#index index-201-00
#index index-201-01
#index index-201-02
#index index-201-03
#index index-201-04
#index index-201-05
#index index-201-06
#index index-201-07
#index index-201-08
#index index-201-09
#index index-201-10
#index index-201-11
#index index-200-00
#index index-200-01
#index index-200-02
#index index-200-03
#index index-200-04
#index index-200-05
#index index-200-06
#index index-200-07
#index index-200-08
#index index-200-09
#index index-200-10
#index index-200-11
"""

        with open(Path(cfg), 'w+') as ff:
            ff.write(str_cfg.format(str(indexdir.resolve())))

    with open(Path(output), "w+") as astrometry:
        astrometry.write(str_time)
        astrometry.write("\n")
        for fpath in allpaths:
            fpath = Path(fpath)
            hdr = fits.getheader(fpath)
            ra = hdr["OBJCTRA"].replace(" ", ":")
            dec = hdr["OBJCTDEC"].replace(" ", ":")
            fparent = fpath.parent
            astrometry.write(str_mv.format(fpath, fparent))
            astrometry.write("\n")
            astrometry.write(str_wcs.format(fparent, fpath, ra, dec))
            astrometry.write("\n")
            astrometry.write(str_time)
            astrometry.write("\n")
        astrometry.write(f"rm {fparent}/input.*\n")
        astrometry.write(str_time)


TOPPATH = Path("./archive")  # Tune this part to appropriate path
OUTDIR = Path("./original")  # Tune this part to appropriate path
allfits = list(TOPPATH.glob("*.fit"))
allfits.sort()

toiter = iterator(allfits)

for fpath in toiter:
    if fpath.name.startswith("2005"):
        counter = int(fpath.name.split('-')[-1].split('.')[0])
        hdrkw = dict(IMAGETYP='Light Frame', OBJECT='2005UD')
        if counter % 4 != 0:
            continue
    elif fpath.name.lower().startswith("sa") or fpath.name.lower().startswith("skyflat"):
        continue
    elif fpath.name.startswith("Cali-"):
        if "Bias" in fpath.name:
            hdrkw = dict(IMAGETYP='Dark Frame', OBJECT='Bias')
        else:
            hdrkw = dict(IMAGETYP='Dark Frame', OBJECT='Dark')
    elif fpath.name.startswith("flat"):
        hdrkw = dict(IMAGETYP='Light Frame', OBJECT='Flat')

    ccd = yfu.load_ccd(fpath)
    nccd = yfu.bin_ccd(ccd, 4, 4)
    for k, v in hdrkw.items():
        nccd.header[k] = v
    nccd.data = np.floor(nccd.data)
    nccd = yfu.CCDData_astype(nccd, 'uint16')
    newpath = OUTDIR/(fpath.stem + ".fits")
    nccd.write(newpath, overwrite=True)

allpaths = list(OUTDIR.glob("2005*.fits"))
make_astrometry_script(allpaths)
```

For WCS, for first time use:

    $ docker pull dm90/astrometry

Then:

    $ docker run --name nova --restart unless-stopped -v ~/Downloads/astrometry.net/data:/usr/local/astrometry/data -v ~/Downloads:/Downloads -p 8000:8000 dm90/astrometry

From Docker desktop → Dashboard → CLI and

    $ cd Downloads 
    $ bash astrometry.sh

It takes ~ 10 sec for each frame, so total ~100 sample frames took ~ 15 min to implement WCS.

</p>
</details>



## Problems

2 pts each, unless specified.

### 1. Looking at the header

1. Download and unzip the data to a directory you want. I will call that directory ``TOPPATH``, so that ``allfits = list(TOPPATH.glob("*.fits"))`` results in the list of all fits file paths. After doing ``allfits.sort()``, what is the 0-the element of ``allfits``?

   * Hint: ``allfits = list(TOPPATH.glob("*.fits"))``, ``allfits.sort()``, ``allfits[0]``.

2. Load that FITS file (``allfits[0]``), and see the header by, e.g., python, DS9, ``fitsheader`` in terminal, etc. (I did|I didn't)

3. What are the header keyword for (1) date and time of the start of the exposure, (2) filter, and (3) exposure time? [1 pt each]

4. Load the file in python as ``CCDData`` object, and set ``hdr`` as the header of the file. **Print** the 3 values by header keywords (e.g., ``print(hdr["<keyword>"])`` for keywords you found above.
   * Hint: To load as ``CCDData``, use ``ccd = CCDData.read(filepath, unit='adu')`` and ``hdr = ccd.header``.
   * See the official documentation for [``astropy.nddata.CCDData``](https://docs.astropy.org/en/stable/api/astropy.nddata.CCDData.html).

5. Set ``datetime`` as ``DATE-OBS`` in astropy time format.

   * Hint: ``datetime = Time(hdr["DATE-OBS"], format='isot')``. See [``astropy.time`` documentation](https://docs.astropy.org/en/stable/time/).

7. Print a string in the format of ``<object:s>_<YYYYmmdd-HHMMSS>_<filter:s>_<exposure:.1f>.fits``, such as ``2005UD_20181012-114904_R_60.0.fits``.
   * Hint: The format ``YYYYmmdd-HHMMSS`` means year in 4 digits, month in 2 digits, date in 2 digits, and then hour in 2 digits (24-hour), minute in 2 digits, and second in 2digits. You can use ``datetime_str = datetime.strftime('%Y%m%d-%H%M%S')``
   * Hint: For formatted string, you can use ``newname = f"{hdr['<keyword>']:s}_{datetime_str}_{hdr['<keyword>']:s}_{hdr['<keyword>']:.1f}.fits"``

   

### 2. Rename FITS

1. Sometimes it's useful to make a simple spreadsheet to look all the important header information at once. Run the following code to make a summary file : ``summary = yfu.make_summary(fitslist=allfits, keywords=USEFUL_KEYS, output="20181012.csv", pandas=True)``

2. Open the file (using, e.g., Excel) or print ``summary``. Please look at the file and think about how you can classify bias, dark, flat, and object frames using this header information. (I did|I didn't)

3. It's not always convenient to open and look at this summary file to know which file is which. The filename should be more informative. Rename all FITS as we did for ``newname``, but let all the original files be stored in a directory ``archive`` (backup data):

   ```python
   for fpath in allfits:
       ccd = CCDData.read(fpath)
       fpath.rename(ORIGDIR/fpath.name)
       hdr = ccd.header
       datetime = Time(hdr["DATE-OBS"], format='isot')
       datetime_str = datetime.strftime('%Y%m%d-%H%M%S')
       newname = f"{hdr['OBJECT']:s}_{datetime_str}_{hdr['FILTER']:s}_{hdr['EXPTIME']:.1f}.fits"
       newpath = RAWDIR/newname
       if newpath.exists():
           continue
       ccd.write(newpath)
   ```

4. Go to ``TOPPATH`` on your computer. (1) What is the total size of folders ``archive`` and ``raw``? (2) Are the number of files identical? (yes|no) [1 points each]

   * **NOTE**: If you are running out of disk space, delete ``archive`` folder.

5. Make a new summary file for ``RAWDIR`` and overwrite the old one:

   ```python
   allfits = list(RAWDIR.glob("*.fits"))
   allfits.sort()
   summary = yfu.make_summary(fitslist=allfits, keywords=USEFUL_KEYS, output="20181012.csv", pandas=True)
   ```



### 3. Master calibration frames

1. For bias, the simplest criteria to select them is if ``OBJECT`` is ``"Bias"``. For safety, let me add one more criteria ``IMAGETYP`` is ``"Dark Frame"``. How to median combine all of them? Simple as below. Make a master (median-combined) bias frame ``mbias.fits`` in ``CALDIR``.

   ```python
   mbias = yfu.combine_ccd(
       summary_table=summary, 
       type_key=["OBJECT", "IMAGETYP"], 
       type_val=["Bias", "Dark Frame"], 
       dtype='uint16'
   )
   mbias.write(CALDIR/"mbias.fits") # Save the master bias to calibration directory CALDIR
   # yfu.combine_ccd?  # documentation
   ```

2. Make the mbias **without** specifying ``dtype`` (remove the last line of the code). If you save it as ``dummy.fits``, what is the file size of it? 

   * The reason why they're different can be found by checking ``BITPIX`` in the headers of the two files.

3. See the statistics of bias by ``yfu.give_stats(mbias)``. You may see the doc by ``yfu.give_stats?`` from python. What is the rough average value of bias?

4. For dark, story gets a bit complicated. You have to make master dark **for each exposure time**. First, find out what exposure times were used for dark (unique elements of EXPTIME of dark frames). Then combine dark frames in each of the specific exposure time. **Then we have to subtract bias**. Make master dark frame ``mdark_<EXPTIME:.1f>.fits``  in ``CALDIR`` for all the exposure times.

   ```python
   dark_summary = summary[(summary["OBJECT"]=="Dark")]
   dark_exptimes = np.unique(dark_summary["EXPTIME"])
   dark_exptimes.sort()
   
   for dark_exptime in dark_exptimes:
       mdark_i = yfu.combine_ccd(
           summary_table=summary,
           type_key=["OBJECT", "IMAGETYP", "EXPTIME"], 
           type_val=["Dark", "Dark Frame", dark_exptime], 
           dtype='uint16',  # Before bias subtraction, it is always positive
       )
       # After bias subtraction, it can be negative, 
       # but not larger than 2^15 so use int16 than float32 or int32:
       mdark_i = yfu.bdf_process(
           mdark_i,
           mbiaspath=CALDIR/"mbias.fits",
           dtype='int16',  
           output=CALDIR/f"mdark_{dark_exptime:.1f}.fits"
       )
   ```

5. See the statistics of the longest exposure time dark by ``yfu.give_stats(mdark_i)``. Is the average of dark positive as expected?

   * **NOTE**: It happens some time that dark is negative. It is not easy to know the reason. But you may note that the maximum value of dark is much larger than bias: Hot pixels are at least visible.

6. Flats are trickier. You have to combine flats for each optics configuration (e.g., filter). Fortunately we have one filter. Unfortunately, we have different exposure times. What are the unique exposure times for flats we have?

   * **NOTE**: This is because they're sky flats.

7. Before making master flat, we need to subtract bias and dark from each flat frame. Because flats do not have identical exposure time, darks to be subtracted must be differ. Do the bias and dark subtraction for all the flats, and save them as ``<original_name>_bd.fits`` in ``CALDIR``.

   ```python
   flat_summary = summary[(summary["OBJECT"]=="Flat") 
                          & (summary["FILTER"]=="R")]
   for fpath in flat_summary["file"]:
       fpath = Path(fpath)
       ccd = CCDData.read(fpath)
       exptime = ccd.header["EXPTIME"]
       # After bias/dark subtraction, flat frames must have only positive pixel values.
       # If negative, it's either (1) bad flat or (2) pixels which anyway are bad pixels.
       # Therefore, don't care about negativity but use ``uint16`` to save space.
       yfu.bdf_process(
           ccd,
           mbiaspath=CALDIR/"mbias.fits",
           mdarkpath=CALDIR/f"mdark_{exptime:.1f}.fits",
           output=CALDIR/f"{fpath.stem}_bd.fits",
           normalize_median=True,  
       )
   ```
   
8. The mean count of the flat differ from file to file. Therefore, we need to normalize each frame. Because you see star trails in the flat frames, average is not a good option, so use median for normalization. Also due to the star trails, you'd better combine frames with a rejection such as sigma-clip. Make a master flat in ``float32`` datatype with 2-sigma clipped median combine. Save it as ``mflat_R.fits`` in ``CALDIR``.

   ```python
   flatpaths = list(CALDIR.glob("Flat_*_R_*_bd.fits"))
   
   mflat = yfu.combine_ccd(
       fitslist=flatpaths,
       reject_method='sigclip',
       sigma_clip_low_thresh=2,   # 2-sigma clipping
       sigma_clip_high_thresh=2,  # 2-sigma clipping
       mem_limit=2e+9,            # 2GB
       normalize_median=True,     # normalize by median.
   )
   mflat.write(CALDIR/"mflat_R.fits")
   ```



### 4. Wrapup

1. Open ``mbias.fits``. Describe at least 3 features you see from the image (e.g., gradient, bad column, hot pixels, etc). Close the ds9 after this.
2. Open three files (``mdark_10.0.fits``, ``mdark_20.0.fits``, ``mdark_60.0.fits``) as three tabs on ds9. You may use ``Frame`` → ``New`` → ``Open`` to open three files and then ``Frame`` → ``tile``. Lock images by image coordinate (``Frame`` → ``Lock`` → ``Frame`` → ``Image``). Using zoom in/out (mouse wheel) and mouse middle button (or ``Edit`` → ``pan``) to move your focus to pixel ``(x, y) = (481, 619)``. What are the pixel values in three frames?
3. Roughly calculate the dark current in ADU/s at that pixel. Assume the detector was at the identical temperature and ignore any noise/cosmic-ray hit. Close the ds9 after this.
4. Open ``mflat_R.fits``. Describe at least 3 features you see from the image.
5. Open the header of ``mflat_R.fits``. There are many ``HISTORY`` in that which is added by ``ysfitsutilpy``. What are the time spent due to (1) bias subtraction, (2) dark subtraction, and (3) image combination? [1 points each]

