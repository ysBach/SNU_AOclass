# SNU_AOclass
TA seminar notes for the AO classes from 2016-present at SNU, Korea. All the lecture notes are primarily made by **Yoonsoo P. Bach**. I tried not to make typo, logically wrong statement, etc. If any problem is there in the note, that's solely my fault, so please be kind and let me know so that the notes can be updated.


## 1. Short History
<details><summary>click</summary>
<p>

| Semester    | Instructor                  | TA                                         |
| ----------- | --------------------------- | ------------------------------------------ |
| 2020 Spring | professor Masateru Ishiguro | Jooyeon Geem, Yoonsoo P. Bach (unofficial) |
| 2019 Fall   | professor Masateru Ishiguro | Hangbin Jo, Yoonsoo P. Bach (unofficial)   |
| 2019 Spring | professor Masateru Ishiguro | Sunho Jin, Yoonsoo P. Bach (unofficial)    |
| 2018 Fall   | professor Masateru Ishiguro | Sunho Jin, Yoonsoo P. Bach (unofficial)    |
| 2018 Spring | professor Masateru Ishiguro | Sunho Jin, Yoonsoo P. Bach (unofficial)    |
| 2017 Fall   | professor Masateru Ishiguro | Yoonsoo P. Bach (& Da-Eun Kang)            |
| 2017 Spring | professor Masateru Ishiguro | Yoonsoo P. Bach (& Na-Eun Shin)            |
| 2016 Fall   | professor Masateru Ishiguro | Yoonsoo P. Bach                            |

- In 2020: The name of the repo changed (Jan). All previous repos (2017, 2018) are **archived** (Jan).
- In 2019: Made this repo.
- In 2018: Made GitHub repo [link](https://github.com/ysBach/AO_2018). Many documents changed from ipynb to md.
- In 2017: Made GitHub repo [AO_2017](https://github.com/ysBach/AO_2017) and [website](https://ysbach.github.io/AO_2017/). 
- In 2016: No GitHub, but just MS Word-based lecture notes of PyRAF.
</p>
</details>


## 2. To Use This Repo
<details><summary>click</summary>
<p>
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
</p>
</details>


## 3. Seminar Contents

The following lecture notes *only* gives you idea how to use tools for data reduction. **You must be aware of what you are doing!** Identical procedure to the lecture note may give different results, depending on what you've done other than what I did when I make the notes.



### 3-1. Book

Look at the `Books` directory in this repo or 

* PDF: [main.pdf](https://github.com/ysBach/AO2019/blob/master/Books/main.pdf). 
* **The codes** to make plots:  [link](https://nbviewer.jupyter.org/github/ysbach/AO2019/tree/master/Books/codes/).

-----

### 3-2. Lecture Notebooks

All the notes below are accessible at [this nbviewer link](https://nbviewer.jupyter.org/github/ysbach/AO2019/tree/master/Notebooks/).

* Some of Part 0, S, and A are not covered in the class.

* **Tutorial data** available [here](https://www.dropbox.com/sh/3a1j3495o08yweh/AACSPhIhLwut38yYX8mjvX3ka?dl=0) from my Dropbox.



#### Part 0: Preparation

* [00-0_Preface.md](Notebooks/00-0_Preface.md)
* [00-1_Softwares.md](Notebooks/00-1_Softwares.md)
* [00-2_UNIX.md](Notebooks/00-2_UNIX.md)
* Go to [python prep directory](Notebooks/python_prep) and study python by yourself.
* Statistics (See the Book above)
* [references](references/) (Many references you may want to refer to)



#### Part 1: Photometry

1. [Note 01](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/01-imexam.ipynb): ``imexam`` (Maybe it's not usable on Windows...?)
2. [Note 02](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/02-Opening_FITS.ipynb): Simple ``astropy.io.fits``.
3. [Note 03](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/03-Query.ipynb): `astroquery` (Vizier and JPL HORIZONS)
4. [Note 04](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/04-Aperture_Phot_01.ipynb): Aperture Photometry of single star (`photutils` and `astroquery`)
5. [Note 05](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/05-Differential_Phot.ipynb): Differential Aperture Photometry (`ysfitsutilspy` and `ysphotutilspy`)
6. [Note 06](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/06-Extended_Sources.ipynb): Extended source (``photutils``)
7. [Note 07](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/07-Cosmic_Ray_Rejection.ipynb): Cosmic-Ray rejection (``astroscrappy``)
8. [Note 08](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/08-PSF_Extraction.ipynb): Extraction of PSF
9. [Note 09](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/09-PSF_Phot.ipynb): Do photometry from the extracted PSF



#### Part 2: Spectroscopy

1. [Statistics](https://nbviewer.jupyter.org/github/ysBach/SNU_AOclass/blob/master/Notebooks/Spectroscopy_Simulation.ipynb): Is there really a line emission?
2. [Justification](https://nbviewer.jupyter.org/github/ysBach/SNU_AOclass/blob/master/Notebooks/Spectroscopy_in_Python.ipynb): Comparison of my personal notebook with IRAF results on Subaru FOCAS data
   * Adopted by [PyReduc project](https://keheintz.github.io/PyReduc/) ([github](https://github.com/keheintz/PyReduc)) as of 2020 Apr.
3. [SNUO 1m telescope](https://nbviewer.jupyter.org/github/ysBach/SNU_AOclass/blob/master/Notebooks/Spectroscopy_Example.ipynb): Spectrograph data from SNUO



#### Part <u>S</u>: Non-Python <u>S</u>oftwares or <u>S</u>ervices

* [S01_IRAF.md](Notebooks/S01_IRAF.md)
* [S02_Installing_Astrometry_dot_net.md](Notebooks/S02_Installing_Astrometry_dot_net.md)
* SExtractor (see notes in [references/](references/))

#### Part <u>A</u>: <u>A</u>ppendices

* [A02_TRIPOL.md](Notebooks/A02_TRIPOL.md)
* [A03_TRIPOLpy_Tutorial](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/A03_TRIPOLpy_Tutorial.ipynb)

* [A04_SNUO1Mpy_Tutorial](https://nbviewer.jupyter.org/github/ysbach/AO2019/blob/master/Notebooks/A04_SNUO1Mpy_Tutorial.ipynb)

-----

### 3-3. Homework Assignments

See [Assignments directory](Assignments/).

### 