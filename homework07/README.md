Homework 07
===========

dd.py
-----
1. 
I handled the command line arguments using the sys.argv variable, which passes all the of the command
line arguments to a list. Once I have the arguments in a list, I could split the contents of the 
list at the '=' signs, using str.split(). Once that was done, it was easy to parse the arguments using
a simple for loop.

2. 
I opened the source files in read-only mode, and the output files in write-only mode. I also set the code
up so that if the output file does not exist, it will be created.

3. 
The SEEK and SKIP commands needed to be implemented once, before any writing was done. So, I implemented them
immidietly after the file streams were opened. A file descriptor is opened, and then lseek() sets the begin position
to the one specified. If no SEEK or SKIP values are specified, the position is set to the beginning by default. If the file stream is not specified, then the file stream will be STDIN or STDOUT, and lseek() will not be called, which is convenient because you cannot actually lseek() on stdin/out.

4. 
COUNT - this was simple to implement. The actual data processing happens within the classic while loop, "while data:".
This means the program will continue to data process, until there is no more data. Each time it processes, it manipulates a data block of size "BS". I modified the while loop so that it will exit if the data reaches EOF, OR, if the number of times it has written a "BS"-sized block exceeded the COUNT number.

BS - I simply specified explicitly that the data should be processed BS bytes at a time using 


find.py
-------
1. 
I handled the command line arguments the same way I handled them in the last script. I simply set a variable equal to sys.argv and then parsed it.

2. 
I walked the directory tree using the instructions from class. I also included a section that will possibly include the root directory itself, if it satisfies the arguments set by the user.

3. 
I decided whether or not to print a file using my "include" function. It goes through each of the possible arguments, and, if an argument has been entered, it sees if a file has met the requirements of that argument.

4. 
strace -c ./find.py /etc
	stat = 41,563 calls
	lstat = 22 calls
strace -c find -L /etc
	stat = 21,792 calls
	lstat = 13 calls

Find is "missing" around 20,000 stat calls. After investigating the man pages, I discovered this:
"Use of this option [The "-L" option] implies -noleaf"

I then researched noleaf and found that it causes find to function thus:
"When find is examining a directory, after it has statted 2 fewer subdirectories than the directory’s link
count ["Because this count includes "." and "..", so these are ignored], it knows that the rest of the entries in the directory are non-directories (‘leaf’ files in the directory tree). If  only the files’ names need to be examined, there is no need to stat them;  this  gives a significant  increase  in search speed."

