# AO2019
TA seminar notes for the AO classes in 2019 at SNU, Korea. All the lecture notes are primarily made by **Yoonsoo P. Bach**. I tried not to make typo, logically wrong statement, etc. If any problem is there in the note, that's solely my fault, so please be kind and let me know so that the notes can be updated.



## Short History

| Semester    | Instructor                  | TA                                        |
| ----------- | --------------------------- | ----------------------------------------- |
| 2019 Spring | professor Masateru Ishiguro | Sunho Jin, Yoonsoo P. Bach (only seminar) |
| 2018 Fall   | professor Masateru Ishiguro | Sunho Jin, Yoonsoo P. Bach (unofficial)   |
| 2018 Spring | professor Masateru Ishiguro | Sunho Jin, Yoonsoo P. Bach (unofficial)   |
| 2017 Fall   | professor Masateru Ishiguro | Yoonsoo P. Bach (& Da-Eun Kang)           |
| 2017 Spring | professor Masateru Ishiguro | Yoonsoo P. Bach (& Na-Eun Shin)           |
| 2016 Fall   | professor Masateru Ishiguro | Yoonsoo P. Bach                           |

- In 2019: Made this repo.
- In 2018: Made GitHub repo [link](https://github.com/ysBach/AO_LectureNotes) and [website](https://ysbach.github.io/AO_LectureNotes/). Many documents changed from ipynb to md.
- In 2017: Made GitHub repo [AO_2017](https://github.com/ysBach/AO_2017) and [website](https://ysbach.github.io/AO_2017/). 
- In 2016: No GitHub, but just MS Word-based lecture notes of PyRAF.



## To Use This Repo

You may have your preferences to use this repo. One of the possible suggestions is to clone/fork this repo and pull regularly to keep updated:

```
$ cd <Where you want to download this lecture note>
```

For the first time only:

```
$ git clone https://github.com/ysBach/AO2019.git
```

From the second time:

```
$ git pull
```



## Seminar Contents

The following lecture notes *only* gives you idea how to use tools for data reduction. **You must be aware of what you are doing!** Identical procedure to the lecture note may give different results, depending on what you've done other than what I did when I make the notes.



### Book

Fundamental ideas, formulation, and definition/theorems are given in the book material. Look at the `Books` directory in this repo or just the compiled TeX: [main.pdf](https://github.com/ysBach/AO2019/blob/master/Books/main.pdf)

**The codes** to make simple plots in the Book are given mostly as ipython notebooks in `Books/codes` of this repo. I recommend [this nbviewer hosting](https://nbviewer.jupyter.org/github/ysbach/AO2019/tree/master/Books/codes/).



### Notebooks

The demonstration (python codes) for more elaborating examples are given as separate Notebooks in [this nbviewer link](https://nbviewer.jupyter.org/github/ysbach/AO2019/tree/master/Notebooks/).



Some of Part 0, S, and A are not covered in the class.

#### Part 0: Preparation

* [00-0_Preface.md](https://github.com/ysBach/AO2019/blob/master/Notebooks/00-0_Preface.md)
* [00-1_Softwares.md](https://github.com/ysBach/AO2019/blob/master/Notebooks/00-1_Softwares.md)
* [00-2_UNIX.md](https://github.com/ysBach/AO2019/blob/master/Notebooks/00-2_UNIX.md)
* Statistics (See the Book above)



#### Part 1: Photometry

1. [Note 01](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/01-imexam.ipynb): ``imexam`` 
2. [Note 02](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/02-Opening_FITS.ipynb): Simple ``astropy.io.fits``.
3. [Note 03](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/03-Query.ipynb): `astroquery` (Vizier and JPL HORIZONS)
4. [Note 04](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/04-Aperture_Phot_01.ipynb): Aperture Photometry of single star (`photutils` and `astroquery`)
5. [Note 05](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/05-Differential_Phot.ipynb): Differential Aperture Photometry (`ysfitsutilspy` and `ysphotutilspy`)



#### Part <u>S</u>: Non-Python <u>S</u>oftwares or <u>S</u>ervices

* [S01_IRAF.md](https://github.com/ysBach/AO2019/blob/master/Notebooks/S01_IRAF.md)
* astrometry.net
* SExtractor

#### Part <u>A</u>: <u>A</u>ppendices

* [A01_HW.md](https://github.com/ysBach/AO2019/blob/master/Notebooks/A01_HW.md)
* [A02_TRIPOL.md](https://github.com/ysBach/AO2019/blob/master/Notebooks/A02_TRIPOL.md)
* [A03_TRIPOLpy_Tutorial](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/A03_TRIPOLpy_Tutorial.ipynb)

* A04_SNUO1Mpy_Tutorial



## Schedule

### 2019-04-22 (Mon)

* **Materials**: 
  * ``Book``'s *Statistics* chapter 

1. Statistics
   * Confidence Interval (CI)
   * The Central Limit Theorem and the meaning of it
   * Some distributions (Student t, Poisson) and Poisson process



### 2019-04-24 (Wed)

* **Materials**:
  * ``Book``'s *Idea of Photometry* chapter
  * KMTNet data (see `data/20180413SAAO_p4179*.fits` of this repo)
  * Install ``SAO ds9``

1. Visual detection of asteroids from KMTNet SAAO data (`SAO ds9`)

   * First introduction to FITS file (header, data, HDU, etc)

   * Frame WCS lock, blinking (ds9)
   * Regions, colormap, scale, smoothing (ds9)
   * Analysis using starcatalog and SkyBot (ds9)

2. Idea of Photometry

   * Point Spread Function (PSF)
   * Aperture summation
   * Sky estimation

3. Help desk for the installation
   * Git, Anaconda, ds9, etc.



### 2019-04-29 (Mon)

* **Materials**: 
  * ``Book``'s *Idea of Photometry* chapter
  * KMTNet data (see `data/20180413SAAO_p4179*.fits` of this repo)

1. [Note 01](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/01-imexam.ipynb): ``imexam`` to do crude photometry.

   - Currently I couldn't find a way to use ``imexam`` on Windows. If you want, please open new [**issues**](https://github.com/spacetelescope/imexam/issues) to ``imexam`` developers.
   
2. [Note 02](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/02-Opening_FITS.ipynb): Simple manipulation of FITS files using ``astropy.io.fits``.

   

### 2019-05-01 (Wed)

* Materials:
  * ``Book``'s *Standardization* chapter

1. [Note 03](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/03-Query.ipynb): Query catalogued objects using `astroquery` if WCS is given (UCAC, Pan-STARRS, JPL HORIZONS).



### 2019-05-08 (Wed)

1. [Note A03_TRIPOLpy_Tutorial](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/A03_TRIPOLpy_Tutorial.ipynb): Photometric preprocessing demonstration from TRIPOL (2019-05-03)
3. What if WCS is broken: Astrometry.net



### 2019-05-13 (Mon)

* Materials:
  * ``Book``'s *Standardization* chapter

1. [Note 03](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/03-Query.ipynb): Review
2. [Note 04](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/04-Aperture_Phot_01.ipynb): Aperture Photometry of single star using python (photutils and astroquery)
3. [Note 05](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/05-Differential_Phot.ipynb): Differential Aperture Photometry to get standardized magnitude of asteroid



### 2019-05-15 (Wed)

