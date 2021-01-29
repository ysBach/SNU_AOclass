# Software Installations

In this chapter, we will **install** the necessary apps/softwares/packages that we will use throughout this course. It includes:

* **Git** and **Slack**
* **Anaconda**: including most of necessary packages, e.g., **Astropy**
* **Astroconda**: IRAF-included; *optional*
* IDE/Editors: **Spyder**, Microsoft Visual Studio Code (**MS VS Code**); *optional*
 * **Image Displayer**
    * SAO ds9
    * ginga; *optional*

The installation may take some time. If you have nothing to do, read the next section while the installation is going on.

* If I say **terminal**, please understand it as terminal of UNIX or Git Bash of Windows. You'll learn how to install Git Bash in the next section if you are a Windows user.



[TOC]

## 1. Git and GitHub

1. Go to [GitHub](http://github.com/) and make your own ID. 
   * The ID might be used in your future Resume (CV; 이력서).

2. Go to [Git website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to download git for your OS. 
   * The ``Git Bash`` will be installed on your Windows, and it allows Windows users to use simple UNIX commands on Windows computer too. 
   * Git Bash is better than Anaconda Prompt, which will be installed if you install Anaconda.



Excerpt from [StackOverflow](https://stackoverflow.com/questions/13321556/difference-between-git-and-github):

>**Git** is a revision control system, a tool to manage your source code history.
>
>**GitHub** is a hosting service for Git repositories.
>
>So they are not the same thing: **Git** is the **tool**, **GitHub** is the **service for projects that use Git**.
>
>To get your code to GitHub, [have a look here](https://help.github.com/articles/create-a-repo/).



**Useful Web Tutorials**: https://36-750.github.io/tools/version-control/

**Useful Video tutorials**

* Nicolas: 
* [코딩 1시간만에 배우기 - 파이썬 (ft. 실리콘밸리 엔지니어) (Korean)](https://www.youtube.com/watch?v=M6kQTpIqpLs)
* 얄팍한 코딩사전 (Korean; [channel](https://www.yalco.kr/26_git_tutorial_2/)):
  1. [Git은 뭐고 Github은 뭔가요?](https://youtu.be/Bd35Ze7-dIw)
  2. [가장 쉬운 Git 강좌 - (상) 혼자작업편](https://www.youtube.com/watch?v=FXDjmsiv8fI&ab_channel=얄팍한코딩사전) 
  3. [가장 쉬운 Git 강좌 - (하) Github편](https://www.youtube.com/watch?v=GaKjTjwcKQo&ab_channel=%EC%96%84%ED%8C%8D%ED%95%9C%EC%BD%94%EB%94%A9%EC%82%AC%EC%A0%84)



## 2. Slack

Some useful links:

* [Official slack](https://slack.com/): log in and see what workspaces you are in.
* [Wikipedia](https://en.wikipedia.org/wiki/Slack_(software))
* [A random blog explaining Slack](http://blog.naver.com/hivearena/220377857149) (Korean)



### 2.1. How to Join Slack Workspace

1. TA will announce the "**invitation link**" to you.

2. Type your email and name.

   * **Please use your real name in English** (e.g., `Yoonsoo`); name is changable in the future

   * You will use that email/pw for your future access to **this** workspace. 
   * I encourage you to **download & install the app** at the [downloads page](https://slack.com/downloads/). 
     * Slack is usable on LINUX, Mac, Windows, Android phone, iPhone, etc.
     * So I suggest you to **install it both on your PC and phone**.
     * When login with your second device, put the workspace id (e.g., `2020AO1`) and use the email/pw you enrolled with your first device.



### 2.2. Terms

The following analogy works:

| Slack concept | Similar concepts                                   | Examples                         |
| ------------- | -------------------------------------------------- | -------------------------------- |
| **workspace** | A course in ETL, a website (모임, 그룹)            | `2018AO1`, `2019AO2`, `2020AO1`  |
| **channels**  | boards in such group or website (게시판, 채팅채널) | `team_hrdiagram`, `announcement` |



### 2.3. Why We Chose Slack

Slack is a software to make co-work easier; basically a "chatting app". We chose this for our communication platform because

1. It is **OS-independent**: Windows, mac, Linux, iOS, Android, Windows Phone, etc all can use slack without much difference. It works perfectly even on web-browsers.
2. Supports channels (public, closed, private)
3. It is widely used among company, labs, researchers, developers, ... . It might be helpful for your future to get used to this widely used software as early as possible when you are allowed to make mistakes.
4. Codes can be inserted (shown) cleanly than any other platforms (Kakaotalk, Line, Facebook, ...).
5. Can be integrated with, e.g., github, Dropbox, and Google Drive.
6. All content inside Slack is searchable, including files, conversations, and people.

Especially, 1, 4 and 5 are the main reasons we dropped Kakao-talk or the likes which we've used for years.



### 2.4. Tips for Slack

![](figs/slack.png)

In our workspace, ``2020ao1.slack.com``, you can see the left side bar:

* At the top, you can see the workspace name and your ID. Click it and set your profile from the drop down menu.


* ``All Threads``: to see "threads", which you will learn as time goes.
* ``Channels``: "boards" or "chatting channel" (게시판; 채팅채널)
* ``Direct Messages``: You may click a person's ID and send private messages.
* ``Invite People``: You will see what it means after clicking it.
* ``Apps``: Slack has powerful "integration" with third party apps such as Google Drive and Github. You can add your own github repo and make it to send summary message to your group's channel so that everyone can share information about the updates easily.

You will mostly use the channels which will be made based on your group topics (e.g., ``#active_comet``, ``#GRB``, ``#satellites``).

Messaging is similar to Facebook or Instagram system + markdown.

* Use "@" to call (tag) a person, such as "@Yoonsoo"

* Use "#" to tag a channel

* Markdown:

  * **Bold**: Embrace with asterisk (*)

  * *Italic*:  Embrace with underscore (_)

  * ~~Strike~~:  Embrace with tilde (~)

  * `short code`: Embrace with one single back quote (`)

  * For long codes or [preformatted](https://www.thoughtco.com/preformatted-text-3468275), embrace with three back quotes (```):

    ```
     This is a
         preformatted
       line
    ```

* You may also use Emoji by typing `+:emoji_name:` or `ctrl+shift+\`.

* You can add file directly (drag and drop). If it's a code or plane text, slack will show a snippet (short excerpt). 

  * If you hover on it, you can see some buttons to "react" like facebook, "comment", "share file", etc.



## 3. Anaconda

All the IRAF/Astropy packages, as well as usual python packages, will be downloaded via a platform called [**Anaconda**](https://www.continuum.io/downloads).


* **TIP**: If you are running out of space and really want very small essential package, try **miniconda**.

**I recommend to use Anaconda3 and use Python 3.6+**. 

> The support for Python 2 will be ceased soon. See, e.g., [PEP373](https://www.python.org/dev/peps/pep-0373/), [Python3Statement](http://www.python3statement.org/). [python clock](https://pythonclock.org/) was made  by Guido (The inventor of Python). All the ``astropy`` and its affiliated packages, ``matplotlib``, and many more which you are familiar with, will not support Python 2 after 2019.
>
> For useful things in Python 3 compared to 2, see [Python 3 for scientists](https://python-3-for-scientists.readthedocs.io/en/latest/python3_user_features.html).

When the download is done, install Anaconda following the website's instruction.

* **IMPORTANT**: If you use **Windows**, you will see a list of checkboxes while installing. For the checkbox related to ``PATH``, you should **CHECK it**. If you haven't, I have no other solution but re-install anaconda.

* **IMPORTANT**: If you are installing it on **terminal**, answer the questions like "add to PATH" with `yes`.



## 4. IRAF/PyRAF (*optional*)

<details><summary>click</summary>
<p>
**IRAF/PyRAF works only on UNIX, and you cannot run it correctly on Windows.**

There have been a lot of different ways to install IRAF: First people had to download with a lot of commands including "`cd ..`", "`wget blahblah`", etc. Then STScI developed a huge pack of all necessary softwares, named **Ureka**. But using *Ureka is deprecated* since April 2016. Now we use [**AstroConda**](http://astroconda.readthedocs.io/en/latest/installation.html). There are reasons for these transformations, and you may be able to find the reasons as time goes, if you are interested.

In terminal, type the followings (This may take **tens of minutes** depending on the Internet connections!)

    conda config --add channels http://ssb.stsci.edu/astroconda
    conda config --set channel_priority false
    conda create -n iraf python=2.7 iraf-all pyraf-all stsci

The name of the environment, ``iraf``, is ``iraf27`` in the original official website, but I just prefer ``iraf`` because it's shorter. You can set it as any name you like.

</p>
</details>



## 5. Astropy and Affiliated Packages

### 5.1. Installation

* **Astropy**: the name of a project which devotes its human power in developing a *single* package containing tools useful for astronomers in Python language([GitHub](https://github.com/astropy/astropy/wiki), [Official website](http://www.astropy.org/), [The most recent stable distribution documentation](http://docs.astropy.org/en/stable/)).  
* Affilated Packages: Since astropy is a "single core" package, it doesn't have many convenience functionalities for small specific fields of astronomy. So there are some affiliated packages which helps astronomers to fulfill their needs. You may find the list if them [here](http://www.astropy.org/affiliated/). 
* **TIP**: The astropy (but not affiliated packages) must have been installed on your computer by default while installing Anaconda.



Among these affiliated packages, I recommend you to download:

* [photutils](http://photutils.readthedocs.io/en/stable/): Photometry related functionalities
* [ccdproc](http://ccdproc.readthedocs.io/en/stable/): CCD data manipulation
* [astroscrappy](https://github.com/astropy/astroscrappy): cosmic ray rejection tool
* [APLPy](https://aplpy.github.io/): Astronomical image displaying tool
* [astroquery](https://astroquery.readthedocs.io/en/latest/): Querying astronomical catalog data

To download, type

    conda install -c astropy photutils ccdproc astroscrappy aplpy

For astroquery, it is recommended to download the most recent one:

```
$ cd <your_github_download_directory>
$ git clone https://github.com/astropy/astroquery.git
$ cd astroquery
$ python setup.py install
```



### 5.2. Testing Packages

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

## 6. Editors

There are bunch of different editors (including IDEs = Integrated Development Environment) to edit the codes. I personally use spyder (it is installed from Anaconda by default, and you can use it by running `spyder` or type `spyder &` on the terminal). 

Some may prefer **Wing** IDE, which is widely being used in educational institutions, or **PyDev**, **PyCharm**, and even **VI** (vim) or **Emacs**. VI is quite powerful since it is accessible for virtually all of the computers around the world by default, and the debugger, gdb, is also accessible on terminal. If you have an IDE, it most likely contain its own fancy debugger, too. For Windows computers, **Visual Studio** are also good. For Ubuntu, **gedit** or **geany** are also attractable choices. 

For *cross-platform*, there are **Sublime Text 3** and **Atom** which have been popular. Recently Microsoft released **Visual Studio Code**, which I now intensively use. 

I use geany for miscellaneous and short works because it is extremely light. Then spyder is used for interactive work, and VS Code for package managing and non-python language coding.

I have tried all the aforementioned editors, and settled down to the lightest, fastest, most intuitive/interactive, and yet functional editors after ~ 2 years of trial and error. BUT this is just my personal opinion, and you may find very different solution. I have many friends who use VI only for all the coding works. If you can, I recommend to use VI as your main/sub editor, or at least learn how to use it. I don't use VI just because for me it is too difficult to use it.

### 6.1. Spyder

Spyder has many important and useful functionalities. Because it uses IPython console as its default, it is very convenient to use it as editor and as terminal at the same time. 

#### 6.1.1. Shortcuts

Go to Tools -> Preferences (`Ctrl+Alt+Shift+P` on Ubuntu). "Keyboard shortcuts" list all the useful shortcuts. On Ubuntu, followings are the most important and useful ones:

* `F9`: run the line
* `ctrl+1`, `ctrl+4`: make comment or comment block. Test it by yourself to see it.
* `ctrl+5`: Remove the comment block
* `#%%`: (It's not a shortcut) Makes the "cell". Use it like this:  
    ```python
    #%%
    # Cell 1
    import numpy as np

    #%%
    # Cell 2
    print(np.ones(10))
    ```
* `ctrl+enter`: Run the cell, remaining at the cell. 
* `shift+enter`: Run the cell, Proceed to the next cell.
* `ctrl+shift+E`: Change the focus to "editor" window
* `ctrl+shift+I`: Change the focus to "IPython console" window

#### 6.1.2. Useful Settings

It is better to let `matplotlib` plotting window to pop-up (than showing the figure in-line). Go to the Preferences --> IPython Console --> Graphics. Set Graphics backend to "Automatic". Turn Spyder off and turn it on again. You will now see a new window pops up when you plot anything, e.g.,

```python
import maptlotlib.pyplot as plt
plt.plot([0,1], [1,1])    
```


## 7. Image Displayer
In astronomical image reduction process, you need some tools to display images on computer screen to interactively investigate the images. There is a *historical standard*, which is kind of an *affiliated package of IRAF*, [SAO ds9](http://ds9.si.edu/site/Download.html). The most recent version as of Mar 2018 is ver 7.5. I am currently using ver 7.6 beta. Some people use [Maxim DL](http://diffractionlimited.com/product/maxim-dl/), but it's commercial. In the future, as Python gets more and more attention, Ginga will be another powerful option. I am not sure when Ginga will become quite *perfect*, but until then, I recommend you to use both of them. Their pros and cons will be explained from now.

### 7.1. SAO ds9

Many useful documentations and YouTube videos: [SAOImageDS9 - Documentation (google.com)](https://sites.google.com/cfa.harvard.edu/saoimageds9/documentation?authuser=0) (retrieved 2021-01-29)

* Among them, a useful DS9 tutorial lecture note by [George J. Bendo (ver. 2020-06-26 as of 2021-01-29)](http://www.jb.man.ac.uk/~gbendo/Sci/Pict/DS9guide.pdf)
* For CIAO tutorials, you need to install CIAO environment from conda -- not recommended if you don't understand what it means.

SAO ds9 was made for Chandra X-ray observation, but became so powerful that it has been used for decades by virtually all astronomers.  It has many powerful features, and for me it's more convenient than ginga. By the system default, you will use ds9 to open any FITS image.

If you want to run ds9, you can do `ds9 &` on terminal. Once you've got used to ds9, you can do a bit advanced command such as 

    ds9 -zscale image01.fits image02.fits image03.fits -single &

or 

    ds9 -zscale image*.fits -single &. 

For more command line options, see [this link](http://ds9.si.edu/doc/ref/command.html).

If you want to turn ds9 on IRAF console, put exclamation mark (!):

    ecl> !ds9 &
and `!ds9 image*.fits -single &`, etc, will work identically. There is another task called DISPLAY in IRAF. Type `epar display` to see the parameters. Some frequently used commands are the zscale command, e.g., `displ image*.fits z1=100 z2=3000`. But be careful since DISPLAY shows different pixel values than actual value: See [here](http://iraf.net/forum/viewtopic.php?showtopic=1469817).




### 7.2. Ginga: Astropy Affiliated
[Ginga](https://ginga.readthedocs.io/en/latest/) (pronounced *ging-ga*, which means galaxy in Japanese; the reason for the name is explained in the link) is an affiliated package of astropy, and is used for FITS image viewer. If you do not want ginga, please refer to SAO ds9 in later section.

If you want to download it, type

    $ conda install -c astropy ginga

It is made to serve the role as SAO ds9, but to perform some useful calculations that ds9 cannot do by default. ds9 has tremendous power when it is used *with* IRAF, but that is not a favorable solution for Python users. So Ginga is made to fully funtional with Python only, as well as to be able to interact with IRAF as ds9 does.

You can use `$ ginga &` on terminal or `ecl> !ginga &` on IRAF console. Although you can do `ginga image.fits &` as you did for ds9, it is usually better to use interactive drag-and-drop way to open image than command line. In `ginga`, you can also use `Operation -> utils -> FBrowser`.

The most important feature of `ginga` is to use it for interactive FWHM estimation and radial profile check, which is done by ``pick``: [documentation](https://ginga.readthedocs.io/en/latest/manual/plugins_local/pick.html?highlight=pick).

I couldn't find how to use Ginga with IRAF yet.... Though [this official site](http://ginga.readthedocs.io/en/latest/manual/plugins_global/iraf.html) says you can. I think this is a [known bug](https://trello.com/c/6mt7oBXZ/44-iraf-plugin-implemented) that you actually cannot.


