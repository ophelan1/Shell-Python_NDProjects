Homework 03
===========

Activity 1 - Makefile
---------------------
Given the following pairs of files, identify which one of the two is larger and discuss why:

a. libgcd.a vs libgcd.so
	libgcd.a - 1.4K, libgcd.so - 5.6K

	"libgcd.a" is a static library, and so it only needs to be accessed when compiling, not at run time. So it is 
	archived, which saves space. "libgcd.so" is a shared library, so it is accessed at run time. Therefore it is not
	archived, and so is larger.

b. gcd-static vs gcd-dynamic
	gcd-static - 743K, gcd-dynamic - 7.2K

	"gcd-static" was compiled using a static library. This means that the code from the library neccesary for the program to run is copied into the executable, making the executable much larger. "gcd-dynamic" uses a shared library, which means that it calls on the library when it needs it, but does not copy the code itself. Thus, it is smaller. 

What libraries does gcd-static depend on? What libraries does gcd-dynamic depend on? How did you find out?
	
	GCD-DYNAMIC: libgcd.so, libc.so.6
	GCD-STATIC: Does not depend on any libraries
		I ran >>> readelf -d ./gcd-dynamic

Try to run the gcd-dynamic application. Did it work? Why or why not? Which environment variable could we set to allow gcd-dynamic to execute and what would we set it to?
	
	It did not work. Even though the program compiled, in order to use the gcd library at run time, it must know where
	to find that library. The library seach path for Unix is LD_LIBRARY_PATH. To change this variable, you can run:
	>>> setenv LD_LIBRARY_PATH /path/to/dir/with/library:$LD_LIBRARY_PATH. 
	(On the student machines, it is not a variable, so you must instead edit the contents of /").

What are the advantages and disadvantages to static and dynamic linking? If you were to create an application which type of executable would you want to produce by default? Explain your choice and discuss your reasoning.

	Linking dynamically reduce the amount of code in each binary that uses a library, because the library code itself does not have to be loaded until run-time. This is especially important when a library is used frequently with many different programs on a systed. This means that every time a library component is called, it must be loaded into memory, which causes a reduction in speed of execution.

	Static linking copies all of the neccesary library components into the binary. This means that you do not need the library itself at runtime. In addition, because the code is already in memory, there is no delay. However, it also means that the binary's are much larger because they need to include all of the necesary library code that is called. 

	If I were to create an application I would link it statically. Every system has a different file system layout. Therefore, it is much safer to include the libraries in the application itself, rather then trying to link the libraries on every machine. In addition, the application would run faster. 

Activity 2 - Fix It
---------------------
How did you download and extract the is_palindrome.tar.gz archive? What commands did you use?

	>>> curl https://www3.nd.edu/~pbui/teaching/cse.20189.sp16/static/tar/is_palindrome.tar.gz > ./is_palindrome.tar.gz
	>>> tar -zxvf is_palindrome.tar.gz

What flags did you use to force gcc to include debugging symbols in the is_palindrome executable? How does including these symbols affect the size of the executable? Explain and provide evidence.

	"-g -O0" are the flags I used. 
	is_palindrome - WITH debug - 9.0K
	is_palindrome - WITHOUT debug - 8.6K

	The executable WITH debugging is larger because the executable has a list of memory addresses, and the variables
	they correspond to within the code.

For each of the three classes of bugs, describe how you diagnosed the problem, what the problem was, and how you fixed it. Be sure to explain the commands you used to track down the bugs and why your modifications address the issues you found.

	For all 3 bugs, I used valgrind.
	>>> valgrind --tool=memcheck --leak-check=yes example1

	1. Segmentation Fault
		CODE   		  : fgets(buffer, BUFSIZ, stdin)
		SOLUTION		  : char *buffer = "" ### => ### char buffer[BUFSIZ]

	2. Invalid Memory Access 
		CODE   		  : char *sanitized = malloc(strlen(s));
		SOLUTION		  : malloc(strlen(s)) ### => ### strdup(s);
						  : (in main...) >>> free(sanitized);

	3. Invalid Read: Invalid read of size 1
		ERROR LOCATION: (is_palindrome.c:27) (is_palindrome.c:45)
		CODE 			  : const char *back  = s + strlen(s);
		SOLUTION		  : s + strlen(s) ### => ### s + strlen(s) - 1


Of the bugs you found and fixed, which one was the hardest? Discuss why that bug was so difficult for you and what can be done in the future to prevent such bugs.

	The hardest bug for me to crack dealt with the memory allocation of my sanitized string. (char *sanitized = strdup(s);). The reason it was so difficult, was because my error message did not referene that section of the code. Rather, because that section of the code was outputting an incorrect variable, the error only showed up later when that variable was passed to the next function. In future, I think I will try to include regular checks in the code, which print out variables and their types, so I can keep track of what each function is outputting.


1. strace /afs/nd.edu/user15/pbui/pub/bin/COURIER - "Are you sure you put the package in the right place"
		> Found in code: stat(/tmp/ophelan1.deaddrop)
		>>> echo "test" > /tmp/ophelan1.deaddrop
		>>> strace /afs/nd.edu/user15/pbui/pub/bin/COURIER

2. strace /afs/nd.edu/user15/pbui/pub/bin/COURIER - "Whoa whoa... you can't give everyone access to the package! Lock it down!"
		> Found in code: {st_mode=S_IFREG|0711, st_size=5, ...})
		>>> chmod 0700 /tmp/ophelan1.deaddrop
		>>> strace /afs/nd.edu/user15/pbui/pub/bin/COURIER

3. strace ... - "What are you trying to pull here? The package is the wrong size!"
		> Found in code: read(3, "test\n", 8)
		>>> nano /tmp/ophelan1.deaddrop [ change to a 8char string, (8 bytes)]
		>>> strace...

3. "Well, everything looks good... I'm not sure what 'abcdefgh' means, but I'll pass it on."







