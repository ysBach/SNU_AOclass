# Notebooks

**!!!**: **All the notes below are accessible at [this nbviewer link](https://nbviewer.jupyter.org/github/ysbach/SNU_AOclass/tree/master/Notebooks/).**

* Some of Part 0, S, and A are not covered in the class.

* **Tutorial data** available [here](https://www.dropbox.com/sh/3a1j3495o08yweh/AACSPhIhLwut38yYX8mjvX3ka?dl=0) from my Dropbox.



## Part 0: Preparation

* [00-0_Preface.md](00-0_Preface.md)
* [00-1_Softwares.md](00-1_Softwares.md)
* [00-2_UNIX.md](00-2_UNIX.md)
* [00-3_Prepare_Python.md](00-3_Prepare_Python.md) - **Please read it!**
* **Go to [python prep directory](python_prep) and study python by yourself.**
* Statistics (See the [Books](../Books) directory)
* [references](references/) (Many refereces you may want to refer to)



## Part 1: Photometry

1. [Note 01](https://nbviewer.jupyter.org/github/ysbach/SNU_AOclass/blob/master/Notebooks/01-imexam.ipynb): ``imexam`` (Maybe it's not usable on Windows...?)
2. [Note 02](https://nbviewer.jupyter.org/github/ysbach/SNU_AOclass/blob/master/Notebooks/02-Opening_FITS.ipynb): Simple ``astropy.io.fits``.
3. [Note 03](https://nbviewer.jupyter.org/github/ysbach/SNU_AOclass/blob/master/Notebooks/03-Query.ipynb): `astroquery` (Vizier and JPL HORIZONS)
4. [Note 04](https://nbviewer.jupyter.org/github/ysbach/SNU_AOclass/blob/master/Notebooks/04-Aperture_Phot_01.ipynb): Aperture Photometry of single star (`photutils` and `astroquery`)
5. [Note 05](https://nbviewer.jupyter.org/github/ysbach/SNU_AOclass/blob/master/Notebooks/05-Differential_Phot.ipynb): Differential Aperture Photometry (`ysfitsutilspy` and `ysphotutilspy`)
6. [Note 06](https://nbviewer.jupyter.org/github/ysbach/SNU_AOclass/blob/master/Notebooks/06-Extended_Sources.ipynb): Extended source (``photutils``)
   1. [Note 06-1](https://nbviewer.jupyter.org/github/ysBach/SNU_AOclass/blob/master/Notebooks/06-1_photutils_SExtractorBackground_and_sep.ipynb): A technical (advanced) topic, ``SExtractorBackground`` (``photutils``) and ``sep``
7. [Note 07](https://nbviewer.jupyter.org/github/ysbach/SNU_AOclass/blob/master/Notebooks/07-Cosmic_Ray_Rejection.ipynb): Cosmic-Ray rejection (``astroscrappy``)
8. [Note 08](https://nbviewer.jupyter.org/github/ysbach/SNU_AOclass/blob/master/Notebooks/08-PSF_Extraction.ipynb): Extraction of PSF
9. [Note 09](https://nbviewer.jupyter.org/github/ysbach/SNU_AOclass/blob/master/Notebooks/09-PSF_Phot.ipynb): Do photometry from the extracted PSF



## Part 2: Spectroscopy

1. [Statistics](https://nbviewer.jupyter.org/github/ysBach/SNU_AOclass/blob/master/Notebooks/Spectroscopy_Simulation.ipynb): Is there really a line emission?
2. [Justification](https://nbviewer.jupyter.org/github/ysBach/SNU_AOclass/blob/master/Notebooks/Spectroscopy_in_Python.ipynb): Comparison of my personal notebook with IRAF results on Subaru FOCAS data
   * Adopted by [PyReduc project](https://keheintz.github.io/PyReduc/) ([github](https://github.com/keheintz/PyReduc)) as of 2020 Apr.
3. [SNUO 1m telescope](https://nbviewer.jupyter.org/github/ysBach/SNU_AOclass/blob/master/Notebooks/Spectroscopy_Example.ipynb): Spectrograph data from SNUO



## Part <u>S</u>: Non-Python <u>S</u>oftwares or <u>S</u>ervices

* [S01_IRAF.md](Notebooks/S01_IRAF.md)
* [S02_Installing_Astrometry_dot_net.md](Notebooks/S02_Installing_Astrometry_dot_net.md)
* SExtractor (see notes in [references/](references/))



## Part <u>A</u>: <u>A</u>ppendices

* [A02_TRIPOL.md](Notebooks/A02_TRIPOL.md)
* [A03_TRIPOLpy_Tutorial](https://nbviewer.jupyter.org/github/ysbach/SNU_AOclass/blob/master/Notebooks/A03_TRIPOLpy_Tutorial.ipynb)

* [A04_SNUO1Mpy_Tutorial](https://nbviewer.jupyter.org/github/ysbach/SNU_AOclass/blob/master/Notebooks/A04_SNUO1Mpy_Tutorial.ipynb)