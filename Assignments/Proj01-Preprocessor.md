# Project 01

In this project, you will make a set of functions and scripts. 

## Problem

Make a code script, and/or module and/or package, which may include functions, classes, or whatever you may need (as many as you wish), to do the followings:

1. **Automatically classify** any input FITS file into one of ``['bias', 'dark', 'flat', 'comp', 'objt']``. 
   * The ``flat`` can either be flat lamp image, dome flat, or sky flat. 
   * The ``comp`` is the comparison (arc lamp) in spectroscopy. 
   * The ``objt`` is the light frame image of any celestial object, other than calibration frames.
2. **Combine** to make master bias, dark, and flat.
   * bias must be median combined. 
   * dark must be median combined for *each exposure time*. Then bias subtracted.
   * For each flat, it must be first bias and dark subtracted. Use the dark of the same exposure time as your flat. Then normalize each flat by its average. Then the normalized flats must be median combined for *each filter* (in polarimetry, for each wave-plate angle; in spectroscopy, for each slit/grating/... setting). 
   * Depending on your choice, you can use sigma clipping for combining processes.
   * You may develope combiner by yourself, but also you can use [``ccdproc.combine``](https://ccdproc.readthedocs.io/en/latest/image_combination.html) 
3. **Save** the obtained master bias, dark, and flat.
   * Each dark and flat files must have indicators for its exposure time, filter, etc, to distinguish it from the other images of the same kind.
4. Do **preprocessing** for `comp` and `objt` (bias subtraction, dark subtraction, flat correction).
   * Note that dark must be used with the same exposure time, and flat must be with the same filter or other settings.
   * You may do cosmic-ray rejection, by benchmarking the L.A.Cosmic.

5. **Save** the preprocessed images as separate files.

   * You may put them in a separate directory, which will be easier for you to check.

   * You may put ``_bxx``, ``_bdx``, ``_bdf`` at the start/end of the original file name to indicate the preprocessing.

### Conditions

1. You must use the header information, not the file names or hand-written log.

2. Please try **not** import packages **other than**

   * python default packages (e.g., `pathlib`, `itertools`, etc)

   * Basic science packages: ``numpy``, ``scipy``, ``astropy``
   * Basic astropy-affiliated packages: ``ginga``, ``imexam``, ``ccdproc``, ``photutils``, ``specutils``
   * But you may benchmark the source codes from other packages. For instance, "**Python users in Astronomy**" group of Facebook, and the Gist/snippets they communicate with, or random GitHub repo, or our lecture notes or ``ysfitsutilpy``, ``ysphotutilpy``, ``TRIPOLpy``, and ``SNUO1Mpy``. Many times, the ready-made packages may not fulfill your needs. You must write codes by yourself by benchmarking the packages' source codes.

3. Later you may use the codes for your semester project work. Please try to make it **as reusable as possible**.

### NOTE

It's always better to archive what you've done into the header information. After bias, dark, and flat corrections, for instance, add history and comments to FITS header as we did in the homework.