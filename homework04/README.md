Homework 04
===========
1. 
	a. My computer, and the student machine, did not have default values for the enviornmental variables. I added all the neccesary variables using $ import VARNAME=VARVALUE. This is important because if I were to simply set variables within the script, they would not remain once the script finishes.

	b. To find all the files with the given EXTENSIONS I used pngs. I also could have used a pattern matching while loop, but pngs seemed easier and this way it will not output an error message if there are no files, only if there is an error.

	c. When VERBOSE==1, an "if" statement triggers and the script runs "set -v"
	d. When running a command, there is an output option if the command fails. "CMD || FailureCMDs." If the compile command fails, then the program instead prints an error message and exits.

2. When a makefile runs, it only compiles differences. This is ideal for large programs because it will not recompile huge files every time. However, makefiles offer a lot less control and response to variables. Shell scripts offer lot's of control and can help with debugging because you can personalize output options. However, when a shell script runs, it must recompile all the files every time. Personally, I am not working on any huge projects, making the benefit of Makefiles void. Ergo, shell scripting is the best option available to me. 
