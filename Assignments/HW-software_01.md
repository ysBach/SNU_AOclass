# HW (Softwares & Tools)

You may refer to 

* Lecture note [00-1. Softwares](https://github.com/ysBach/SNU_AOclass/blob/master/Notebooks/00-1_Softwares.md)
* Lecture presentation on Softwares.



## 1. Slack

2 points each

(I will check each one of your Slack accounts in our workspace)

1. Watch the videos below (yes|no)
   1. https://slack.com/#what-is-slack (2m 33s; retrieved 2020-04-14)
   2. https://slack.com/features#why-slack (1m 59s; retrieved 2020-04-14)
2. Join our workspace via [this link](https://join.slack.com/t/2020ao1/shared_invite/zt-d41p1yyo-3gLPwfpzSypMrCG1Flavdw).
   * **NOTE**: Refer to our lecture note [here](https://github.com/ysBach/SNU_AOclass/blob/master/Notebooks/00-1_Softwares.md#2-slack) and follow the section 2.1.
3. Change your name to your real name in English, profile picture to whatever you like.
4. Send a DM (private message) to me saying hello.
5. What are the differences between workspace and channels? (describe in about 1-2 lines)
   * **TIP**: see the lecture note linked above.



All important notices will be made via both Slack & ETL, but **all other notices will be made via Slack only.**





## 2. GitHub

2 points each.

(I will check whether you did these correctly by visiting your repo and looking at the commit histories)

1. Make a GitHub account. What's your ID?
2. Apply for GitHub student account at [here](https://education.github.com/pack). You will get the education pack soon (maybe it will take few days). Did you get the pack? (yes|no)
3. Make a test public repo by yourself using any name. Initialize with README. Make at least one commit by changing README.md or adding other files (see lecture presentation). What is the link to your repo?
   * Note: You must be able to see your commit at GitHub within 1 minute. If you cannot, check whether you did add/commit/push correctly. Search on google by yourselves to learn how to do these.
4. Clone your repo to your local workspace by ``$ git clone <repo_url>`` to the terminal (see lecture presentation PPT file)
5. Write ``*.txt`` to the top line of ``.gitignore`` file. Then add/commit/push ``.gitignore`` file.
   * Tip: ``.gitignore`` is a hidden file. You may have to tune the file explorer (finer for mac) option to see this file.
6. Make a fake file ``test2.txt`` (``$ touch test2.txt``) and do ``git status``. Can you see ``test2.txt``? (yes|no)
7. Open an issue at your test repo (you can put any content as you like). Then do ``git add`` anything, make a commit with message like "Fixes #1", and push. Is your issue closed? (yes|no)
   * I will visit your repo to check whether you correctly closed this issue.
   * In the future (when you "work"), you may learn fork, commit to the forked repo, and request a pull request (PR). The way you closed your first _issue_ is how you will do to close isseus.



## 3. SAO ds9, Astrometry.net

2 points each

1. Install the most recent version of SAO DS9 on your computer. (yes|no)
2. Follow the steps below:
   1. Download ``SNUO_STX16803-kw4-4-4-20190602-135247-R-60.0.fits`` and ``SNUO_STX16803-kw4-4-4-20190602-135247-R-60.0_bdfw.fits`` from our Tutorial data link (see [README](https://github.com/ysBach/SNU_AOclass)). 
   2. The first FITS file will not be used, but it is the file before what is called the preprocessing (bias subtraction, dark subtraction, and flat fielding).
   3. Open the second one with SAO ds9.
   4. Can you see the RA/DEC information? (yes|no)
3. Open the two FITS files you downloaded using SAO ds9. What differences can you find? List at least three of them (e.g., pixel values are different, visually different, etc). 
4. Actually, this WCS information is **wrong**, because I did 4x4 binning to reduce the file size after I obtained the WCS. Thus, we need to update this. Follow the steps below:
   1. Go to ``astrometry.net`` web service ([link](http://nova.astrometry.net/upload)). 
   2. Choose the file (the second FITS file, ``SNUO_STX16803-kw4-4-4-20190602-135247-R-60.0_bdfw.fits``)
   3. Click on ``Advanced Settings [+]``, set the followings
      * **Scale** → ``custom``, Units → "arcseconds per pixel", Lower bound: 1, Upper bound: 2
      * **CRPIX center**: check
   4. Click upload.
   5. After a success, go to results page and download the new FITS file. 
   6. Find the positions of USNO URAT 1 stars in the field of view by using SAO ds9's "Analysis-Catalogs-Optical-URAT1" (see the presentation file).
   7. Take a photo/screenshot of what you see and submit it.

If you have LINUX on your computer, you may try the offline version of the astrometry.net. This is many times essential for professional research. See the astrometry.net installation note in our lecture note contents ([link](https://github.com/ysBach/SNU_AOclass#3-seminar-contents)).



## 4. Python & conda

2 points each

I am assuming you have already downloaded/installed python (Anaconda recommended). If not, please refer to our lecture note [here](https://github.com/ysBach/SNU_AOclass/blob/master/Notebooks/00-1_Softwares.md#3-anaconda). **Be careful when you are setting PATH option**.

1. Turn on the terminal (Win10: Anaconda Prompt). Install astropy-related packages by the following command. See also section 5 of our lecture note [here](https://github.com/ysBach/SNU_AOclass/blob/master/Notebooks/00-1_Softwares.md#5-astropy-and-affiliated-packages). Could you finish the installation? (yes|no)
   ```
   $ conda install -c astropy ccdproc photutils astroscrappy aplpy
   ```
   
1. Open Jupyter notebook or IPython console (if you don't know what these are, google it). import each of the above packages and print the versions of them (e.g., ``import ccdproc`` and ``print(ccdproc.__version__)``).

1. While installing affiliated packages, what does ``-c`` mean (answer in one word)?

   - **TIP**: Search for ``conda install -c``.

4. If you do ``conda create -n``, what does it creat (answer in one word)?
   * **TIP**: Search for conda environment

