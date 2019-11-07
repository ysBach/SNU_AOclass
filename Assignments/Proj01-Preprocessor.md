# Project 01

In this project, you will make a set of functions and scripts. 



Please submit a simple report (including the code, showing *some* results, and giving simple explanations) which you think the TA can evaluate whether you finished the task appropriately. You may need to re-use these in your final report. 

You may refer to the presentation material from this repo (the first lecture material of the TA seminar).



You don't need to answer all the questions separately. But all these processes are essential to get the final result of this project. Thus, please regard these items (Problems) as checklist: You don't have to make an answer sheet like "answer to number 1: blahblah". Just make codes which work well, and present the results.



## Problems [80 pt]

Download your raw FITS files from https://sao.snu.ac.kr (as we learned in the class). If you don't have any data, you can just test with other teams' data sets, and utilize the code for your data when you acquire it.



Make a code script, and/or module and/or package, which may include functions, classes, or whatever you may need (as many as you wish), to do the followings:

1. **Automatically classify** any input FITS file into one of ``['bias', 'dark', 'flat', 'comp', 'objt']``.
   * The ``flat`` can either be flat lamp image, dome flat, or sky flat. 
   * The ``comp`` is the comparison (arc lamp) in spectroscopy. 
   * The ``objt`` is the light frame image of any celestial object, other than calibration frames.
2. **Combine** to make master bias, dark, and flat. [1 & 2 = 40 pt]
   * bias must be median combined. 
   * dark must be median combined for *each exposure time*. Then bias subtracted.
   * For each flat, it must be first bias and dark subtracted. Use the dark of the same exposure time as your flat. Then normalize each flat by its average. Then the normalized flats must be median combined for *each filter* (in polarimetry, for each wave-plate angle; in spectroscopy, for each slit/grating/... setting). 
   * Depending on your choice, you can use sigma clipping for combining processes.
   * You may develope combiner by yourself, but also you can use [``ccdproc.combine``](https://ccdproc.readthedocs.io/en/latest/image_combination.html) 
3. **Save** the obtained master bias, dark, and flat. [10 pt]
   * Each dark and flat files must have indicators for its exposure time, filter, etc, to distinguish it from the other images of the same kind.
4. Do **preprocessing** for `comp` and `objt` (bias subtraction, dark subtraction, flat correction). [20 pt]
   * Note that dark must be used with the same exposure time, and flat must be with the same filter or other settings.
   * You may do cosmic-ray rejection, by benchmarking the L.A.Cosmic.

5. **Save** the preprocessed images as separate files. [10 pt]

   * You may put them in a separate directory, which will be easier for you to check.

   * You may put ``_bxx``, ``_bdx``, ``_bdf`` at the start/end of the original file name to indicate the preprocessing.

### Conditions

1. You must use the header information, not the file names or hand-written log.

2. Please try **not** to import packages **other than**

   * python default packages (e.g., `pathlib`, `itertools`, etc)

   * Basic science packages: ``numpy``, ``scipy``, ``astropy``, ``scikit learn``
   * Basic astropy-affiliated packages: ``ginga``, ``imexam``, ``ccdproc``, ``photutils``, ``specutils``
   * But you may benchmark the source codes from other packages. For instance, "[**Python users in Astronomy**](https://www.facebook.com/groups/astropython/)" group of Facebook, and the Gist/snippets they communicate with, or random GitHub repo, or our lecture notes or ``ysfitsutilpy``, ``ysphotutilpy``, ``TRIPOLpy``, and ``SNUO1Mpy``. Many times, the ready-made packages may not fulfill your needs. You must write codes by yourself by benchmarking the packages' source codes.

3. Later you may use the codes for your semester project work. Please try to make it **as reusable as possible**. (Google for "DRY principle")

### NOTE

It's always better to archive what you've done into the header information. After bias, dark, and flat corrections, for instance, add history and comments to FITS header as we did in the homework.

Also you may refer to the snippet we used in the class:

```python
from pathlib import Path
from astropy.io import fits
import pandas as pd
#%%
allfits = list(Path("2019-10-15").glob("*.fit"))
hdul = fits.open(allfits[0])
data = hdul[0].data
hdr = hdul[0].header

print(data[:1,:10])
#%%
fpaths = dict(bias=[], dark={}, flat=[], comp=[], objt=[])
objt_name = []

allfits.sort()

for fpath in allfits:
    hdr = fits.getheader(fpath)
    imagetyp = hdr["IMAGETYP"].lower()
    exptime = float(hdr["EXPTIME"])
    obs_object = hdr["OBJECT"]
    if imagetyp.startswith("bias frame") and exptime == 0.:
        fpaths['bias'].append(fpath)
    elif imagetyp.startswith('dark frame'):
        try:
            fpaths['dark'][exptime]
        except KeyError:
            fpaths['dark'][exptime] = []
        fpaths['dark'][exptime].append(fpath)
        
    elif imagetyp.startswith('flat field'):
        fpaths['flat'].append(fpath)
    elif imagetyp.startswith('light frame') and obs_object.lower() == 'comp':
        fpaths['comp'].append(fpath)
    else:
        fpaths['objt'].append(fpath)
        objt_name.append(hdr["OBJECT"])
```

