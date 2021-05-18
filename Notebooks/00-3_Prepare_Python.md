# Prepare Python Environment

For this lecture notes, you need some packages to run the codes. 



> **For Windows Users**
>
> If you want to use Windows, you have to sacrifice ``fitsio`` (unfortunately, their installation assumes ``gcc``). Erase the installation of ``fitsio`` from the codes below. ``fitsio`` is used (optionally) within ``ysfitsutilpy`` to boost the FITS I/O speed (factor of ~ 30x on macOS), but for this undergraduate course, it may not impact your semester more than few minutes, hopefully.



## Installation Script

Copy and paste the following lines to the terminal (I am assuming you have anaconda installed):

```
conda install -c conda-forge numpy scipy astropy pandas jupyter sep -y
conda install -c astropy ccdproc photutils astroscrappy aplpy specutils
conda install -c conda-forge fitsio -y  # Windows will raise error here; ignore this line if it does.
```

**This may take several minutes.** Be patient and grab a cup of coffee.

Then git clone some repos:

```
cd <PathToGitClone> 
git clone https://github.com/jrjohansson/version_information.git && git clone https://github.com/astropy/astroquery.git && git clone https://github.com/ejeschke/ginga.git && git clone https://github.com/quatrope/astroalign && git clone https://github.com/ysBach/ysfitsutilpy.git && git clone https://github.com/ysBach/ysphotutilpy.git && git clone https://github.com/ysBach/ysvisutilpy.git
```



**AFTER the two processes above are finished**, install the git-cloned packages after git pull (you may use this for updating the packages afterwards)

```
cd version_information && pip install -e . && cd ..
cd astroquery && git pull && pip install -e . && cd ..
cd ginga && git pull && pip install -e . && cd .. 
cd astroalign && git pull && pip install -e . && cd .. 
cd ysfitsutilpy && git pull && pip install -e . && cd .. 
cd ysphotutilpy && git pull && pip install -e . && cd .. 
cd ysvisutilpy && git pull && pip install -e . && cd ..
```



## Check if Installed Correctly

Some packages has test module. Please run these to check if the installation worked correctly.

```
$ ipython
In [1]: import astropy
In [2]: astropy.test()
```

(If you don't see any error, it's fine.)



## Troubleshoot

If you have any trouble installing the abovementioned packages, that's a big problem. Please immediately contact the TA or open an issue at this repo.