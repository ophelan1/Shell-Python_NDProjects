TLDR - tail
==========

Overview
--------

tail prints the last couple lines (default = 10) of each FILE to standard output.

Examples
--------

-Standard Use of tail-
	tail FILE

-Different Number of Output Lines (15)-
	tail -15 FILE

-Multiple FIles-
	tail FILE1 FILE2

-Output Less Than Default = 10 -
	tail -n 5 FILE1 FILE2

-Display only the last given number of bytes-
	tail -c 20 FILE1

