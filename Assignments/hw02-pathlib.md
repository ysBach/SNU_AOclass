## Problem Set 02 [20 point]

### Instructions

Please use python 3.6+ (Never use python 2). 

For other packages: Although I didn't run all the tests, likely there will be no problem if you use decently recent versions of any packages used in the homework (any version released after 2017).

Here we will learn how to code in _pythonic_ way. **Open your terminal (or Jupyter Notebook) at an *empty* directory**. Start solving the problems after running the code below:

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
   - Hint: ``flist = list(TOPPATH)``
7. Find how many files and directories are in the current directory.
   - Hint: ``len(flist)``
8. Check whether ``newdir`` is an existing path.
   - Hint: try ``newdir.exists()``
9. Check whether ``newdir`` is a file or directory.
   - Hint: try ``newdir.is_file()`` and ``newdir.is_dir()``
10. Find the absolute path of ``newdir``.
    - Hint: ``newdir.resolve()``