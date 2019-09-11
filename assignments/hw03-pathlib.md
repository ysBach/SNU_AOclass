## Problem Set 03 [30 point]

### Instructions

Please use python 3.6+ (Never use python 2). 

For other packages: Although I didn't run all the tests, likely there will be no problem if you use decently recent versions of any packages used in the homework (any version released after 2017).

Here we will learn how to code in _pythonic_ way.  **Open your terminal (or Jupyter Notebook) at an *empty* directory**. Start solving the problems after running the code below:

```python
from pathlib import Path
TOPPATH = Path('.')
```

You can use multiple lines of code to answer the following problems.

### Problems

Answer the following problems [2 points each]

1. Make an empty file named ``test00.txt``.

   - Hint: set ``filepath = TOPPATH/'test00.txt'`` , and use ``filepath.touch()``.

2. Make a simple code which does ``filepath.touch()`` if ``filepath`` does not exist. Use ``if``.

   - Hint: You can use ``if filepath.exists(): ...``

3. Make a list which contains the path objects for the 10 files: ``test01.txt``, ``test02.txt``, ..., ``test10.txt``.

   - Hint: Initiate a list ``filelist = []``.

   - Hint: use for loop like this

   - ```python
     for i in range(1, 10):
         filelist.append(TOPPATH / f"test{02:d}.txt")
     ```

   - (You will learn what ``f"{02:d}"`` means later. If you want, google "python format string leading zeros".)

4. Make 10 files with empty contents, named ``test01.txt``, ``test02.txt``, ..., ``test10.txt``.

   - Hint: ``for fpath in filelist:`` and use ``fpath.touch()``.

5. Make ``filelist2`` which contains ``test08.txt``, ``test09.txt``, ..., ``test12.txt``.

   - Hint: Do as ``filelist``, but change the ``range`` part.

6. Iterate through the paths in ``filelist2``, and make an empty file of that path if it does not exist.

   - Hint: Use for loop such as ``for fpath in fililist2``. 
   - Hint: Use ``if fpath.exists():`` inside the for loop.

7. Make a list ``filelist3``, which is the union set (list) of ``filelist`` and ``filelist2``.
   - There are several ways to do this. One possibility is to use for loop and ``append `` as you did in ``filelist`` and ``filelist2``.
   - Another possiblility is to use ``for fpath in filelist:`` and use ``if fpath in filelist2:`` etc.
   - A simpler pythonic way is to use ``list(set(filelist).union(filelist2))``.
   - Tip: If you want union of more than 2 lists, you should do ``list(set().union(a, b, c, d))``.
8. Make a list ``allfiles`` of all the file paths in your ``TOPPATH``.
   - Hint: ``allfiles = list(TOPPATH.glob('*'))``
9. Append a fake path ``tttt00.txt`` to ``allfiles``.
   - Hint: ``allfiles.append(TOPPATH/'tttt00.txt')``
10. Delete ``allfiles[0]``. 
    - Hint: ``allfiles[0].unlink()``
11. Delete all the files you made.
    - Hint: Use for loop. Then ``if fpath.exists():`` and ``fpath.unlink()``.



Advanced [8 points]

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



