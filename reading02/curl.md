TLDR - curl
==========

Overview - transfer data from or to a server
--------

curl [Options] [URL...]

Options
--------

- Get the contents of a URL and print it to stdout 
	>>> curl URL

[ -o ] Get the contents of a URL and store it in a file 
	>>> curl URL > FILE.ext
	>>> curl -o FILE.ext URL 

[ -L ] Follow redirects (i.e. for when a site has moved)
	>>> curl -L google.com
	
[ -v ] Verbose mode, print bugging pages.

[ -trace ] SUPER verbose mode



Resources
---------

[ Linux Man-Pages ]
