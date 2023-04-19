(00:python_prep)=

# Python Preparation Course

Here, I will put materials you can study and soem external references for studying python rather than much of other explations. You must install python first (e.g., Anaconda). See the note [Softwares](00:Softwares) to install python, and then [Prepare Python](00:Prepare_Python) to set up the environments.

## Tutorials

* You will learn ``pathlib`` and other simple python grammars throughout the first few homework assignments.
* [numpy tutorial](00:numpy_tutorial): Basic numpy to a bit advanced masking.
* [pandas tutorial](00:pandas_tutorial): Basic pandas, including iteration and grouping.
* [astropy fits tutorial](00:astropy_fits): Basic FITS I/O and explanations about FITS, header, extensions.

## HW Assignments

* [HW on general python](HW:python_prep)
* [HW on using numpy](HW:numpy)
* [HW on using pandas](HW:pandas)
* [HW on using FITS and astropy](HW:astropy_fits)

## References

### References - Python in Astronomy

1. Matt Craig's [ccd as book](https://www.astropy.org/ccd-reduction-and-photometry-guide/v/dev/notebooks/00-00-Preface.html)
   * **HIGHLY RECOMMENDED!**
   * Explains details about the astrnomical images, with worked examples. If you're not familiar with astrnomical data reduction, this is a good reference to start with.
2. Matt Craig's [reducer](https://reducer.readthedocs.io/en/latest/)
   * A simple Jupyter Notebook to reduce data, which the author used for his classes.
   * If you want, you may get ideas from this and use it in your own code.
3. Lecture note for [Técnicas Experimentales en Astrofísica](https://guaix.fis.ucm.es/~jaz/master_TEA/tea_book/intro.html)
   * Unfortunately, this is now unaccessible (retrieved 2022-04-05)..
   * I was recommended by one of my friend at MPI, and this looks very well structured for beginners. It can be a good complementary material to this lecture note.
4. [astropy tutorial](http://learn.astropy.org/)
   * I personally think the web is too laggy but some tutorials seem informative, e.g., [UVES spectrum analysis](http://learn.astropy.org/rst-tutorials/UVES.html?highlight=filtertutorials).
5. The latest or stable official websites for each package, e.g., [astropy](http://docs.astropy.org/en/stable/), [photutils](https://photutils.readthedocs.io/en/latest/) and [ccdproc](https://ccdproc.readthedocs.io/en/latest/) themselves are good references.

### General Python

* Book [_Think Python_](https://greenteapress.com/wp/think-python-2e/)
  * **HIGHLY RECOMMENDED!**
* Prof. Jinsoo Park(박진수)'s [lecture notes](https://github.com/jinsooya/lecture-notes)
* Ivezić et al.'s book ([Amazon](https://www.amazon.com/Statistics-Mining-Machine-Learning-Astronomy/dp/0691198306/))
  * The first author is the creator of AstroML available on [GitHub](https://github.com/astroML/astroML).
  * Recommended if you want to use python in astronomical research.
* [scipy lecture notes](https://scipy-lectures.org/)
  * Only the chapter 1 is enough maybe for this course.
* [Jake's _Python Data Science Handbook_](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/)
  * This contains too much information for beginners... Maybe you can take a look at ``matplotlib`` part, etc, for fun.
* Other free books/lectures/materials are everywhere (e.g., google "python free")
* Or summarized at some places ([example](https://www.techrepublic.com/resource-library/whitepapers/getting-started-with-python-a-list-of-free-resources/#ftag=CAD-00-10aag7f))
* Python visualization: [pyviz.org](https://pyviz.org/), [datavizpyr](https://datavizpyr.com/) (python and R)
* List of python-based Monte Carlo packages: <https://gabriel-p.github.io/pythonMCMC/>

The materials below are from [SPLIT Program of SNU](https://eng.snu.ac.kr/reserve/split-program) (retrieved 2019 Sep)

* Codecademy Learn [Python](https://www.codecademy.com/learn/learn-python)
* [Google Python Class](https://www.youtube.com/watch?v=tKTZoB2Vjuk&t=2626s)
* 한입에 쏙 파이썬, 김왼손의 왼손코딩 [YouTube](https://www.youtube.com/playlist?list=PLGPF8gvWLYyontH0PECIUFFUdvATXWQEL)
* Python 강의-김규태(고려대학교) [YouTube](https://www.youtube.com/playlist?list=PLB2ZAVLNuRBN9VCRVzDv6EFohXCWQxT-U)
* MIT OCW 6.0001 Introduction to Computer Science and Programming in Python. Fall 2016 [YouTube](https://www.youtube.com/playlist?list=PLUl4u3cNGP63WbdFxL8giv4yhgdMGaZNA)

### Jupyter Notebook / Jupyter Lab

* What is Jupyter? See [Wikipedia](https://en.wikipedia.org/wiki/Project_Jupyter#Products)
* [Notebook Basics](https://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb) by MS Azure
* awesome jupyter: [A](https://github.com/markusschanta/awesome-jupyter)
