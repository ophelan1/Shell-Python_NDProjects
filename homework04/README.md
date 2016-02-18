Homework 04
===========
Activity 1
----------
1. 
	a. My computer, and the darrow machine, did not have default values for the enviornmental variables. I added all the neccesary variables using $ import VARNAME=VARVALUE. This is important because if I were to simply set variables within the script, they would not remain once the script finishes.

	b. To find all the files with the given EXTENSIONS I used pngs. I also could have used a pattern matching while loop, but pngs seemed easier and this way it will not output an error message if there are no files, only if there is an error.

	c. When VERBOSE==1, an "if" statement triggers and the script runs "set -v"
	d. When running a command, there is an output option if the command fails. "CMD || FailureCMDs." If the compile command fails, then the program instead prints an error message and exits.

2. When a makefile runs, it only compiles differences. This is ideal for large programs because it will not recompile huge files every time. However, makefiles offer a lot less control and response to variables. Shell scripts offer lot's of control and can help with debugging because you can personalize output options. However, when a shell script runs, it must recompile all the files every time. Personally, I am not working on any huge projects, making the benefit of Makefiles void. Ergo, shell scripting is the best option available to me. 

Activity 2
----------
1.
	a. I passed the command line arguments using getopts and shift. Until it reaches the last flag, the getopts while loop will continue to take a flag as input, assign that flag according to the case structure, then shift to the next flag. Once all the flags are exhausted, the directory will be the first argument. So, the position of OPTIND is shifted so that it now corresponds to the first arguemnt. The directory name is then assigned using $@.
	b. The case where there are no command line arguments takes care of itself when I use a while loop with getopts. Once the while loop triggers, getopts immidietly will return 0, because there are no flags, and the while loop exits. Then, the script shifts the input, as it would have if there HAD been arguemnts, and assigns the variable directory. Each time the script runs, it sets the values of the 
	possible flags to their defaults ("" for flag1, 10 for flag2), so that they will hold their default values if no argument is passed.
	c. The program naturally handles more than one directory input because du can accept more than one directory input. All one has to do is set $directory = "THE STRING OF ALL DIRECTORIES ENTERED". This is done by setting directory=$@ (when the index of OPTIND is set to the position of the first argument). When the program is done accepting options, it does one final "getopts" before accepting a directory as input, returning 0 and exiting the while loop. This means the index has been shifted one more to the right than it should be, thus ($OPTIND - 1) is the position of the first directory. So if we set directory equal to argv[ $(($OPTIND-1)) ] then it will be equal to the string of non-option arguments that begins after the flags are finished. That is, it will be equal to the string of directory names.
	d. When getopts is set up, it is given a list of expected options (i.e. :an:h). If any of these options are followed by ":" (i.e. "n:"), then getopts will expect an argument along with this option. In our case, that argument is how many rows to display. When getopts comes across an option like this, it stores the accompanying argument in a variable called $OPTARG. By setting flag2=$OPTARG when getopt detects -n, we are setting flag2 ("N") equal to the argument which follows -n, that is, the number of rows to display. 
2. The hardest part of this program was debugging. Because it is a shellscript, and not an actual program with error warnings and debug tools, disk_usage would often terminate with cryptic messages as to what the issue is. Even using "set -x" and "set -v" didn't really help. The test program also did not help with debugging except to say "it worked!" when it actually hadn't. In addition, most of the research I do for these homeworks I do on google, and because there are not many people out there who still write shell scripts for the Bourne Shell, there was not much syntactically-correct help available. I am not sure what is meant by the "took up the most amount of code." In my script, each block of code (cleanup(), getopt, and shift) is about five lines. 


Activity 3
------
1.
	a. I handled the different signals using "trap." Although this did not work for the taunt_test.sh file, I believe this is because taunt_test sends kill commands uses kill, which depends on PID, and not pkill, which depends on the name of the process. When I sent the signals myself using "pkill" the signals were interpreted correctly.
	b. I used piping to pass a message to cowsay. Fairly self explanatory, the output of the "cout" is passed to "cowsay"
	c. The timeout handles itself using the "read" command. Although "read" will pass an input to the variable "input," nothing is done with this variable. Rather, the read command is used with the "-t" flag, so that after 10 seconds it will return an error, and wthe script will instead print the message. 
2. It depends on what needs to be done. If a very simple set of commands needs to be run, a shell script is easier than a C-program. If a complicated program needs to run with multiple inputs and variables, then a C program is easier and has a greater range of functions. 
