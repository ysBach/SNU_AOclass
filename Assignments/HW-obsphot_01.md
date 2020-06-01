## Note

I am not assuming you to provide perfect answers to these at your first trial, even without any real observation. Don't be too worried, we will revisit this set of homework again and again.

This problem set will also be updated over time (due to the lack of TA's ability...)



## Information

* Assume you are making an observation in June, using SNU astronomical observatory 1-m telescope. 
* The pixel scale is roughly 0.31"/pixel and the detector has 4k x 4k pixels, resulting the FOV of roughly 21' by 21'.
* Minimum altitude must be ~ 30 degree.

* If you observe a 14-mag star in R_C band at airmass 1.4 with EXPTIME=60s, the SNR ~ 65.
* For StarAlt, you can use ``126.954 37.455 150 +9`` for ``Observatory``.



## Problems

5 pts each

1. What is the target you selected? 
   * Provide RA, DEC, apparent magnitude at the filters you want to observe, other information you think important
2. What is the science you are interested in? Describe it shortly.
3. What is/are the 
   1. signal to noise ratio (SNR) required for that science? 
   2. exposure time you need (refer to the information above)?
   3. number of nights you need?
   4. best observing dates?
   5. sky condition, including seeing size? (clear sky is good but difficult to be assigned..!)
4. When you turn on the telescope, it cannot quickly find the object accurately. It may be looking at somewhere "close" to the target, but not exactly putting your object at the center of the FOV. Considering the information given above, prepare "finding chart", i.e., the star charts near your object. Indicate your target and some bright objects nearby it, so that you can identify your target's location based on them.
5. Find at least two standard stars (blue-red pair: see lecture book), which will be observable at the night. You may use stars from SDSS ([link](https://www-star.fnal.gov/ugriz/tab08.dat)) or Landolt's ([link](https://www.eso.org/sci/observing/tools/standards/Landolt.html)). 
   * Good thing for Landolt's standard star field is that if you take one image, you have many stars at identical airmass and different colors. For our case, since we don't have SDSS filter system, maybe it's better to use Landolt's.
6. Use [StarAlt](http://catserver.ing.iac.es/staralt/) or other program you are familiar with. Check moon distance, minimum altitude, etc and remove any object you cannot properly observe.
7. Now that you have selected a target and at least two standard stars, find the stars from, e.g., [SIMBAD](http://simbad.u-strasbg.fr/simbad/).
   * NOTE: sometimes the naive use of star name does not work. In that case, you need to search using RA/DEC coordinate, and manually find the star.
8. For each standard star, roughly estimate how long EXPTIME will be needed for your purpose.
9. Describe the order of observation you want to make.