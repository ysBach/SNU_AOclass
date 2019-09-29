## Problem Set 05 [30 points]

### Instructions

Please use python 3.6+ (Never use python 2). 

For other packages: Although I didn't run all the tests, likely there will be no problem if you use decently recent versions of any packages used in the homework (any version released after 2017).

Here we will learn how to code in _pythonic_ way. Start solving the problems after running the code below:

```python
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('default')
```

While answering the problems, follow these rules:

1. **Never use ``for`` or ``while`` loop**.
2. You **should not import any other packages**.
3. Answer to **each problem** must be a **one-line** of python code.
4. For each problem, I gave hints. **It is also homework for you to search for those on google**.

### Problems

You can fill in the ``?`` parts in the Hints and use that to answer the questions. Or, you can just make your own answer, ignoring the Hints.

2 points for each problem:

1. Setup numpy random seed as 1234.
   * Hint: ``np.random.seed(?)``
2. Make an array of shape 10 by 2, sampled from normal distribution of $X \sim N(50, 3^2)$. Give it a name ``data``.
   * Hint: ``np.random.normal(loc=?, scale=?, size=(10, 2))``
3. Now regard this data represents two sampling processes of 10 samples out of the normal distribution. Get the sample mean of the two sampling processes. Give it a name ``avgs``.
   * Hint: ``np.mean(data, axis=?)``
   * Think why we need ``axis`` option.
4. Get the sample standard deviation of the two sampling processes. Give it a name ``stds``.
   * Hint: ``np.std(data, axis=?, ddof=1)``
   * Think why we need ``ddof=1``.
5. Calculate the standard errors (s.e.: $\mathrm{s.e.} := s/\sqrt{N}$ for sample standard deviation s and sample number N) of two sampling processes. Give it a name ``ses``.
   * Hint: ``stds / np.sqrt(data.shape[?])``
6. Are the ``avgs`` +/- ``1*ses`` of the two sampling cases overlap? 
7. Are the ``avgs`` +/- ``1*stds`` of the two sampling cases overlap? 

The standard error here is the 1-sigma confidence interval of the *point estimator for the mean*, based on the central limit theorem (CLT; refer to the ``Books/`` of this repo). Simply put, this is the estimated interval of the mean. On the other hand, standard deviation is the scatter of data. Note that even though you have large standard deviation, the standard error can be very small as N increases (think about coin tossing experiments with head=-1 and tail=+1).



[6 points]

8. Consider these two estimates are the measurement of the line width of an AGN emission line in Feb 2000 and Jun 2010. Will you say the emission line width has significantly changed in 10 years? They differ in the standard error sense, but in our simple "simulation" they both came from the identical distribution. That is, the true line widths (which we don't know in the real observation) were identical but the observations indicated that the estimated means are quite different. What happened? How would you understand this? If you have to write a research paper with these results (you cannot observe again back in 2000 and 2010!), what will be your conclusion?
   * Just describe your opinion. I haven't put any fixed answer for this problem. 



[5 points]

The CLT says the distribution of the sample means follow normal distribution, regardless of the original distribution. Let's check this. 

9. Fill in the ``?`` parts below to generate the histogram of sample means for 100000 sampling procedures (each case you draw 10 samples) from a Poisson distribution of parameter lambda = 2, and the mathematically expected gaussian function (mu = true mean = lambda, sigma = true standard deviation = sqrt(lambda)).

   ```python
   np.random.seed(1234)
   
   def gauss(x, mu, sigma):
       return np.exp(-(x - mu)**2/(2*sigma**2))
   
   # For Poisson distribution, variance = mean = std**2
   mean = 2
   variance = ?
   n_sample = 10
   
   data_pois = np.random.poisson(lam=mean, size=(n_sample, 100000))
   avgs_pois = np.mean(data_pois, axis=0)
   
   h = plt.hist(avgs_pois, bins=100)
   x = np.linspace(0, 10, 100)
   
   expected_mu = mean
   expected_sigma = np.sqrt(variance)/np.sqrt(n_sample)
   plt.plot(x, h[?].max()*gauss(x, ?, ?))
   plt.show()
   ```

   Does the histogram follows expected Gaussian curve? Note that the original distribution you sampled is **NOT** Gaussian at all (Poisson distribution with mean 2 is far from normal distribution).



[5 points]

Consider you created M universes which have identical mean value of X (e.g., Hubble's constant, dark energy fraction, etc). The 1-sigma confidence interval (CI) of X means that, if you calculated CI from the data obtained from identical observations (or measurements or experiments) from each M universes, 68.27% of the universes will contain the true mean of X within its own CI. Other (31.63%) universes will not contain the true value within their CI. Let's confirm this using simple simulation below.

10. Fill in the ``?`` parts below to print the percentage out of the 100000 universes with 10 samples which their CI actually "hit" the true value.

    ```python
    np.random.seed(12354)
    
    true_mu = 50
    true_sigma = 3
    n_sample = 10
    
    data_ci = np.random.normal(loc=?, scale=?**2, size=(n_sample, 100000))
    avgs_ci = data_ci.mean(axis=?)
    stds_ci = data_ci.std(axis=?, ddof=1)
    ses_ci = stds_ci / np.sqrt(data_ci.shape[?])
    
    hit = ((true_mu > avgs_ci - ses_ci) 
           ? (true_mu < avgs_ci + ses_ci))  # Hint: one of & and |
    print(100 * np.count_nonzero(?)/np.shape(hit)[?], "%")
    ```

    The result must be similar to 68%.

    * Note: Most likely your value is smaller than 68%. That is because, under the CLT logic, the statistic $(\bar{X}-\mu) / (s/\sqrt{N})$ follows the Student t-distribution with degrees of freedom (N - 1) (in our case, 9), not the standard normal distribution, which is the limiting case of the t-distribution when degrees of freedom is infinity. Therefore, the calculation above which uses ``avgs_ci - ses_ci`` must have multiplied a factor, i.e., $t_{(n-1),\, \alpha/2}$ (for the signicance level $\alpha=0.6827$ for the 1-sigma), which is always larger than 1. Thus, we are "underestimating" the CI in the above example, so your calculation is likely smaller than 68%. If you increase ``n_sample``, the final result will get larger and converge to 68.27 %.