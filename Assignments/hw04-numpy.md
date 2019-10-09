## Problem Set 04 [30 points]

### Instructions

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

### Problems

2 points for each problem:

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
    
    * Hint: use ``np.arange``
    * Check ``v[0] == 0``
12. Select only the odd-index elements of ``v``, and reshape it to ``(2, 25)`` array and save it as ``w``.
    * Hint: using ``array[::2]`` will give even-index elements. How can you get the odd-index elements?
    - Hint: Reshaping is done by ``array.reshape(n1, n2)``.
13. Take the median of ``w`` along the axis of ``1``, i.e., ``print(w.shape)`` should be ``(2,)``
    
    - Hint: use ``np.median`` with ``axis`` option.
14. For magnitude differences of 0, 1, .., 5 mag, print the flux ratios using Pogson's formula.
    
    - Hint: ``np.arange`` can make numpy array of [0, 1, ..., 5]. Then use ``10**<something>``.
15. For flux ratios (say, array ``r`` = flux1 / flux2) of 0.10, 0.15, 0.20, ..., 2.00, calculate the magnitude difference using Pogson's formula, and save it as ``dm``.
    
    - Hint: similar to above, but with ``np.log10``.

