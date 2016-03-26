Homework 07
===========

dd.py
-----
I handled the command line arguments using the sys.argv variable, which passes all the of the command
line arguments to a list. Once I have the arguments in a list, I could split the contents of the 
list at the '=' signs, using str.split(). Once that was done, it was easy to parse the arguments using
a simple for loop.

I opened the source files in read-only mode, and the output files in write-only mode. I also set the code
up so that if the output file does not exist, it will be created.

The SEEK and SKIP commands needed to be implemented once, before any writing was done. So, I implemented them
immidietly after the file streams were opened. A file descriptor is opened, and then lseek() sets the begin position
to the one specified. If no SEEK or SKIP values are specified, the position is set to the beginning by default. If the file stream is not specified, then the file stream will be STDIN or STDOUT, and lseek() will not be called, which is convenient because you cannot actually lseek() on stdin/out.

COUNT - this was simple to implement. The actual data processing happens within the classic while loop, "while data:".
This means the program will continue to data process, until there is no more data. Each time it processes, it manipulates a data block of size "BS". I modified the while loop so that it will exit if the data reaches EOF, OR, if the number of times it has written a "BS"-sized block exceeded the COUNT number.

BS - I simply specified explicitly that the data should be processed BS bytes at a time using 


find.py
-------
I handled the command line arguments the same way I handled them in the last script. I simply set a variable equal to sys.argv and then parsed it.

I walked the directory tree using the instructions from class. I also included a section that will possible include 
the root directory itself, if it satisfies the arguments set by the user.

I decided whether or not to print a file using my "include" function. It goes through each of the possible arguments, and, if an argument has been entered, it sees if a file has met the requirements of that argument.

Did not have enough time to answer the last question.
NOTE: It is really frustrating having a test file that says I did not pass a certain part, without telling me why. I have been struggling for LITERALLY 5 hours on only a couple of the arguments (perm specifically), because the test fails, but I have no idea why. I am printing out MOST of everything the normal find function does, but not all of it. I have no idea why it is only partially working, and so it is really difficult to find out exactly the problem. 