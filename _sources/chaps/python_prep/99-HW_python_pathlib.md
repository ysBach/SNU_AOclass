(HW:python_prep)=
# HW Python Basic & ``pathlib``

## Problem Set 1 [45 points]

Please use python 3.6+ (Never use python 2).

For other packages: Although I didn't run all the tests, likely there will be no problem if you use decently recent versions of any packages used in the homework (any version released after 2020).

**If you want, you can increase the number of input parameters, make subfunctions, etc, to realize more general functionalities, unless the "instructions" say not to.**

This is a set to make you familiarize with Python. I had to design this problem set, because we mostly do not look at the references and/or not trying to use google. You may refer to *Think Python* chapters and if you cannot find the answer, you must use the Internet.

### Problems

- **Warn**: Be aware not to miss any period (`.`) or quotation marks (`'` or `"`).

1. Write down the results of the following, i.e., write down the results when you `print()` each of these.  [22 point]

   1. `a1 = 3 + 4`
   2. `a2 = 3 + 4.`
   3. `b = 4 - 2`
   4. `c = 9 * 8`
   5. `d = 22 / 3`
   6. `e = 22 // 3`
   7. `f = 22 % 3`
   8. `g1 = 2**2`
   9. `g2 = 2.**2`
   10. `g3 = 2**2.`
   11. `h = "hello"`
   12. `a1t = type(a1)`
   13. `a2t = type(a2)`
   14. `bt = type(b)`
   15. `ct = type(c)`
   16. `dt = type(d)`
   17. `et = type(e)`
   18. `ft = type(f)`
   19. `g1t = type(g1)`
   20. `g2t = type(g2)`
   21. `g3t = type(g3)`
   22. `ht = type(h)`

2. Using `assert`, write a one-line code that [4 point]

   1. checks whether `22` is equal to `3*e + f`.
   2. checks whether `g2` is equal to `g3`

3. Write a one-line code which will define `str_quotation`, such that `print(str_quotation)` gives `Hello, World! It's me "Hi"`.  (Hint: use the escape charater `\`, e.g., `\"`.) [4 point]

4. Write down the results of the following, i.e., write down the results when you `print()` each of these. [10 point]

   1. ``L_str = ["a", "b", "c"]``
   2. ``L_num = [1, 2, 3.]``
   3. ``tLs = type(L_str)``
   4. ``tLs0 = type(L_str[0])``
   5. ``tLn2 = type(L_num[-1])``
   6. ``d1 = {'name': ['Halpha', '[Mg II]', '[O III]'], 'intensities': [1, 0.1, 0.2]}``
   7. ``d1_k = list(d1.keys())``
   8. ``d1_e = list(d1.items())``
   9. ``d1_lines = d1['names']``
   10. ``d1_inHa = d1['intensities'][0]``


## Problem Set 2 [50 points]

Please use python 3.6+ (Never use python 2).

For other packages: Although I didn't run all the tests, likely there will be no problem if you use decently recent versions of any packages used in the homework (any version released after 2017).

Here we will learn how to code in *pythonic* way. **Open your terminal (or Jupyter Notebook) at an *empty* directory**. Start solving the problems after running the code below:

```python
from pathlib import Path
TOPPATH = Path('.')
```

### Problems
Answer the following questions with **one line** code. [2 points each]

1. Make a directory named ``class_01``.
   - Hint: ``newdir = TOPPATH/'class_01'`` and ``newdir.mkdir()``
2. Try to make a directory named ``class_01`` *again*. What error do you see?
3. How can you avoid this error?
   - Hint: try using ``.mkdir(exist_ok=True)``.
4. Make a subdirectory ``assignment_01`` inside ``class_01``.
   - Hint: ``hw01 = newdir/'assignment_01'`` and do ``.mkdir()``.
5. Make the following directory using one line code: ``class_01_appendix/code_snippets``.
   - Hint: Use ``.mkdir(parents=True)``
6. Make a list of all the files and directories in the current directory.
   - Hint: ``flist = list(TOPPATH.glob('*'))``
7. Find how many files and directories are in the current directory.
   - Hint: ``len(flist)``
8. Check whether ``newdir`` is an existing path.
   - Hint: try ``newdir.exists()``
9. Check whether ``newdir`` is a file or directory.
   - Hint: try ``newdir.is_file()`` and ``newdir.is_dir()``
10. Find the absolute path of ``newdir``.
    - Hint: ``newdir.resolve()``

Answer the following problems [2 points each]

1. Make an empty file named ``test00.txt``.
   - Hint: set ``filepath = TOPPATH/'test00.txt'`` , and use ``filepath.touch()``.

2. Make a simple code which does ``filepath.touch()`` if ``filepath`` does not exist. Use ``if``.
   - Hint: You can use ``if filepath.exists(): ...``

3. Make a list which contains the path objects for the 10 files: ``test01.txt``, ``test02.txt``, ..., ``test10.txt``.
   - Hint: Initiate a list ``filelist = []``.
   - Hint: use for loop like this
   - ```python
     for i in range(1, 11):
         filelist.append(TOPPATH / f"test{i:02d}.txt")
     ```
   - (You will learn what ``f"{02:d}"`` means later. If you want, google "python format string leading zeros".)

4. Make 10 files with empty contents, named ``test01.txt``, ``test02.txt``, ..., ``test10.txt``.
   - Hint: ``for fpath in filelist:`` and use ``fpath.touch()``.

5. Make ``filelist2`` which contains ``test08.txt``, ``test09.txt``, ..., ``test12.txt``.
   - Hint: Do as ``filelist``, but change the ``range`` part.

6. Iterate through the paths in ``filelist2``, and make an empty file of that path if it does not exist.
   - Hint: Use for loop such as ``for fpath in filelist2``.
   - Hint: Use ``if fpath.exists():`` inside the for loop.

7. Make a list ``filelist3``, which is the union set (list) of ``filelist`` and ``filelist2``.
   - There are several ways to do this. One possibility is to use for loop and ``append`` as you did in ``filelist`` and ``filelist2``.
   - Another possiblility is to use ``for fpath in filelist:`` and use ``if fpath in filelist2:`` etc.
   - A simpler pythonic way is to use ``list(set(filelist).union(filelist2))``.
   - Tip: If you want union of more than 2 lists, you should do ``list(set().union(a, b, c, d))``.

8. Make a list ``allfiles`` of all the txt file paths in your ``TOPPATH``.
   - Hint: ``allfiles = list(TOPPATH.glob('*.txt'))``
9. Append a fake path ``tttt00.txt`` to ``allfiles``.
   - Hint: ``allfiles.append(TOPPATH/'tttt00.txt')``
10. Sort the list ``allfiles`` and print it.
    - Hint: use ``.sort()`` appropriately, and just ``print(allfiles)``
11. Delete ``allfiles[0]``.
    - Hint: ``allfiles[0].unlink()``
12. Delete all the files you made.
    - Hint: Use for loop. Then ``if fpath.exists():`` and ``fpath.unlink()``.


**Advanced [6 points]**

Python has a very useful ``try-except-finally`` clause.

Do ``touch`` to all the paths in ``filelist3`` again.

Then use

```python
for fpath in filelist3:
    try:
        fpath.unlink()
    except FileNotFoundError:
        continue
```

1. Does it run correctly? Are all the files removed?
2. *Think* about what each line means. (No answer required)


