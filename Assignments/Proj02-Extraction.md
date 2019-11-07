# Project 02

In this project, you will extract a spectrum from a preprocessed 2-D CCD image.



Please submit a simple report (including the code, showing *some* results, and giving simple explanations) which you think the TA can evaluate whether you finished the task appropriately. You may need to re-use these in your final report. 

You may refer to the presentation material from this repo (the first lecture material of the TA seminar).

Because you may encounter some problems, I recommend you to start with the brightest object (e.g., standard star). 

You don't need to answer all the questions separately. But all these processes are essential to get the final result of this project. Thus, please regard these items (Problems) as checklist: You don't have to make an answer sheet like "answer to number 1: blahblah". Just make codes which work well, and present the results.

## Problems [80 pt]

1. Identify some lines from the arc lamp you used. [20 pt]
   * If you find the comparison does not change over time, you can simply combine all the comparison lamp images and use that single data.
   * At SNU SAO 1m LISA Spectrograph, the Ne lamp was used.
   * You may make a csv file with columns containing pixel (initial peak position) and wavelength (check whether you are using in vacuo or in atmosphere wavelength values). It's recommended to use at least ~ 10-15 peaks with suitable wavelength range.
2. Find the **identification function** (A function which maps the given 2D position to a scalar wavelength value). [20 pt]
   * You must **NOT** use the pixel values you found in problem 1 directly. You need to fit a Gaussian or other suitable function with that initial position to find an accurate central pixel position.
   * You may start by doing a fitting to the wavelength-pixel values at a given spatial value. Usually people use the middle point of the spatial direction as the starting position.
   * To increase the signal to noise ratio of each line, you may use binning along the spatial direction.
   * The 2-D function can be chosen at your taste. (but conventionally people used Chebyshev or Legendre)
3. Find the **aperture trace**. [20 pt]
   * In doing this, you may need to find the object's position and sky region by yourself.
   * Sky must be fitted by a way (depending on your mathematical or scientific reasoning), which may differ from person to person. 
4. **Extract** the spectrum [20 pt]
   * You may use ``photutils``'s ``RectangularAperture`` and choose ``method`` to be ``center`` or ``subpixel``. 
   * Setting the size of the aperture is also your choice, based on mathematical or scientific reasoning.
   * The final results must contain at least the two columns: (1) wavelength (2) instrumental ADU/sec.
   * You may also estimate the error-bar of each value too (including one to all of Poisson noise, readout noise, dark noise, sky estimation noise, etc).