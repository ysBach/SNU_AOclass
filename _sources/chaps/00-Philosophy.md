Made by Yoonsoo P. Bach

* Ver 1.0: 2017 Feb
* Ver 1.1: 2017 Sep
* Ver 2.0: 2018 Mar
* Ver 2.1: 2020 Sep (add "A Note")


```{contents}
```

# Philosophy

All the lecture materials were first made for "**Astronomical Observation**" (AO hereafter) of the Dept. of Astronomy of Seoul National University in 2017. Then gradually updated as time went.

* Lecturer: Prof. Masateru Ishiguro
* TA: Yoonsoo P. Bach


This preface contains some comments to explain ground philosophy while making the lecture notes and the reason for transforming from previous IRAF/IDL-based AO system to Python3-based system.


## A Note

I was lucky to have opportunities to serve as a TA at the AO class at SNU for years. In 2016, I found the system in IRAF and IDL prevailing in astronomy will only hinder our development and lead our academic society to a future dependent to commercial companies; later I also noticed a possibility of legal issues*. IRAF is a large blackbox, which indeed does not work as it is described in the manual or we'd expect (from image combination and aperture photometry to the PyRAF problem**). People have been using it just because there was no alternative, and these hidden bugs do not give error much larger than our expected precision; but we've got to regret we didn't have systematic "testing modules" and just assumed it works correctly.

I have tried my best to discard all pieces of IDL and most of IRAF, and replace all to python. These are the skeletons for photometry/polarimetry tools I developed for my observational research†.

\* See 2.1.3 below. Also P01 in ppt mentions this.

\*\* If you are using PyRAF (nothing but a IRAF wrapper in python), I urge you to check if it REALLY does the calculation you intended. Many times, it does not update the internal parameters. Worse, it does not raise any warning or error, and pretend as if it did everything correctly. I had to abandon all of my research outputs in 2016 after I found PyRAF does not even do aperture photometry correctly. (Many are confused, so a note: PyRAF is not astropy)

† SNUO1Mpy; TRIPOLpy; NICpolpy; Bach, Ishiguro, Jin et al. 2019 (4179 Toutatis, JKAS); Takahashi+2020 (submitted); Pravec et al. (1999 KW4, in prep), Ishiguro, Bach, Jin et al. (2005 UD, in prep); Bach, Ishiguro et al. (Vesta and Ceres, in prep), Craig, McCully, Conseil, Bach (astropy Image-combination in ccdproc); Geem, Ishiguro et al. (1984QY1+, in prep); Heintz and Finbo ([PyReduc](https://keheintz.github.io/PyReduc/))


## Choosing Software and Programming Language

### Problems of IRAF
For decades, IRAF of NOAO has become a virtual standard of astronomical image reduction process. As any other tools, it also have had some problems, and I want to point out three of them.

1. No human power to develop or maintain IRAF
2. IRAF has some problems since it's an "old" software
3. IRAF has some license issue and thus documentation issue happened in the summer of 2019.
4. Major new facilities in the near future will not use IRAF/IDL

The last one will be explained later, since it includes IDL too.

#### Human Power Issues

The most important problem is that “required” updates of IRAF may not be there after version 2.16.1, at least officially, and **STScI is now decreasing human power to IRAF development / maintenance**.

IRAF and its core SPP/CL are designed purely for IRAF society. There is virtually no computer scientists, programmers, and even no astronomers, who have interest in developing new codes using SPP now. You may not even have heard about the name SPP before. In other words, we cannot hope IRAF to be fixed / updated even if there are serious / unexpected bugs or problems. Few such problems are actually there, and some are documented by STScI (go to a doc page of some IRAF task, e.g., [``IMEXAMINE``](http://stsdas.stsci.edu/cgi-bin/gethelp.cgi?imexamine): you can see section called ``BUGS``). Some bugs include inaccurate aperture sum or wrong pixel value display if you use ``DISPLAY``.

Even though such serious problems may be alleviated in the future, it is almost hopeless to “optimize” IRAF. There are a plethora of different ideas and algorithms to make computation faster, and are still being studied by frontier computer scientists, yet they may not be implemented to IRAF.

This is critical, considering one single astronomical image is now becoming size of giga-bytes. My favorite example is [L.A. Cosmic](http://www.astro.yale.edu/dokkum/lacosmic/), which is a tool for removing cosmic-rays from astronomical images. We have both IRAF and Python versions (Python versions from `astroscrappy` actually uses C++, though it is fully usable on Python), and the Python version is order of magnitude faster than that of IRAF version. It can be up to ~100+ times faster, not only because it works efficiently, but also because IRAF does not support efficient parallel computing by default. One of my colleagues had to spend ~ 0.5 day for doing L.A.Cosmic to all her FITS data. IF there was anything wrong with the results, you have to spend 0.5 day again. The amount of data we have to analyze increases exponentially over time. LSST, which will survey all-sky with a depth of Subaru, or JWST, which is next-generation-HST, decided to use Python 3 and C++ against IRAF/IDL (see below)



#### IRAF is Old

Second problem of IRAF is because it is an **old** software, i.e., a problem that any other programs may have if they were developed decades ago, and it include:

* Works only on 32-bit environment
   * So we need some trick to run IRAF on modern-standard, 64-bit, computers.
   * This treatment is required almost only for IRAF. Almost none of modern softwares require 32-bit environment.
* Works only on UNIX-based OS
   * It is bothersome for majority of Windows computer users to have redundant LINUX computer for IRAF purpose, unless MS fully supports UNIX-like environment.
* CL has no debug functionality, so it is bad for large programming.
 * Each observatory needs its own software for data reduction. SPP and CL are not good for such purpose.
 * Actually, many different observatories makes their own routines with IDL, not IRAF/SPP/CL, and distribute it to the observers.



#### License and Documentation Problems

IRAF seems to have a copyright problem which can be sensitive to mention; I hesitate to even mentioning it. If you are interested, you may search for [iraf-community distribution](https://iraf-community.github.io/) (which became public to open source community thanks to the years of hard work of Dr. Streicher). I heard from third persons that this may have been one of the reasons why NASA and STScI started to hide IRAF from the main pages and tried to erase many traces of it. You may remember STScI's removal of IRAF documentation hosting in the summer of 2019 (I harshly blamed it as an irresponsible vandalism action in science done by an institution which once urged scientists to use IRAF).



### PyRAF and Its Problems
PyRAF is an alternative, made of Python, to avoid those problems of IRAF, especially to alleviate the complexity / debugging problem of SPP/CL:

> Excerpt from [STScI](http://www.stsci.edu/institute/software_hardware/pyraf/stsci_python):
>
> PyRAF is a command language for running IRAF tasks that is based on the Python scripting language.

According to this [Link](http://iraf.net/forum/viewtopic.php?showtopic=97713&lastpost=true), the attempt to replace CL by Python was ongoing in 1999. [This report](https://arxiv.org/abs/1610.03159) (arXiv 1610.03159) says such attempt for using Python started in 1998. Before 2000, when PyRAF was first being made, IRAF was not even a free software, so using totally-free Python is a very attractive trial. PyRAF works on Windows, too, though has many problems, since some functionalities are designed only for UNIX system *from the beginning*, and it is also clearly noted by STScI.

This PyRAF has some serious problems. First of all, **identical CL script gives different results in PyRAF for some cases**. This is implicitly explained in [PyRAF Tutorial](http://stsdas.stsci.edu/pyraf/doc.old/pyraf_tutorial/PythonPrereq.html), too: *"You can even run more than 90% of IRAF CL scripts!" (in PyRAF)*. In different perspective, it means ~ 10% of CL scripts does not work identically compared to that of IRAF. I have such experience for photometry and I had to do all the things again from the scratch. So if you have CL scripts you made when you were using IRAF, you wouldn't want to take risks of using PyRAF. You don't know which part will give different result from the original IRAF! No warning system of indicating the difference between IRAF and PyRAF is developed, so you have to run the script on IRAF and check whether it works correctly on PyRAF, which is just bothersome and inefficient.

Other than that, PyRAF was written in Python 2, and unlike many other Python packages, it has small amount of manual, which makes it difficult to start and use efficiently. You wouldn't want to move to PyRAF, which doesn't seem to be *much* better than IRAF CL scripting. One of the important issues of PyRAF is the same as that of IRAF: **No big update will be made in the near future**, though we have many known bugs. It is difficult to manually check how much budget and human resources are being used for PyRAF, but you can compare the frequency of update of PyRAF and Astropy. Although PyRAF is being updated with certain period, we are not sure how long will it be maintained. Lim Pey-Lian, at Science Software Branch of STScI, replied to my question about PyRAF via the official help email account that :

> "We are phasing out our IRAF support. Could you please try out photutils, a Python replacement for photometry tasks ..."

### IDL and Its Problems
These are logical reasons why many people seek for IRAF-alternatives. **One of such solutions is IDL**. Easier scripting, OS-independent, and the fact that is maintained by software experts made astronomers relieved and rely on this software. However, IDL also has some problems: The most important one is the **license issue**, and secondly the problem as a programming language (see [here](https://en.wikipedia.org/wiki/IDL_(programming_language)#Problems)). Also it is slow in plotting graphs, especially 3-D plotting. Another important issue is that it is used by very minor groups of people, astronomy and bio-imaging, so there is not many structured manuals we can access: same as IRAF!

License is very critical for users, not only because its price (SNU has spent budget for IDL license comparable to that used for rebuilding telescope at Building 45), but because you have to purchase license at **each time** when there is an update. You cannot use IDL 8.1 even if you have license of IDL 8.0. Institutions will be burdened with this, since many researchers should use the software, and the amount of required budget will go up almost linearly. If the institution does not support lisence fee, the compatibility problem arises: Say you have source code written in IDL 8, but the institution has license of IDL 7 only. Nevertheless, it is widely being used at observatories and institutions, due to its convenience for scripting compared to IRAF.

In July 2017, there has been a big happening at SNU: IDL License policy changed and thus all the PCs of students and professors could not use IDL for few days (IDL license needs the Internet connection, and the company shutdown the older license without properly noticing it). More seriously, the updated license has a policy that it does not allow more than 100 tabs. I said, tabs, not computers. So if 10 users are using the SNU license and turned on 10 tabs each, no more person can use IDL. This is the weakest point of all commercial softwares. Especially if it is a programming language, it is a disaster.

Same thing happens almost every 2-3 months since then (added 2018 March).

### Examples of IRAF and IDL Usage

* NASA IRTF: You will get IDL source codes to analyze SpeX (spectroscopy observation instrument) from IRTF.
* Nayoro Pirka, Japan: One of few cases of using IRAF. If you use MSI (multi spectroscopy imager), you will use MSIRED package, which are written fully in IRAF CL.
* Subaru: If you used FOCAS of Subaru at Hawai'i, you will receive FOCASRED package, which you may use either IDL or IRAF (recommended to use both).



### New Major Facilities Wants Freedom from IRAF

By the "New Major Facilities", it includes HST, JWST, LSST, and future space telescopes and/or large projects.

STScI, which will be the [Science and Operations Center of JWST](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope#Ground_support_and_operations), as well as HST, selected Python 3 for their data production. They are now developing pipelines for JWST ([github](https://github.com/STScI-JWST/jwst)). All the new packages from STScI, e.g., the famous DRIZZLEPAC (now named AstroDrizzle), supports python only (preface and section 5.1 of this [handbook](http://documents.stsci.edu/hst/HST_overview/documents/DrizzlePac/drizzlepac.pdf)). The reason for choosing Python for the new era is described in 2013 JWST Roadmap, e.g., [Section 3.5](http://www.stsci.edu/~ferguson/roadmap/html/intro.html#multiple-interfaces) and why we should avoid IRAF in general sense in [Section 4.2](http://www.stsci.edu/~ferguson/roadmap/html/intro.html#remove-scientist-dependency-on-iraf).

The LSST data management team has chosen to use Python 3 and C++ ([main DM page](http://dm.lsst.org/)), although they will support python 2.7 for few years but not long.

> Python 2 will be cease to be supported soon. See, e.g., [PEP373](https://www.python.org/dev/peps/pep-0373/), [Python3Statement](http://www.python3statement.org/), [python clock](https://pythonclock.org/) made by Guido (The inventor of Python). All the astropy and its affiliated packages, matplotlib, and many more which you are familiar with, will not support Python 2 within only few years (even before you get a PhD!).
>
> For useful things in Python 3 compared to 2, see [Python 3 for scientists](https://python-3-for-scientists.readthedocs.io/en/latest/python3_user_features.html).

The programmers working for these large projects are contributing to astropy core packages, too.

### Python: An Alternative

If you are a very smart persion, you can of course directly make a binary code (11000101011101000010101101...), and this will be the most efficient way. When I was an undergrad student at KAIST, there was this professor who taughte the Introduction to Programming course, which was mandatory, said "I had a friend who believes it is the best way to make all the programs in binary from the beginning. But the thing is, not everyone is as smart as she does."

The second best option might be using some low-level languages, such as C, or make appropriate modifications to pre-existing IRAF and make it more efficient/faster. The thing is that, we have to think about the **vast majority of people who are not** that smart (plus, as mentioned above, there is no one interested in developing IRAF). This is because we do not have much room to lose such people who may serve important roles in the future of astronomy. Quite many scientists are also involved in that *vast majority*, and they are not (and likely should not) practiced to be a programmer.

Thus, the next option we may choose, are languages which have the following strong points:

1. Easy to learn and coding (scripting),
2. i.e., "a language that more people can participate/contribute"
3. Reliable, since they are maintained, managed, stablized, and optimized by computer scientists / programmers / experts,
   * i.e., "a language which are also being used by non-astronomers"
4. Have no license problem,
5. OS-independent (if properly coded),
6. Have good and enough amount of manual/examples,
7. Have enough number of useful packages in reliable manner,
8. And have many users so that faster feedback/Q&A can be made.
   * e.g., stackoverflow
9. Additionally, languages which have potential of having connections with future languages, so that learning it can be investment to our future.

**Python is a language which satisfactorily meets all the above conditions**

It is not easy for laymen to use SPP/CL, as it has no highlighting or syntax coloring functionality in any of IDE and has complicated manuals. For the third item, Python is completely free, installed by default to virtually all LINUX distributions, and thus no license issue can come to Python users. The fourth and fifth items are strong points of Python which most Python users would agree. If you use Anaconda or Git, you can manage and update packages even on Windows via shell script, and the Spyder IDE is provided by default. Python is well known to have well structured manuals.

The sixth item means NumPy, SciPy, Matplotlib, and AstroPy, which we will learn throughout this course. They are specialized to majority of numerical calculations and graph plotting. Seventh item can be checked at web sites such as Stack Overflow. Tremendous amount of manual and Q&A database can be found, incomparable to IRAF, and also more diversity is there since non-astronomers also use it, unlike IDL.

Finally, Julia, Jupyter, Markdown (this preface is also made from md), and many future softwares uses Python-like grammar or implement ways to use Python. Python is good for large-data analysis, too, which is the future of astronomy. The strong point of Python with Jupyter can be seen throughout this TA class. Although it is commercial, you can also find Python tools attached to Excel and make neat graphics without errors. We may need a long time to see Python fades out into past.

### So... Use Python

Some astronomers dreamt for using Python for these reasons. That is now descending as Astropy Project. Alongside with the "core" package, astropy, there are other packages that are listed under the name of "Astropy Affiliated Packages". You can easily manage versions of packages and update them using Anaconda, and it is extremely easy to fix bugs compared to IRAF/IDL. Astropy itself also provides neat and clean examples and manuals.

Additional benefits we may get from using Python is to learn how to be prepared for new future environment. Even if Python becomes deprecated and a new language becomes the new *standard* on some day, you can easily adopt to that new environment. On top of that, new future language can become easier than Python, but not the other way, your value will get higher in that era as you can cope with more languages.

However, these do not mean Python has no problem. There are quite many packages which are not stable (no stable release), even though they are considered as "widely used" and "working perfectly". Core packages of Astropy works fairly well, but there are some [known issues](http://docs.astropy.org/en/stable/known_issues.html). Photometry and spectroscopy tools are still 0.x versions. Only photometry version (photutils) is considered as "stable" from [Astropy affiliate website](http://www.astropy.org/affiliated/). Critically, LSST and JWST are not operating yet, so all the packages are not really completed yet.

## Transformation into a New Curriculum and Possible Pitfalls

I have briefly introduced why astronomers started using Python. You may have understood that it is at least worth considering the reformation of the structure of AO practice sessions, which had been using IRAF or IDL. The basic philosophy I am trying this new transformation is simple: The belief that education should let educatee to be prepared for their future, and this should be one of the primary goals of it.

**I know that it may be comfortable and easy to teach IRAF as the TA.** But I wonder whether it really is an efficacious curriculum if students realize the existence/importance of Astropy *after* they become pre-researchers while school teaches IRAF only. Now that Computational Astronomy course of SNU changed its main programming language to Python from IDL, and I guess this will be a great opportunity to make flexible Python environment at SNU for future.

One thing that scares me is the **possibility of a big gap between the generations who've learnt IRAF and AstroPy**. I cannot say it is like using photoplate after implementation of CCD, but it feels like. As an example, the terms used in Ginga is slightly different from that of ds9, so it's quite confusing if you are used to SAO ds9. Now my role, as a TA who's earning money from this work, is clear: While contributing to construct a new educational curricula which fits better to prepare for the future, yet I have to amalgamate the gap between generations to avoid excessive inefficiency and lose of humanpower in communications between those generations. It might be tough for young studnets because they should take the redundant burden with older generation in communication; but this kind of pain has been there when we transformed from cgs to SI unit system. The reason for the widely used cgs values in astronomical field seems to be due to the low weighting to the "efficient communication with other fields of sciences" factor, but I worry that this might have become a giant wall which isolates astronomical society. Some other critiques to this Python trial may be that this astropy, and even Python, will have become a *legacy of the past* somewhere in the near future. I do, however, worry much more about the severance between our generations and much younger generations in the future, if we choose not to give enough opportunity to experience the frontier of modern (computational/observational) astronomy, just because IRAF has been the "historical standard".

My basic reason for this is that not all educatee are smart enough to find and "experience" of such things by themselves, as I am. If I didn't have personal antipathy toward observation course which I took right after I became a graduate student, I would never dare to find softwares other than IRAF. Not because of other reasons, but because I had had too much things to digest by myself at that time compared to my ability, so that I had no much mental space to think about other issues than coursework itself. I believe this kind of effort to help them with modern technology is inevitable to draw the maximum efficiency of students like me.

It does not mean I will not deal with IRAF (but I will not deal with IDL at all): It is up to you to choose which one you use (IDL, IRAF, ds9, Astropy, ...), and I personally think that the knowledge on using IRAF is quite essential at least until next decade. This is because

1. Many observatories still use IRAF as default.
   * you may see some computers at observatories which are prepared for those who want to primitively check the observed data using only IRAF).


2. The importance of smoothness in communication between older and younger generations in this field.
3. Historically important.
   * Even if we use computers for observation, some information on CCD and even photoplate can help us understand the reasons for certain calculation and processes.

In short, it roots from the faith that **we should avoid radical discontinuity between generations**, while guaranteeing the freedom of choosing language/software. Also I have to keep in mind that the IRAF tutorial should not be a big burden for students who learns Python.

The reason I am preparing this manual is not only because I believe that this new trial must not end as a one-time trial, but also continuous in time domain such that the transition from older to younger-fashioned way is smooth enough so not much social cost is spent in the future.

Now the task left in front of me is to make this manual easy and simple with readability, yet contains enough information, so that next educatee and TA/instructor can be benefitted from it. **A new TA or educator in the future, who will take the holy responsibility of education, which is strict and priceless, must critically evaluate this new trial with long and tortuous consideration, investigation, and continuous effort. Then they should decide how they will write the new future in front of them.**

Even though the students took this course might become the sole isolated people using astropy, this manual should totally be abandoned *if* an unassailable disadvantage, inefficiency, or problems are found from this curriculum. That is totally my fault, who will have been the former TA, and that is the reason why I cannot skip the lectures on practicing IRAF and SAO ds9. If that unfavorable situation occurs, then we have to go back to the previous IRAF/ds9 + IDL curriculum. For it not to be that way, my effort to clarify whether it is a reasonable trial worth doing is the most important.

I will do my very best for this course to be remembered as a part of your "good memory" during this year. If it turned out that it's not, then it totally is my fault, and I beg your cool-headed critics and feedbacks.


At 19-dong of SNU,

First written on the verge of winter of 2017,

Updated on the fringes of summer of 2017,

Updated on the first day of 2018 Spring semester,

Yoonsoo P. Bach





