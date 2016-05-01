Homework 01
===========

Paths
-----
1. cd /afs/nd.edu/user14/csesoft
2. cd ./csesoft
3. cd ~/../csesoft
4. ln -s /afs/nd.edu/user14/csesoft ./csesoft

Copying, Moving, Removing
-------------------------
1. cp /usr/share/pixmaps ~/images
2. file ./* | grep link
	After copying the "pixmpas" folder to the "images" folder and running the above command while in the "images" folder, I learned that all but one of the symbolic links in my "images" directory are broken. Next to these links, "file" prints out:
	> ./redhat-programming.png:          broken symbolic link to `../icons/System/48x48/apps/redhat-programming.png'
	They are broken because they are on a relative path. My parent directory does not contain an "icons directory"
3. time mv ./images ./pixmaps
4. Yes it is. Because the computer has to load the $USER variable from memory
5. rm -r /tmp/$USER-pixmaps

Files and Directories
---------------------
1. ls -lh /afs/nd.edu/user37/ccl/software
2. ls -lt /afs/nd.edu/user37/ccl/software
3. find /afs/nd.edu/user37/ccl/software/cctools/x86_64 -type f | wc   				( 2215 - It is the first number )
4. ls -l /afs/nd.edu/user37/ccl/software/cctools/x86_64| grep weaver
5. du -csh /afs/nd.edu/user37/ccl/software/cctools/x86_64/* | sort -nr  			(redhat5 is 82 megabytes)
6. find /afs/nd.edu/user37/ccl/software/cctools/x86_64/redhat5 -type f | wc   	( 898 )
7. du -ah /afs/nd.edu/user37/ccl/software/cctools/x86_64 | sort -nr | head -n 1 	(1006K	/afs/nd.edu/user37/ccl/software/cctools/x86_64/redhat5/bin/chirp)
8. find /afs/nd.edu/user37/ccl/software/cctools/x86_64 -type f -mtime +30 | wc    ( 534 )

Unix Permissions
----------------
1. User can read write and execute, group can read and execute, others can only execute.
2. 
	a. chmod 711 data.txt
	b. chmod 770 data.txt
	c. chmod +r data.txt
	d. chmod 000 data.txt
3. Root User

AFS Permissions
---------------
1. Use the fs listacl command to view the ACLs on your home directory, your Private directory, and your Public directory. What are the differences in the ACLs for those three folders and what do those differences mean?

	Access list for /afs/nd.edu/user29/ophelan1 is; Normal rights:; system:anyuser l
		- Any other user can see the files in my home directory, but not read them. 

	Access list for /afs/nd.edu/user29/ophelan1/Public/ is; Normal rights:; system:anyuser rlk
		- Any other user can see, read, and lock the files in Public.

	Access list for /afs/nd.edu/user29/ophelan1/Private/ is; Normal rights:
		- There are no access rights granted to other users.

2. Permissions are 777, everyone has full read, write, and execute permissions
	> touch: cannot touch `/afs/nd.edu/common/ophelan1.txt': Read-only file system
	The afs file system is a read-only system, which means I cannot create a new file, even if I have write permissions.

3. fs setacl /path/to/directory <instructor_username> <perms (i.e. all)>

Masks
-----
-rw-rw-rw- 1 ophelan1 dip 0 May  1 01:36 world1.txt
-rw-r--r-- 1 ophelan1 dip 0 May  1 01:37 world2.txt
-rw--w--w- 1 ophelan1 dip 0 May  1 01:37 world3.txt

1. They are not the same. Umask sets the permissions that should be applied to created files. Since I set a 
different umask before creating each file. The permissions are different. This can be helpful when creating 
a lot of files with specific permissions, because you do not have to manually go through and change all of them. 
