TLDR - kill
==========

Overview
--------
	
	kill - terminate a process

	>>> kill [-s SIGNAL] PID

Examples
--------
- List all the possible signals -

	>>> kill -l

	> HUP INT QUIT ILL TRAP... 

- Specify the Signal to Send -

	>>> kill -s SIGNAL PID

- Print the pid, do not send signal - 

	>>> kill -p PID



Resources
---------

- [http://linux.die.net/man/1/kill]

