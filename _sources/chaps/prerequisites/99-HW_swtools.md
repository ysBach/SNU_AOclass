(HW:swtools)=

# HW Software & Tools

## 1-1. Slack (1) [10 points]

(I will check each one of your Slack accounts in our workspace)

1. Watch the videos below (yes|no)
   1. <https://slack.com/#what-is-slack> (2m 33s; retrieved 2020-04-14)
   2. <https://slack.com/features#why-slack> (1m 59s; retrieved 2020-04-14)
2. Join our workspace (Ask TA for the invitation).
   * **NOTE**: Refer to our lecture note [Softwares](00:Softwares) and follow the section for slack.
3. Change your name to your real name in English, profile picture to whatever you like.
4. Send a DM (private message) to the TA saying hello.
5. What are the differences between **workspace** and **channels**? (describe in about 1-2 lines)
   * **TIP**: see the lecture note.

## 1-2. Slack (2) [10 points]

Open the DM(direct message) to yourself. Send messages to yourself (for testing purpose) following the items below. Do the followings, and **take screenshots or photos**.

(Slack syntax ≈ facebook/instagram + markdown)

1. Call yourself by ``@<yourname>``. Tag a channel by ``#notice``.
2. Use backquote(`` ` ``) to make an inline code (e.g., `` `print("Hello, world!")` ``). Your text should become a redish text with gray-boxed background.
3. For longer code, Use three backquotes (`` ``` ``), and a gray block will appear. Make a simple code block with a content as you wish. Use shift+Enter for newline.
4. Slack accepts many of markdown syntax. Write any message including bold (use ``*`` or ctrl+B), italic (use `_` or ctrl+I), and strikethrough (use `~` or ctrl+shift+X). Example: ``**bold**, _italic_, and ~strikethrough~``
   * TIP: In Slack, ``*bold*`` works. But in normal markdown, single asterisk means italic and only double asterisk means bold (sigh...).
5. Write any message using bullet list (use ``* content`` or ctrl+shift+8 and then use shift+enter), numbered list (use ``1. content`` or ctrl+shift+7 and then use shift+enter), and quotation (use ``> content`` or ctrl+shift+9 and then use shift+enter)
6. Write any message using emoji by colon(``:``). Example: ``:smirk::thumbsup:`` (use autocomplete!)
7. Write a message with, e.g., your github repo link (ctrl+shift+U)
8. Open a thread to any of the message you wrote to yourself (by replying to any of the message).
9. Add any reaction to any of the message.
10. Share any message to yourself (it cannot be exported since it's private message).

## 2-1. GitHub (1) [4 points]

1. What is a ``repo`` of GitHub?
   * **ANSWER**: repo = repository.
2. How can you download a github repo?
   * **TIP**: Search for ``git clone``.

## 2-2. GitHub (2 optional) [14 points]

```{dropdown} Skip this unless the TA asks you to solve these.

2 points each.
(I will check whether you did these correctly by visiting your repo and looking at the commit histories)

1. Make a GitHub account. What's your ID?
2. Apply for GitHub student account at [here](https://education.github.com/pack). You will get the education pack soon (maybe it will take few days). Did you get the pack? (answer: yes|no)
3. Make a test public repo by yourself using any name. Initialize with README. Make at least one commit by changing ``README.md`` or adding other files (see lecture presentation). What is the link to your repo?
   * Note: You must be able to see your commit at GitHub within 1 minute. If you cannot, check whether you did add/commit/push correctly. Search on google by yourselves to learn how to do these.
4. Clone your repo to your local workspace by ``$ git clone <repo_url>`` to the terminal (see lecture presentation PPT file)
5. Write ``*.txt`` to the top line of ``.gitignore`` file. Then add/commit/push ``.gitignore`` file.
   * Tip: ``.gitignore`` is a hidden file. You may have to tune the file explorer (finer for mac) option to see this file.
   * If you don't see the hidden file ``.gitignore``, it means you didn't select anything for "Add .gitignore" when you were making the repo. Do ``$ touch .gitignore`` on terminal to make the file.
6. Make a fake file ``test2.txt`` (``$ touch test2.txt``) and do ``git status``. Can you see ``test2.txt``? (answer: yes|no)
7. [Open an issue](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue) at your test repo (you can put any content as you like). Then modify any of the file in your local workspace. Do ``git add`` this file, make a commit with message like "Fixes #1", and push. Is your issue closed? (answer: yes|no)
   * I will visit your repo to check whether you correctly closed this issue.
   * In the future (when you "work"), you may learn fork, commit to the forked repo, and request a pull request (PR). The way you closed your first _issue_ is how you will do to close isseus.
```

## 2-3. GitHub (3 optional) [6 points]

```{dropdown} Skip this unless the TA asks you to solve these.
2 points each

1. What is your github repo address again? (because I just want to click this from your answer sheet...)
2. I have visited all your repos and made at least one issue. Modify any file at your local workspace as you wish, commit with a message "Fixes #x" (x is the number of the issue I opened), and push to close the isse. (answer: I did)
3. Edit your GitHub bio (profile) at ``https://github.com/<YourUserName>``. (answer: I did)
```

## 3. SAO ds9, ``Astrometry.net`` [8 points]

1. Install the most recent version of SAO DS9 on your computer. (answer: yes|no)
2. Follow the steps below:
   1. Download ``SNUO_STX16803-kw4-4-4-20190602-135247-R-60.0.fits`` and ``SNUO_STX16803-kw4-4-4-20190602-135247-R-60.0_bdfw.fits`` from our Tutorial data link (see [README](https://github.com/ysBach/SNU_AOclass)).
   2. The first FITS file will not be used, but it is the file before what is called the preprocessing (bias subtraction, dark subtraction, and flat fielding).
   3. Open the second one with SAO ds9.
   4. Can you see the RA/DEC information? (answer: yes|no)
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

If you have LINUX on your computer, you may try the offline version of the astrometry.net. This is many times essential for professional research. On mac, you can use [``brew``](https://formulae.brew.sh/formula/astrometry-net). (TO BE UPDATED 2023-04-06. If this is not updated, please let me know --- I must have forgotten.)

## 4. Python & conda [8 points]

2 points each

I am assuming you have already downloaded/installed python (Anaconda recommended).

1. Turn on the terminal (or Anaconda Prompt for Windows users). Install astropy-related packages by the following command. See also section 5 of our lecture note [Softwares](00:Softwares). Could you finish the installation? (yes|no)

1. Open Jupyter notebook or IPython console (if you don't know what these are, google it). Then import each of the above packages and print the versions of them (e.g., ``import ccdproc`` and ``print(ccdproc.__version__)``).

1. While installing affiliated packages, what does ``-c`` mean? Answer in one word.
   * **TIP**: Search for ``conda install -c`` on web.

4. If you do ``conda create -n``, what does it creat? Answer in one word.
   * **TIP**: Search for "conda environment" on web.

```{admonition} Deprecated homework problems regarding IRAF
:class: dropdown
1. Why did I use ``conda config --set channel_priority false`` when installing IRAF?
   - **TIP**: Search for conda channels and channel priority.
2. How can you make a new environment via Anaconda? (what is an environment for?)
   - **TIP**: Search for ``conda create -n``. You used it when you are installing IRAF.
```

## 5. Interactive Image Analysis [28 points]

2 points each

You may have downloaded the FITS files from **SAO ds9** part.

First, open any one of these. Then:

1. Go to ``Frame`` → ``New Frame`` and then ``File`` → ``open`` to open the other file. Click ``Frame`` → ``Single Frame`` and ``Scale`` → ``ZScale``. (answer: I did|I didn't)
2. Press tab key on your keyboard. Set to ZScale if this frame hasn't yet. (answer: yes|no)
3. On one of the image, use your mouse wheel to zoom in/out, click mouse wheel button to move your center of view. Then press tab key. They are now mismatched with each other in the image frame. Go to ``Frame`` → ``Match`` → ``Frame`` → ``Image`` and hit tab keys. Are they spatially matched now? (answer: yes|no)
   * When visually inspecting the data, you may also use ``Frame`` → ``Match`` → ``Scale``//``Scale and Limits``, but these are not useful in our case.
4. Play with Scales (``Scale`` → ``Linear``, ``Log``, ..., ``Histogram``) and Color. Select a scale and color combination of your favorite. Also choose your favorite style by tuning many options available from ``Color`` → ``Colarbar``. Select ``View`` → ``Horizontal Graph`` and ``Vertical Graph`` to show both graphs. (answer: yes|no)
5. Display the file ``~~~~_bdfw.fits``. Select ``Edit`` → ``Region``, and ``Region`` → ``Shape`` → ``Circle``. Draw any circle near our object located roughly at (x, y) = (557, 504). Then click ``Region`` → ``Centroid``. The region should now be centered at the star you chose. If not, move the region slightly so that it centers near the true center of the star, and click ``Centroid`` again. Did it find the correct center? (answer: yes|no)
   * This centroiding algorithm in DS9 is not robust, so it may change depending on the initial condition. Don't be too surprised if it changes when you click Centroid for many times...
6. Double click on the circle you drew, write ``Text`` you want to display, tune the ``Radius`` to ``5`` in the unit of  "**Image**" and click ``Apply``. Select your favorite style of this "region", by ``Color``, ``Width``, ``Property``, and ``Font``. Go to ``Analysis`` → ``Statistics``. From the new window, write down **sum** and **area(arcsec\*\*2)**, down to the precision of around 3 significant figures. These should be around 1.6e+5 and 7.6. This is the statistics of "target + sky".
7. Draw a region as in previous, but with ``Region`` → ``Shape`` → ``Annulus``. Make it centered at the same star. Double click it, set ``Inner`` and ``Outer`` of ``Radius`` to ``20`` and ``40`` in the unit of "Image", respectively. Click ``Generate`` and ``Apply``. Go to ``Analysis`` → ``Statistics`` and write down **surf_bri**, **mean**, **median**, and **stddev**, down to the precision of around 3 significant figures. These should be around 20000, 2000, 2000, and 10. This is the statistics of the "sky".
   * Crudely speaking, mean and median must be similar and it's nice if |mean - median| ≪ stddev. This is true in our case. Otherwise, we need to employ some empirical/mathematical tricks such as "MMM (mean-median-mode)" relationship, which we will learn later.
8. To see how the sky values are distributed, draw a circular region to the sky (where no visible object is there). Then ``Analysis`` → ``Histogram``. Does it look like Gaussian? (answer: yes|no)
9. Draw an annulus as in previous problem and center it to the same star. Double click it. (If you cannot, you may remove the previous regions, or click them and do ``Region`` → ``Move to Back``) Set ``Inner`` and ``Outer`` of ``Radius`` to ``0`` and ``20`` in the unit of "Image", respectively. Set ``Annuli`` to ``20``. Click ``Generate`` and ``Apply``. Show the radial profile by ``Analysis`` → ``Radial profile``. The x-axis must be in arcseconds unit. Estimate FWHM.
10. From the radial plot from previous problem: What is a rough estimate of sky value you find from this plot? Does this match with the ``surf_bri`` from previous problem?
11. Roughly calculate ``I = sum(circular region) - area(circular region)*surf_bri(annulus)`` and instrumental magnitude ``m_inst = -2.5 log_{10} (I)`` of your object.
12. Congratulations! You have just finished your very first simple photometry in your life (answer: yay|yes|hooray|oh|wow|~~no~~).

11. Do a similar calculation (calculate ``I`` and ``m_inst``) for any nearby star (you can choose any star, which (a) does not have any nearby star (b) not too faint, not too bright). What is a rough position in X, Y,  ``I``, and ``m_inst``?
12. Say that star has a catalogued magnitude ``m_0``. Using Pogson's formula, what is our target's magnitude in terms of ``m_0``?
