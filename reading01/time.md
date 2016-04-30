TLDR - time
==========

Overview
--------
	
	time - time a process ("command")

	>>> time command  [ARGUMENTS]

EXAMPLES
--------
	
	- Measure the length of time for the command "date" -

		>>> time date
		> Tue Apr 12 05:29:40 EDT 2016
		> date  0.00s user 0.01s system 92% cpu 0.014 total

EXIT STATUS
-----------

     1-125   An error occurred in the time utility.

     126     The utility was found but could not be invoked.

     127     The utility could not be found.

     Otherwise, the exit status of time shall be that of utility.


Resources
---------

- [http://linux.die.net/man/1/time]

