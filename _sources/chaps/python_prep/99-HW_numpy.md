(HW:numpy)=

# HW `numpy`

## Instructions

Please use python 3.6+ (Never use python 2).

For other packages: Although I didn't run all the tests, likely there will be no problem if you use decently recent versions of any packages used in the homework (any version released after 2017).

Here we will learn how to code in _pythonic_ way. Start solving the problems after running the code below:

```python
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('default')
np.random.seed(123)
```

While answering the problems, follow these rules:

1. **Never use ``for`` or ``while`` loop**.
2. You **should not import any other packages**.
3. Answer to **each problem** must be a **one-line** of python code.
4. For each problem, I gave hints. **It is also homework for you to search for those on google**.

### Problem Set 1 [30 points]

2 points for each problem.
(You can fill in the ``?`` parts in the Hints and use that to answer the questions. Or, you can just make your own answer, ignoring the Hints.)

1. Make an identity matrix ``A`` such that ``print(A.shape)`` results in ``(3, 3)``.
   - Hint: use ``np.eye``
2. Make a matrix ``B`` consists of random numbers and shape of ``(3, 3)``.
   - Hint: use ``np.random.rand``
3. Using ``B``, make an array ``C`` which has ``C[i, j] = sqrt(B[i, j])``.
   - Hint: use ``np.sqrt``
4. Do matrix multiplication to make an array ``D`` which is C^2.
   - Careful: ``C*C`` or ``C**2`` will give ``C[i, j]*C[i, j]``, which is different from matrix multiplication
   - Hint: search for _numpy matrix multiplication_ on google. Try ``C@C``.
5. Check whether ``B`` and ``D`` are identical.
   - Hint: use ``print(B == D)``
6. Extract diagonal components of ``A``.
   - Hint: use ``np.diag``
7. Check whether the diagonal of ``A`` is always unity.
   - Hint: ``print(A == 1)`` may work but only for element-wise. How can you convert it to a single ``True``?
8. From ``B``, extract only the elements larger than 0.5.
   - Hint: ``mask = B > 0.5`` will give you the "mask". How can you select elements only when it is ``True``? Think about the usage of mask as ``array[mask]``.
9. Update all the elements in ``B`` smaller than 0.5 to the sign-inverted value of the original value.
   - Hint: Do similar masking, but you can do something like ``array[mask] = -1*array[mask]``.
10. Calculate the sample standard deviation of ``B``.
    - Hint: use ``np.std``.
    - Hint: **sample** standard deviation must have ``N-1`` in the denominator. See ``ddof`` option of ``np.std``.
11. Make a vector ``v`` such that ``v[i] = i**2``, and ``print(v.shape)`` results in ``(100,)``.
    - Hint: use ``np.arange``
    - Check ``v[0] == 0``
12. Select only the odd-index elements of ``v``, and reshape it to ``(2, 25)`` array and save it as ``w``.
    - Hint: using ``array[::2]`` will give even-index elements. How can you get the odd-index elements?
    - Hint: Reshaping is done by ``array.reshape(n1, n2)``.
13. Take the median of ``w`` along the axis of ``1``, i.e., ``print(w.shape)`` should be ``(2,)``
    - Hint: use ``np.median`` with ``axis`` option.
14. For magnitude differences of 0, 1, .., 5 mag, print the flux ratios using Pogson's formula.
    - Hint: ``np.arange`` can make numpy array of [0, 1, ..., 5]. Then use ``10**<something>``.
15. For flux ratios (say, array ``r`` = flux1 / flux2) of 0.10, 0.15, 0.20, ..., 2.00, calculate the magnitude difference using Pogson's formula, and save it as ``dm``.
    - Hint: similar to above, but with ``np.log10``.

## Problem Set 2 [30 points]

2 points for each problem:

1. Setup numpy random seed as 1234.
   - Hint: ``np.random.seed(?)``
2. Make an array of shape 10 by 2, sampled from normal distribution of $X \sim N(50, 3^2)$. Give it a name ``data``.
   - Hint: ``np.random.normal(loc=?, scale=?, size=(10, 2))``
3. Now regard this data represents two sampling processes of 10 samples out of the normal distribution. Get the sample mean of the two sampling processes. Give it a name ``avgs``.
   - Hint: ``np.mean(data, axis=?)``
   - Think why we need ``axis`` option.
4. Get the sample standard deviation of the two sampling processes. Give it a name ``stds``.
   - Hint: ``np.std(data, axis=?, ddof=1)``
   - Think why we need ``ddof=1``.
5. Calculate the standard errors (s.e.: $\mathrm{s.e.} := s/\sqrt{N}$ for sample standard deviation s and sample number N) of two sampling processes. Give it a name ``ses``.
   - Hint: ``stds / np.sqrt(data.shape[?])``
6. Are the ``avgs`` +/- ``1*ses`` of the two sampling cases overlap?
7. Are the ``avgs`` +/- ``1*stds`` of the two sampling cases overlap?

```{admonition} A mathematical note
:class: dropdown
The standard error here is the 1-sigma confidence interval of the *point estimator for the mean*, based on the central limit theorem (CLT; refer to the ``Books/`` of this repo). Simply put, this is the estimated interval of the mean. On the other hand, standard deviation is the scatter of data. Note that even though you have large standard deviation, the standard error can be very small as N increases (think about coin tossing experiments with head=-1 and tail=+1).
```

8. [10 points] People normally approximate magnitude difference ``dm`` as fractional flux difference, 1.086 *(flux1 - flux2) / flux2 = ``1.086*(r - 1)``, because ``dm`` = 1.086 d(flux) / flux. The ``r`` values are the true ratio.
   - Now you want to calculate the absolute error of this approximation (i.e., "approximated fractional difference" - ``(r - 1)`` = dm - ``(r - 1``), and plot it as a function of ``r``.
   - Then you want to specify at which locations the absolute error is within 1 % level.
Fill in the code below for the it to correctly run.

```python
# template
r =  # <<<< Fill here (you did identical thing in problem 18)
dm =  # <<<< Fill here (you did identical thing in problem 18)
error =   # <<<< Fill in here

fig, axs = plt.subplots(1,
                        2,
                        figsize=(8, 4),
                        sharex=,  # <<<< Fill in here
                        sharey=   # <<<< Fill in here
                       )
ax1, ax2 = axs.tolist()
ax1.plot(r, dm)
ax2.plot(r, error)
plt.setp(ax1,
         xlabel=,  # <<<< Fill in here
         ylabel=   # <<<< Fill in here
        )
plt.setp(ax2,
         xlabel=,  # <<<< Fill in here
         ylabel=,  # <<<< Fill in here
         ylim=     # <<<< Fill in here to see 0 ~ +3% range.
        )
ax1.grid()
ax2.grid()

ax2.axhline(0, color='k', ls=':')
ax2.axhline(,    # <<<< Fill in here to see 1% error level
            color='k',
            ls=':')

plt.tight_layout()
plt.show()
```

9. [6 points] Consider these two estimates are the measurement of the line width of an AGN emission line in Feb 2000 and Jun 2010. Will you say the emission line width has significantly changed in 10 years? They differ in the standard error sense, but in our simple "simulation" they both came from the identical distribution. That is, the true line widths (which we don't know in the real observation) were identical but the observations indicated that the estimated means are quite different. What happened? How would you understand this? If you have to write a research paper with these results (you cannot observe again back in 2000 and 2010!), what will be your conclusion?
   - Just describe your opinion. I haven't put any fixed answer for this problem.

## Problem Set 3 (optional) [10 points]

This problem set is about statistics, which is not essential for undergraduate courses. **TA will likely skip this problem set**.

9. [5 points] The CLT says the distribution of the sample means follow normal distribution, regardless of the original distribution. Let's check this. Fill in the ``>>FILLHERE<<`` parts below to generate the histogram of sample means for 100000 sampling procedures (each case you draw 10 samples) from a Poisson distribution of parameter lambda = 2, and the mathematically expected gaussian function (mu = true mean = lambda, sigma = true standard deviation = sqrt(lambda)).

   ```python
   np.random.seed(1234)

   def gauss(x, mu, sigma):
       return np.exp(-(x - mu)**2/(2*sigma**2))

   # For Poisson distribution, variance = mean = std**2
   mean = 2
   variance = >>FILL HERE<<
   n_sample = 10

   data_pois = np.random.poisson(lam=mean, size=(n_sample, 100000))
   avgs_pois = np.mean(data_pois, axis=0)

   h = plt.hist(avgs_pois, bins=100)
   x = np.linspace(0, 10, 100)

   expected_mu = mean
   expected_sigma = np.sqrt(variance)/np.sqrt(n_sample)
   plt.plot(x, h[>>FILL HERE<<].max()*gauss(x, >>FILL HERE<<, >>FILL HERE<<))
   plt.show()
   ```

   Does the histogram follows expected Gaussian curve? Note that the original distribution you sampled is **NOT** Gaussian at all (Poisson distribution with mean 2 is far from normal distribution).

10. [5 points] Consider you created M universes which have identical mean value of X (e.g., Hubble's constant, dark energy fraction, etc). The 1-sigma confidence interval (CI) of X means that, if you calculated CI from the data obtained from identical observations (or measurements or experiments) from each M universes, 68.27% of the universes will contain the true mean of X within its own CI. Other (31.63%) universes will not contain the true value within their CI. Let's confirm this using simple simulation below. Fill in the ``>>FILLHERE<<`` parts below to print the percentage out of the 100000 universes with 10 samples which their CI actually "hit" the true value.

    ```python
    np.random.seed(12354)

    true_mu = 50
    true_sigma = 3
    n_sample = 10

    data_ci = np.random.normal(loc=>>FILL HERE<<, scale=>>FILL HERE<<, size=(n_sample, 100000))
    avgs_ci = data_ci.mean(axis=>>FILL HERE<<)  # Hint: must have length 100000
    stds_ci = data_ci.std(axis=>>FILL HERE<<, ddof=1)
    ses_ci = stds_ci / np.sqrt(data_ci.shape[>>FILL HERE<<])

    hit = ((true_mu > avgs_ci - ses_ci)
           >>FILL HERE<< (true_mu < avgs_ci + ses_ci))  # Hint: one of & and |
    print(100 * np.count_nonzero(>>FILL HERE<<)/np.shape(hit)[>>FILL HERE<<], "%")
    ```

    The result must be similar to 68%.

```{admonition} A mathematical note
:class: dropdown
Most likely your value is smaller than 68%. That is because, under the CLT logic, the statistic $(\bar{X}-\mu) / (s/\sqrt{N})$ follows the Student t-distribution with degrees of freedom (N - 1) (in our case, 9), not the standard normal distribution, which is the limiting case of the t-distribution when degrees of freedom is infinity. Therefore, the calculation above which uses ``avgs_ci - ses_ci`` must have multiplied a factor, i.e., $t_{(n-1),\, \alpha/2}$ (for the signicance level $\alpha=0.6827$ for the 1-sigma), which is always larger than 1. Thus, we are "underestimating" the CI in the above example, so your calculation is likely smaller than 68%. If you increase ``n_sample``, the final result will get larger and converge to 68.27 %.
```
