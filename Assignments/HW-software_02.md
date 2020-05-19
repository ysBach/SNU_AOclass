# HW (Softwares & Tools)

You may refer to 

* Lecture note [00-1. Softwares](https://github.com/ysBach/SNU_AOclass/blob/master/Notebooks/00-1_Softwares.md)
* Lecture presentation on Softwares.



## 1. Slack

Total 10 points

Open the DM(direct message) to yourself. Send messages to yourself (for testing purpose) following the items below. Do the followings, and **take screenshots or photos**.

(Slack syntax ≈ facebook/instagram + markdown)

1. Call yourself by ``@<yourname>``. 
2. Tag a channel by ``#notice``.
3. Use backquote(`` ` ``) to make an inline code (e.g., `` `print("Hello, world!")` ``). Your text should become a redish text with gray-boxed background.
4. For longer code, Use three backquotes (`` ``` ``), and a gray block will appear. Make a simple code block with a content as you wish. Use shift+Enter for newline.
5. Slack accepts many of markdown syntax. Write any message including bold (use ``*`` or ctrl+B), italic (use `_` or ctrl+I), and strikethrough (use `~` or ctrl+shift+X). Example: `` **bold**, _italic_, and ~strikethrough~``
   * TIP: In Slack, ``*bold*`` works. But in normal markdown, single asterisk means italic and only double asterisk means bold (sigh...).
6. Write any message using bullet list (use ``* content`` or ctrl+shift+8 and then use shift+enter), numbered list (use ``1. content`` or ctrl+shift+7 and then use shift+enter), and quotation (use ``> content`` or ctrl+shift+9 and then use shift+enter)
7. Write any message using emoji by colon(``:``). Example: ``:smirk::thumbsup:`` (use autocomplete!)
8. Write a message with, e.g., your github repo link (ctrl+shift+U)
9. Open a thread to any of the message you wrote to yourself (by replying to any of the message).
10. Add any reaction to any of the message.
11. Share any message to yourself (it cannot be exported since it's private message).



## 2. GitHub

2 points each

1. What is your github repo address again? (because I just want to click this from your answer sheet...)
2. I have visited all your repos and made at least one issue. Modify any file at your local workspace as you wish, commit with a message "Fixes #x" (x is the number of the issue I opened), and push to close the isse. (I did)
3. Edit your GitHub bio (profile) at ``https://github.com/<YourUserName>``. (I did)



## 3. Image

2 points each

You may have downloaded the FITS files from Software HW 01. Open any one of these.

1. Go to ``Frame`` → ``New Frame`` and then ``File`` → ``open`` to open the other file. Click ``Frame`` → ``Single Frame`` and ``Scale`` → ``ZScale``. (I did|I didn't)
2. Press tab key on your keyboard. Set to ZScale if this frame hasn't yet. (yes|no)
3. On one of the image, use your mouse wheel to zoom in/out, click mouse wheel button to move your center of view. Then press tab key. They are now mismatched with each other in the image frame. Go to ``Frame`` → ``Match`` → ``Frame`` → ``Image`` and hit tab keys. Are they spatially matched now? (yes|no)
   * In visually inspecting the data, you may also use ``Frame`` → ``Match`` → ``Scale``//``Scale and Limits``, but these are not useful in our case.
4. Play with Scales (``Scale`` → ``Linear``, ``Log``, ..., ``Histogram``) and Color. Select a scale and color combination of your favorite. Also choose your favorite style by tuning many options available from ``Color`` → ``Colarbar``. Select ``View`` → ``Horizontal Graph`` and ``Vertical Graph`` to show both graphs. (yes|no)
5. Display the file ``~~~~_bdfw.fits``. Select ``Edit`` → ``Region``, and ``Region`` → ``Shape`` → ``Circle``. Draw any circle near our object located roughly at (x, y) = (557, 504). Then click ``Region`` → ``Centroid``. The region should now be centered at the star you chose. If not, move the region slightly so that it centers near the true center of the star, and click ``Centroid`` again. Did it find the correct center? (yes|no)
   * This centroiding algorithm in DS9 is not robust, so it may change depending on the initial condition. Don't be too surprised if it changes when you click Centroid for many times...
6. Double click on the circle you drew, write ``Text`` you want to display, tune the ``Radius`` to ``5`` in the unit of  "**Image**" and click ``Apply``. Select your favorite style of this "region", by ``Color``, ``Width``, ``Property``, and ``Font``. Go to ``Analysis`` → ``Statistics``. From the new window, write down **sum** and **area(arcsec\*\*2)**, down to the precision of around 3 significant figures. These should be around 1.6e+5 and 7.6. This is the statistics of "target + sky".
7. Draw a region as in previous, but with ``Region`` → ``Shape`` → ``Annulus``. Make it centered at the same star. Double click it, set ``Inner`` and ``Outer`` of ``Radius`` to ``20`` and ``40`` in the unit of "Image", respectively. Click ``Generate`` and ``Apply``. Go to ``Analysis`` → ``Statistics`` and write down **surf_bri**, **mean**, **median**, and **stddev**, down to the precision of around 3 significant figures. These should be around 20000, 2000, 2000, and 10. This is the statistics of the "sky".
   * Crudely speaking, mean and median must be similar and it's nice if |mean - median| ≪ stddev. This is true in our case. Otherwise, we need to employ some empirical/mathematical tricks such as "MMM (mean-median-mode)" relationship, which we will learn later.
8. To see how the sky values are distributed, draw a circular region to the sky (where no visible object is there). Then ``Analysis`` → ``Histogram``. Does it look like Gaussian? (yes|no)
9. Draw an annulus as in previous problem and center it to the same star. Double click it. (If you cannot, you may remove the previous regions, or click them and do ``Region`` → ``Move to Back``) Set ``Inner`` and ``Outer`` of ``Radius`` to ``0`` and ``20`` in the unit of "Image", respectively. Set ``Annuli`` to ``20``. Click ``Generate`` and ``Apply``. Show the radial profile by ``Analysis`` → ``Radial profile``. The x-axis must be in arcseconds unit. Estimate FWHM. 
10. From the radial plot from previous problem: What is a rough estimate of sky value you find from this plot? Does this match with the ``surf_bri`` from previous problem?
11. Roughly calculate ``I = sum(circular region) - area(circular region)*surf_bri(annulus)`` and instrumental magnitude ``m_inst = -2.5 log_{10} (I)`` of your object. 
12. Congratulations! You have just finished your very first simple photometry in your life (yay|yes|hooray|oh|wow|~~no~~).

11. Do a similar calculation (calculate ``I`` and ``m_inst``) for any nearby star (you can choose any star, which (a) does not have any nearby star (b) not too faint, not too bright). What is a rough position in X, Y,  ``I``, and ``m_inst``?
12. Say that star has a catalogued magnitude ``m_0``. Using Pogson's formula, what is our target's magnitude in terms of ``m_0``?

