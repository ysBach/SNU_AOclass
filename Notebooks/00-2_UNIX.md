# UNIX Shell

This time, we will learn very basic things on UNIX. You can find good references from anywhere, and I will explain very basic things which are essential to follow the course materials.

Some good references are in this repo ([link](https://github.com/ysBach/AO2019/tree/master/references)):

1. [00_UNIX_Tutorial_01.pdf](https://github.com/ysBach/AO2019/blob/master/references/00_UNIX_Tutorial_01.pdf) and [00_UNIX_Tutorial_02.pdf](https://github.com/ysBach/AO2019/blob/master/references/00_UNIX_Tutorial_02.pdf) by UCSD.
   * I think it is enough to read Tutorial 1 and 2 of the first file.
2. [00_Park_Basic_LINUX.pdf](https://github.com/ysBach/AO2019/blob/master/references/00_Park_Basic_LINUX.pdf) by Keunhong Park (former SNU graduate student) in **Korean**.



## Some Jargons

* **directory**: For Windows users, the word "directory" may not be familiar. It is similar to "folder".
* **terminal**: Decades ago, there was no "monitor" like today. Terminal was used as a tunnel between the computer or calculator and human (thus "terminal"). In other words, it displays things from computer to people OR gets input from person to computer. Nowadays, terminal means a program which does similar job, but with much powerful functionalities.
* **shell**: Shell is an application running on terminal, and it interprets what people type to the terminal. Thus it is also called "command line interpreter" or just CLI. `bash` is one of such shells. 
* **prompt**: A serial of characters which indicates that the terminal is ready to get command from you. It's `$` on Ubuntu and `>>>` for Python.
* `ls`: "List"
* `cd`: "Change Directory"
* `cp`: "Copy"
* `mv`: "Move"
* `mkdir`: "Make Directory"
* `pwd`: "Present Working Directory", i.e., your present location
* `chmod`: "Change Mode"
* `rm`: "Remove"
* `~`: The home directory. Type `cd ~` and then `pwd` to see what `~` means.
* ``echo``: Similar to print functions in C or python languages.

If you want, you can find manuals from [here](https://ss64.com/bash/).



## Tutorial

Now I will show you how some simple commands work.

    aaa@YPB:~$ ls
    00_Preface-English.ipynb  01_Installation.ipynb  02_Python_Basic.ipynb   html
    00_Preface-Korean.ipynb   01_LINUX_Shell.ipynb   03_Get_the_Taste.ipynb  README.md

By default, you may see colors for different types, e.g., gray for normal files and blue for directories. 

    aaa@YPB:~$ ll
    total 200
    drwxrwxr-x 5 aaa aaa  4096  3 15 03:13 ./
    drwxrwxr-x 5 aaa aaa  4096  3 14 01:18 ../
    -rw-rw-r-- 1 aaa aaa 22660  3 13 23:07 00_Preface-English.ipynb
    -rw-rw-r-- 1 aaa aaa 27503  3 13 15:22 00_Preface-Korean.ipynb
    -rw-rw-r-- 1 aaa aaa 16134  3 13 23:20 01_Installation.ipynb
    -rw-rw-r-- 1 aaa aaa  2184  3 15 03:13 01_LINUX_Shell.ipynb
    -rw-rw-r-- 1 aaa aaa 21730  3 13 23:48 02_Python_Basic.ipynb
    -rw-rw-r-- 1 aaa aaa 81065  3 14 03:19 03_Get_the_Taste.ipynb
    drwxrwxr-x 8 aaa aaa  4096  3 15 02:50 .git/
    drwxrwxr-x 2 aaa aaa  4096  3 14 22:43 html/
    drwxr-xr-x 2 aaa aaa  4096  3 15 02:51 .ipynb_checkpoints/
    -rw-rw-r-- 1 aaa aaa   342  3 14 00:03 README.md

Here, the directory or files start with `.` are the ones which are *hidden*. The first column means the permissions (see some manual for `chmod`). 

### Making and Editing a File

Let's make a test file:

    vi sample.txt

`vi` is a default editor. Hit `i` and type "hello". Hit `Esc`, and then colon (`:`). You will see the colon appeared at the bottom. Type "`wq`" and hit `Enter`. `wq` means write and quit. Then typing `ls` will show you a new file named "`sample.txt`".


Now let's move it to a new directory. You can type

    mkdir test         <--- make directory named "test"
    cd test            <--- go to that directory
    mv ../sample.txt . <--- move the "sample.txt" to here (.)
    pwd                <--- print your current location
    ls                 <--- show file list

You may want to rename or copy the file:

    cp sample.txt ..     <--- copy sample.txt to the higher directory
    cp sample.txt qq.txt <--- copy sample.txt to the higher directory with a new name "qq.txt"
    mv sample.txt pp.txt <--- move sample.txt as pp.txt, i.e., identical to "rename"!    

How can we remove `pp.txt` and the directory `test`?

    rm pp.txt    <--- remove pp.txt
    cd ..        
    rm -r test   <--- remove test directory

As you saw, to delete directory, you need an option "`-r`", which means "recursive". If you don't do so, you will get an error message 

    rm test
    rm: cannot remove 'test/': Is a directory



### Writing What You See on a File

You may frequently need a list of filenames. For example, you want to open FITS files "abc.fits", "def2.fits", ..., "zer0.fits", which have no clue on the naming. One way is to make a text file contains the file names, and load it from Python. Then, you can use for loop to open each file sequentially. 

    ls *.fits >> list.txt

Here, `*` means "any string", i.e., `ls *.fits` will list any file ends with `.fits`. `>>` means "add to", or "append to". That is, all the output of `ls *.fits` will be added to a file named `list.txt`. If there is no file named `ls *.fits`, it will automatically make it.
​    
    ls *.fits > list.txt
Test what happens when you use "`>`".

 

### Making a Script File

This is a very simple shell script which gets 2 arguments (example is from [here](http://www.macs.hw.ac.uk/~hwloidl/Courses/LinuxIntro/x984.html)). Copy the following and save it as `test.sh` file.

```bash
#!/bin/bash

# example of using arguments to a script
echo "My first name is $1"
echo "My surname is $2"
echo "Total number of arguments is $#" 
```

Then on the terminal,

```
$ chmod a+x name.sh
$ ./test.sh Hans-Wolfgang Loidl
```

You will see the output

```
My first name is Hans-Wolfgang
My surname is Loidl
Total number of arguments is 2
```

If you want, you can learn loops, etc.