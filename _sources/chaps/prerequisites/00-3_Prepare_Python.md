(00:Prepare_Python)=

# (IMPORTANT) Python Environment

For this lecture notes, you need some packages to run the codes.

```{admonition} For Windows users
If you want to use Windows, you have to sacrifice ``fitsio`` (unfortunately, their installation assumes ``gcc``). Erase the installation of ``fitsio`` from the codes below.
```

If you are familiar with conda and virtual environment, please feel free to make a new env for this lecture note. If you don't understand what this means, please ignore it (you will natually know what it is after few years of using conda and having numerous headaches and googling experiences).

```{note}
If you are sick of the slow speed of ``conda`` and adventerous, give [``mamba``](https://github.com/mamba-org/mamba) a try.
```

## Installation Script

Copy and paste the following lines to the terminal (I am assuming you have anaconda installed, following [00-1_Softwares.md](00-1_Softwares.md)):

```
conda create -n snuao python=3.10 numpy=1.24 scipy=1.10 astropy=5.2 pandas=1 jupyter=1 sep=1.2 ccdproc=2.4 photutils=1.6 specutils=1.10 -y
conda activate snuao
conda install -c conda-forge fitsio -y  # Windows will raise error here; ignore this line if it does.
```

**This may take several minutes.** Be patient, grab a cup of coffee and read the "Reading Materials" section below.

***AFTER the above is finished***, install the submodules:

```
cd submodules/
cd version_information && pip install -e . && cd ..
cd astroquery && pip install -e . && cd ..
cd ginga && pip install -e . && cd ..
cd astroalign && pip install -e . && cd ..
cd astroscrappy && pip install -e . && cd ..
```
(basically any version of these may not break any part of the notebooks, hopefully...)

Finally

```
pip install astro-ndslice==0.2 ysfitsutilpy==0.2 ysphotutilpy==0.1 --no-deps
```

### Reading Materials

Somethings to read during the installation:

**Astropy**
: The name of a project which devotes its human power in developing a *single* package containing tools useful for astronomers in Python language([GitHub](https://github.com/astropy/astropy/wiki), [Official website](http://www.astropy.org/), [The most recent stable distribution documentation](http://docs.astropy.org/en/stable/)).

**Affilated Packages**
: Since astropy is a "single core" package, it doesn't have many convenience functionalities for small specific fields of astronomy. So there are some affiliated packages which helps astronomers to fulfill their needs. You may find the list if them [here](http://www.astropy.org/affiliated/).

```{note}
The astropy (but not affiliated packages) must have been installed on your computer by default while installing Anaconda.
```

Among the Astropy affiliated packages, these will be heavily used:

[photutils](http://photutils.readthedocs.io/en/stable/)
: Photometry related functionalities

[ccdproc](http://ccdproc.readthedocs.io/en/stable/)
: CCD data manipulation

[astroscrappy](https://github.com/astropy/astroscrappy)
: The cosmic ray rejection tool, which uses L.A.Cosmic algorithm ([van Dokkum 2001, PASP](http://www.astro.yale.edu/dokkum/lacosmic/)).

[APLPy](https://aplpy.github.io/)
: Astronomical image displaying tool (you *may* use it in the future...?).

[astroquery](https://astroquery.readthedocs.io/en/latest/)
: Querying astronomical catalog data - unlike most of other packages, it is recommended to use the "developer's version" of astroquery rather than stable version of it. This is why we install astroquery by ``git clone`` rather than ``conda install``.

[``fitsio``](https://github.com/esheldon/fitsio.git)
: The popular ``cfitsio`` in python.

```{note}
``fitsio`` is used (optionally) within ``ysfitsutilpy`` to boost the FITS I/O speed (factor of ~ 30x on macOS) when header is unnecessary.
```

## Check if Installed Correctly

Some packages has test module. Please run these to check if the installation worked correctly.

<details><summary>click</summary>
<p>
You can simply test the installation by tests. Run ipython or Jupyter notebook/lab, and type

``` python
>>> import astropy, photutils
>>> photutils.test()
>>> astropy.test()
```

These will take quite long time, especially astropy takes very long time. (So I didn't show you the full result)

You need to do it only once when you first installed these packages. If you want to test only some part of the whole package, you can specify the module, e.g., you can test `astropy.io.fits` by:

```python
>>> astropy.test(package='io.fits')
```

While the test is going on, look at the names of the directories, like `astropy/table`, `astropy/units`, etc. These are the names we will encounter very frequently, so this test is not only to **test**, but also to get accustomed to the astropy and python language.

Each dot(`.`) means `test passed` and `x` means `test failed`. But some of the failures are just OK. `s` means it is skipped for some reason.

An example test for **Astropy 1.3.1 and Photutils 0.3.1** (took ~ 10 mins):

```bash
(long long test explanations....)
======================== 1056 passed, 2 skipped, 2 xfailed in 82.18 seconds ========================
(long long test explanations....)
Some tests are known to fail when run from the IPython prompt; especially, but not limited to tests involving logging and warning handling.  Unless you are certain as to the cause of the failure, please check that the failure occurs outside IPython as well.  See http://docs.astropy.org/en/stable/known_issues.html#failing-logging-tests-when-running-the-tests-in-ipython for more information.
== 24 failed, 8717 passed, 75 skipped, 42 xfailed, 1 xpassed, 2 pytest-warnings in 573.02 seconds ==
```

The astropy will do the tests automatically (takes ~ 10 minutes). There might be some errors, but usually they are not important, so you can ignore them. If "`astropy.test()`" itself does not work, please check whether the installation of Anaconda had been done correctly.

</p>
</details>

## Troubleshoot

If you have any trouble installing the abovementioned packages, that's a big problem. Please immediately contact the TA or open an issue at this repo.
