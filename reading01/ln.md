TLDR - ln
==========

Overview
--------

[ln (modifier) (target of link) (new link name)] makes links between files. 


Examples
--------
-Create A Hard Link-
	
	>>> ln /full/path/of/original/file /full/path/of/hard/link/file

-Create A Soft Link-

	>>> ln -s /full/path/of/original/file /full/path/of/soft/link/file

-Remove the links already on the page-
	
	>>> ln -f /full/path/of/original/file

-Specify the directory in which to create the links-
	
	>>> ln -t  /full/path/of/original/directory 


Resources
---------

- [Linux Man Pages](http://man7.org/linux/man-pages/man1/ln.1.html)

