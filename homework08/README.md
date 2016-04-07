Homework 08
===========

timeout.py
----------
1. Parent - Sets an alarm using signal.alarm(TIME), And then waits for the child process to finish
			   If the alarm goes off, the signal is caught, and the child is killed with SIGINT
   Child  - The child runs the actual command itself, by using the system call os.execvp(Command, CMD).

2. signal.signal(signal.SIGALRM, alrm_handler) was used to catch the alarm set by the parent. When the 
	alarm goes off, the child is killed using os.kill(os.getpid(), 15). The parents "wait()" function 
	then recieves this kill signal into it's variable "status".

3. The test script verifies my program by giving different sleep commands to timeout.py. If the sleep 
	value is larger then the set time value, the program should fail, because the alarm should signal
	before the sleep command is finished. If the sleep value is smaller, the sleep command should run
	and exit succesfully.

4. When I run "find.py -t 2 sleep 2" I get the same result each time - Failure. (I did not write a shell script 
	because it was honestly faster for me to take 10 minutes to run it repeatedly) This makes sense because
	when i debug, it is clear that the parent function executes first each time. This means that the alarm 
	begins it's countdown moments before the sleep command is executed. Therefore, the alarm will always be
	triggered before the sleep command runs it's course. 

rorschach.py
------------
1. I decided not to use OS.walk, just because it's a lot easier to handle variable without it. So I created
	a list of directories from the input, and then iterated through it using itDir(). Within itDir, I iterate
	through each of the files using itFiles. THEN, (if the file being considered was newly modified), I
	iterate through each of the rules using itRules(), and see if the file name matches the pattern for each rule.

2. I loaded the rules using the function loadRules(). This function opens the specified file stream (in my case,
	a file I created based on the sample file called '.rorschach.yml'). Then, it uses yaml.load() to pass the rules
	into a list of dictionaries. After that, it was simply a matter of looping through the dictionary, and setting
	pattern = the key for 'pattern', and action = the key for 'action', when I wanted to check files against the pattern,
	and execute the action if the file is a match.

3. As I iterated through each file, I created a variable called new_time. If that variable >= START_TIME, that means
	the file was created or modified after the program began. So, if that is the case, the program then iterates through
	the rules and sees if the file matches the pattern. The only issue with this is that, if the file was created after
	START_TIME, it will be reconsidered every single time the program reiterates through the files. To get around this, 
	I update START_TIME every time it iterates through all the files. That way, if a file is newly created, then it will 
	be affected by the rules once, and then next time the program loops through, it's "new_time" will HAVE to be less than
	the new START_TIME, and so it will not be considered. 

4. I executed each action using os.execvp(Action[0], Action). The 'Action' variabel is a list (the format execvp accepts)
	obtained using the shlex.split(dictItem['action'].format(...) command. The section of code within format(...) ensures that
	if the action requires the fullname, it will get the full name, and if it asks for the basename, it will get the basename. 

5. 
	1. The "busy waiting" problem is related to the fact that rorschach is constantly checking to see if a condition is true. 
		This wastes a lot of time and processing power, especially if the sleep value is very small, because this means a lot of checking and rechecking. An alternative would be to increase the sleep time. Or, one could set an alarm on the specified directories, 
		which sends a signal when a change has been made in that directory. This would mean that rorscach would only have to 
		check it's conditions when a change has been made, not continually.
	2. I am unsure why cache invalidation would be a problem for rorschach. 