REGRADING CHANGES:
	1. README - Q6 Corrected
	2. ln.md, ls.md, ps.md - Updated
	3. kill.md, write.md, time.md - Newly Created

Reading 01
==========

1. To create a file only viewable by me I would enter the following into the terminal:

subl private.txt 			//My text editor of choice is SublimeText2
chmod 700 private.txt       //The 7 allows me full permission to read write and  								//execute, and the following two 0's deny access to 								//groups and the world.



2. To create a link to the cse20189.01 directory:

ln -s /afs/nd.edu/coursesp.16/cse/cse20189.01 link 		//Creat a link called "link"



3. To determine the size of file named "BigFile":

ls -lh BigFile				//More user friendly output then [ls -l]
du BigFile					//Even more user friendly



4. To determine the size of a directory named "MyFolder":

du MyFolder					//Gives the size of MyFolder
ls -lh MyFolder				//Gives the size of the folder and the contents



5. To end the process "ssh student00":

kill 25263



6. To terminate the "urxvt" process:

ORIGINAL SUBMISSION: kill 25129
RE-GRADE SUBMISSION: kill 25129 25913




7. To determine the time it takes to run "simulation"

time simulation



8. To set my default text editor:

export VISUAL=subl
export EDITOR="$VISUAL"


