# Introduction to the terminal

![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/DEC_VT100_terminal.jpg/1200px-DEC_VT100_terminal.jpg)

## Everything is a FILE

[**Everything** is a file](https://en.wikipedia.org/wiki/Everything_is_a_file).

Each file in your computer resides somewhere (in a directory), and each program in your computer is a file, hence, they live somewhere. You can know where they live, and make some programs yourself. But don't be afraid, the only thing you need is a file.

Each program has an specific input and an specific output. These are know as std_in and std_out. For instance, a text editor can have a text input from your keyboard and an output to a file. 

> Every program on your computer has the ability to do a vast amount of different things. Read files, start other programs, do math, control devices. The main difference between bash and most other programs is that unlike them, bash was not programmed to perform a certain task. Bash was programmed to take commands from you, the user. To do so efficiently, a "language" was created which allows users to "speak" to the bash program and tell it what to do. This language is the bash shell language and you are about to become intimately familiar with it.

> In essence, a shell program is one that provides users with an interface to interact with other programs. There is a large variety of shell programs, each with their own language. Some popular ones are the **C shell (csh), Z shell (zsh), Korn shell (ksh), Bourne shell, Debian's Almquist shell (dash), etc. Bash** (also called the Bourne Again shell) is currently the most popular and ubiquitously available shell. Even though all of these shells use seemingly similar syntax, it is important to be fully aware of what shell you're actually writing code for. Often, you'll hear people refer to their code as "shell code", which is about as specific as "source code" is when referring to your Java code. This guide will teach you how to write bash shell code: you should use it only with the bash shell, not any other.

!!! Note
    Probably [the best guide](https://guide.bash.academy/) to learn what this all means.

**TL;DR**
>  Bash is a simple tool in a vast toolbox of programs that lets me interact with my system using a text-based interface. 

### Useful commands

Getting to know eachother:

<p><a href="https://commons.wikimedia.org/wiki/File:Unix_history-simple.svg#/media/File:Unix_history-simple.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Unix_history-simple.svg/1200px-Unix_history-simple.svg.png" alt="Unix history-simple.svg"></a><br>By <a href="//commons.wikimedia.org/wiki/User:Eraserhead1" title="User:Eraserhead1">Eraserhead1</a>, <a href="//commons.wikimedia.org/wiki/User:Infinity0" title="User:Infinity0">Infinity0</a>, <a href="//commons.wikimedia.org/wiki/User:Sav_vas" title="User:Sav vas">Sav_vas</a> - <a rel="nofollow" class="external text" href="http://www.levenez.com/unix/history.html">Levenez Unix History Diagram</a>, <a rel="nofollow" class="external text" href="http://www.ibm.com/developerworks/library/it-schenk1/schenk3.html">Information on the history of IBM's AIX on ibm.com</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=1801948">Link</a></p>

#### WINDOWS specific

- `dir` - To view the contents of a directory, type "dir"
- `del` - Subsequently, you might want to clean up useless files
- `clip` - copy the output

#### UNIX specific

- `ls` - list files in a folder
- `rm <filename>` - delete files. Be careful, it won't ask for confirmation and they won't be in the Trash!!
- `pbcopy` - copy the output

#### All

- `cd <dir>` - It is frequently useful to know in which directory you are currently working To move between directories, use the cd command with the name of a directory example go to desktop  is "cd Desktop"
- `cd ..` go up a directory
- `open <file>` open a file with the default 
- `mkdir <filename>`  - To create a new directory
- `pwd` - print name of current/working directory
- `ls --help` - show help of ls command.
- `ls -a` - list files in a folder (including hidden).
- `ls -l` - show long listing format.
- `man ls` - Format and display the on-line manual pages.
- `mv [-f | -i | -n] [-v] source target` - _change name_ or _move file_ (basically the same)
- `cat <file>` - outputs file into `std_out`

### Redirection and pipelines

We can redirect the `std_out` of a command to a specific target. Most commonly, this will be a file.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Portugal_pipeline.jpg/1200px-Portugal_pipeline.jpg)

#### Basic redirection and appending

- `echo "Hello" > file.txt`: Says hello, but redirects the output to a file (file.txt). Creates a new file
- `echo "Hello" >> file.txt`: Says hello, but redirects the output to a file (file.txt). Appends it to the file

#### Pipeline

Pipelines are meant for command to command communication.

- `pwd|pbcopy`: send the output of *pwd* command to the input of another command, in
- `ps -ax|grep 'python'`: send the output of ps -ax (list of open processes) and only grab the ones that contain python in them

### In terminal applications

**VI(M)**
Screen-oriented text editor originally created for the Unix operating system. 

!!! note "Basic commands"

    - Edit a file: type `i` - > INSERT MODE
    - Exit INSERT MODE: press `Esc`
    - Quit. Out of any mode: type `:q`
    - Write and quit. . Out of any mode: type `:wq`
    - Dont' write and quit. Out of any mode: type `:q!`