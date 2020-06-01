This is a continuation from [master-frame making homework](./HW-preproc_01_mkmaster.md).

## Goals

**I am assuming you are familiar with python ``pathlib`` and ``astropy.io.fits`` by now.**

* Using **ysfitsutilpy**:
  * Do bias, dark, and flat fielding and cosmic-ray rejection.



## Instructions

**You need at least ~ 1 GB of free space on your computer.**

Run the following before you run any code below.

```python
from pathlib import Path
from astropy.nddata import CCDData

import ysfitsutilpy as yfu

TOPPATH = Path(?)  # the directory you saved the FITS files
RAWDIR = TOPPATH/"raw"
REDDIR = TOPPATH/"reduced"
REDDIR.mkdir(parents=True, exist_ok=True)
```

## Problems

5 points each

1. Among all the files in ``RAWDIR``, select only those of 2005 UD and make a list object named ``rawfits``.

   * Hint: ``rawfits = RAWDIR.glob("2005UD*.fits")``, because we put the object name as the prefix of the FITS files. 
   * Also run ``rawfits.sort()``

2. Reduce the first FITS file (``rawfits[0]``), i.e., do bias-subtraction, dark-subtraction, flat-fielding, and cosmic-ray rejection.

   ```python
   gain_original = 1.36
   rdnoise_original = 9.0 
   bin_area = 4*4
   gain = gain_original*bin_area
   rdnoise = rdnoise_original * np.sqrt(bin_area)
   
   fpath = rawfits[0]
   outpath = REDDIR/f"bdfc_{fpath.name}"
   ccd = CCDData.read(fpath)
   exptime = ccd.header["EXPTIME"]
   filt = ccd.header["FILTER"]
   proc = yfu.bdf_process(
       ccd, 
       mbiaspath=CALDIR/"mbias.fits", 
       mdarkpath=CALDIR/f"mdark_{exptime:.1f}.fits",
       mflatpath=CALDIR/f"mflat_{filt.upper():s}.fits",
       do_crrej=True,
       gain=gain,
       rdnoise=rdnoise,
       verbose_bdf=True,
       verbose_crrej=True,
       crrej_kwargs=dict(sepmed=True, objlim=4),
       output=outpath
   )
   ```

   * From the verbose output, you may find the cosmic-ray rejection is the part which consumes most (0.7 sec on my laptop, 90+%) of the time. If you don't specify ``sepmed=True``, it takes about 3 seconds on my laptop (more than 4 times slower).
   * Why did I change gain and rdnoise? Because we did 4x4 binning to the original FITS file by averaging the ``4*4 = 16`` pixels. By doing so, the total ADU of N in that area will become N/16, and therefore the effective gain is increased by the factor of 16. For readout noise, which is a standard deviation of a normal distribution, is propagated in that 16 pixels. The resulting value of 16-pixel mean will, therefoere, have the standard deviation of ``sqrt(16*variance) = sqrt(16*rdnoise_original**2)``.

3. Open the original file with DS9. Open the pre-processed version of that file which you have just made. Lock WCS (``Frame`` → ``Lock`` → ``Frame`` → ``WCS``). Can you see many (but not all) of cosmic-rays are removed?

4. You may have noticed the file size of the output FITS file is now doubled. Why is it?

   * In ``ysfitsutilpy.bdf_process`` and all other parts, ``dtype`` is set to ``'float32'`` by default. All other packages I know of (including ``ccdproc``), the default is ``float64`` and it is very difficult to change it to ``float32``, and therefore wasting twice the disk space. The total disk space used by ``CALDIR`` and``REDDIR`` are ~ 0.5 GB, and this means if you have used ``ccdproc``, you may have wasted additional 0.5 GB space.

5. But because we have asteroid, which is a point-like object compared to all other stars, in the FOV, simple CR-rejection technique may misunderstand our asteroid as a cosmic-ray. Also the stars have non-circular PSF, the CR-rejection sometimes distort the stars. So let's turn off the cosmic-ray rejection. Now iterate through all the FITS files, but let's silence the verbose option:

   ```python
   def iterator(it):
       try:
           from tqdm import tqdm
           toiter = tqdm(it)
       except ImportError:
           print("tqdm is not installed on your computer, but it won't be a problem.")
           toiter = it
       return toiter
   
   for fpath in iterator(rawfits):
       outpath = REDDIR/f"bdfc_{fpath.name}"
       ccd = CCDData.read(fpath)
       exptime = ccd.header["EXPTIME"]
       filt = ccd.header["FILTER"]
       proc = yfu.bdf_process(
           ccd, 
           mbiaspath=CALDIR/"mbias.fits", 
           mdarkpath=CALDIR/f"mdark_{exptime:.1f}.fits",
           mflatpath=CALDIR/f"mflat_{filt.upper():s}.fits",
           verbose_bdf=False,
           verbose_crrej=False,
           output=outpath
       )
   ```

   It took about 15s on TA's notebook. 