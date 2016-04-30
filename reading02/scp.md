TLDR - scp
==========

Overview - secure copy (remote file copy program)
--------

scp [-pqrv] [-P port] [ ophelan1@studentXX.cse.nd.edu:/path/to/file ] [/path/to/local_directory]

Examples
--------

- Copy the file "hello.txt" from the machine "student00" to the local machine 
	>>> scp ophelan1@student00.cse.nd.edu:./testfiles/hello.txt /Users/Owen/tests/hello.txt

[ -r ] Copy All items in a directory, Including subdirectories and their contents
	>>> scp -r ophelan1@student00.cse.nd.edu:./testfiles/hello.txt /Users/Owen/tests/hello.txt

[ -q ] Enable quiet mode, no progress bar or warning messages.
	
[ -v ] Verbose mode, print bugging pages.



Resources
---------

[ Linux Man-Pages ]
