# SNU AO Class
(SNU = Seoul National University, South Korea; AO = Astronomical Observation class)

This is the lecture note initially made by me (Yoonsoo P. Bach, @ysBach). The original contents started to be created in 2016 Fall, when I first took the TA role in the AO class. It used to be maintained until around 2021, and I left the TA role and it was left as was. At the end of 2022, I was kindly asked to make the material more sustainable and stable. Before I leave SNU after getting the PhD, I felt it was my duty (social responsibility) to finish this work.

```{admonition} Brief reasons why I made this
:class: dropdown
When the python lecture note was first made in 2016-2017, astropy had version 1.x, and there was virtually no useful lecture materials on the web **at all** (when it comes to data reduction in python). Unfortunately, python tutorials such as astropy tutorials or other tutorials or lecture notes I found on web merely dealt with high-school level programming, and barely useful. Frankly speaking, I was even upsetted by some people who merely did `print("hello world")` level coding or just a copy-and-paste of the readthedocs manual and uploaded it as lecture material or even publish a package or preoccupy the package name---this not only confused me, but also is an undesirable behavior as an educator, in my opinion. I guess Matt Craig's note (currently hosted at [here](https://github.com/astropy/ccd-reduction-and-photometry-guide)) was the only teaching material that was useful when it comes to astronomical data reduction in python, at least as of around 2018. I found the note a bit too late, so my notes had already diverged a lot from their's (which is, imo, a good thing---diversity). Another philosophical motivation that encouraged me is a [blog post](https://jradavenport.github.io/2015/04/01/spectra.html) by James Davenport, which I encounted in around year 2018:
> ... "**put up or shut up**". I’m tired of people (like me) saying “boo IRAF”, or “we need new tools”, and not building them. That’s why I applaud projects like astropy, emcee, and astroML: they aren’t just complaining, they’re doing. So this is my attempt at doing.

Their package, [pyDIS](https://github.com/StellarCartography/pydis), was the only thing I could find that actually succeeded in reducing long-slit data using python, except for my lecture note (A small discussion at Python users in Astronomy group: [first](https://www.facebook.com/groups/astropython/posts/2615675052010502/?__cft__[0]=AZXosdoaZWOLuSLf8beBbIN7U8GzscCXa7_Xx_XP_kY1aa6-LqlndyXka2xhgn1p3vldEb-nT-9Mn-8DSoZnac1KNRbDOOrZPYHzGENpMkK-l7x-5bpL--Ialvj_JXKMElueLp_GlwA8haDlbSQ7yMar&__tn__=%2CO%2CP-R), [second](https://www.facebook.com/groups/astropython/posts/2617839181794089/?__cft__[0]=AZU3TKqxLi-J9oabIldncj5as1D0GewUUNs0MZxNuW-GpW1UX-Hsc-rGVNBQpjQZsoItQyeAp6vR9W9oeLdjSLGW8AhTO6pwSkuC7JIMbNV8dKqH541RSCjLJj3JuRyCqxDiiLbtpJq0geIEDADc67Zz&__tn__=%2CO%2CP-R)). Not even astropy had any useful tool for that (astropy/specutils were equipped with useful functions only after 2020s).

So I decided to make (1) **USEFUL** material, (2) make the name/title specific, so that I do not pre-occupy the "good" names without a confidence to make it really "good". I think the concepts, theories, tools or codes given in this lecture note is useful enough at least for beginner (but professional) observational astronomers. Also, I believe the name of this repo `SNU_AOclass` and packages (e.g., `ysfitsutilpy` and `ysphotutilpy`) are specific enough, not to pre-occupy "good" names.
```

## How to use this lecture note
This note is composed of three major parts.

Theoretical lecture (Books)
: The theory part (mathematical derivations, verbal explanations, etc) is made with **TeX** as a book-like format.
```{admonition} Why not Jupyter-Book?
:class: dropdown, tip
I tried to migrate those practical parts into Jupyter-Book too, but I found such kind of documents must be stored in TeX for the ultimate reproducibility. Jupyter-Book is also an evolving package, which means that it may undergo backward-incompatible upgrade in the near future, or even disappear as computational facilities (computers, OS, programming languages, etc) evolve. TeX, on the other hand, will be as is forever by design.

Students may also feel more comfortable to see long equations + figures + tables as PDF file rather than HTML.
```

Practical lecture (JupyterBook)
: The coding part (data reduction and analyses) is made with Jupyter-Book. I found Jupyter-Book displays the material much better than simple Jupyter notebooks hosted by nbviewer, thanks to MyST.
In addition to this Jupyter-Book, I will give some lectures using PowerPoint, and they are also uploaded to the repo.

Assignments
: The course contains observational project. To complete it, you need to practice coding & observational preparation. Assignments will be your friend to guide you through the process.


ver 2023 (2023 spring)