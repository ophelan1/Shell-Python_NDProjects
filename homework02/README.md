Homework 02
===========

Questions
-------------
source - student00.cse.nd.edu
target - student01.cse.nd.edu


1
----------
# Create workspace on source machine (WHILE LOGGED ONTO STUDENT00 / STUDENT01)
/tmp/${USER}-workspace

# Create the Random Data File
dd if=/dev/urandom of=random10MB.txt count=10K bs=1K

# Create a Hard Link to the Files:
ln random10MB.txt ./link1


2
----------
Student00
Input: du -h
Output: 11M
The disk usage is not suprising. The folder contains a 10M file and 10 links to the same 
adress in memory. Including the sftpHelper file, added up it is not suprising the folder takes up 11M. 

#Although this is not 10MB, the dd command could easily be modified to read: "count=10KB bs=1KB." 
#My data is simply in powers of 1024 bytes instead of powers of 1000. I realized this mistake after #creating and transferring all the links. I hope that's okay!


3
----------
Student01
Input: du -h
Output: 101M
It takes up around 9x as much space. Which WOULD be suprising, if I had not skipped ahead to question 4.
When scp or sftp transfer links, they actually transfer the data file that the links refer to. In our case that is the 10M random file. So 10 links, each referencing the same 10M file, comes to around 100M. Not too far off.  


4
----------
scp:
scp ./link* ophelan1@student01.cse.nd.edu:/tmp/${USER}-workspace 


sftp:
sftp ophelan1@student01.cse.nd.edu < stfpHelper.txt

	sftpHelper.txt:
	mput link*

	#Cannot find a way to get around the password having to be entered. Program prompts and then waits.


rsync:
rsync ./link* ophelan1@student01.cse.nd.edu:/tmp/${USER}-workspace.


5
---------
Every time you use scp or sftp, the entire data file is sent. It does not matter if that file was already
present. When using rsync, only the changes to a file are sent. This feature makes things like mirroring
(without it, all the data in the computer would have to be sent each time), and backing up (without it, every file to be backed up would have to be resent each time).

6
---------
On networks I know and trust, rsync is easy and the most efficient option. But it is not secure.
Generally I like the idea of my data being hidden from strangers so I would go with sftp.


