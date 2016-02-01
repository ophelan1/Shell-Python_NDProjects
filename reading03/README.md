Reading 03
==========
1.
	strace ls

2.
	ldd /bin/ls

3. 
	strace -e open ls

4.
	gdb hello-debug

5. 
	valgrind --leak-check=yes hello-debug

6. 
	gprof hello-profile
	subl gmon.out
	### My preferred text editor is sublime text ###
