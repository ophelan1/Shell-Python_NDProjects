Homework 02
===========

Part 1
=========
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

PART 2
=========

1. Scan for open ports.
	
	Input: nmap -sV -A -Pn -T4 xavier.h4x0r.space
	Output: 

Not shown: 946 filtered ports, 50 closed ports
PORT     STATE SERVICE           VERSION
22/tcp   open  ssh               OpenSSH 7.1 (protocol 2.0)
8888/tcp open  sun-answerbook?
9111/tcp open  DragonIDSConsole?
9876/tcp open  sd?

There are 2 open ports in the 9000-10000 range. 

2. Check HTTP Files
#I couldn't figure out how to do this at first so I just loaded xavier.h4x0r.space:9876 into 
#Chrome and that worked well enough. Changed my answer once I read the hints. 

	Input: curl xavier.h4x0r.space:9876
	Output:
 _________________________________________ 
/ Halt! Who goes there?                   \
|                                         |
| If you seek the ORACLE, you must query  |
| the DOORMAN at /{netid}/{passcode}!     |
|                                         |
| To retrieve your passcode you must      |
| decode the file at                      |
| ~pbui/pub/oracle/${USER}/code using the |
| BASE64 command.                         |
|                                         |
\ Good luck!                              /
 ----------------------------------------- 
    \                                  ___-------___
     \                             _-~~             ~~-_
      \                         _-~                    /~-_
             /^\__/^\         /~  \                   /    \
           /|  O|| O|        /      \_______________/        \
          | |___||__|      /       /                \          \
          |          \    /      /                    \          \
          |   (_______) /______/                        \_________ \
          |         / /         \                      /            \
           \         \^\\         \                  /               \     /
             \         ||           \______________/      _-_       //\__//
               \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
                 ~-----||====/~     |==================|       |/~~~~~
                  (_(__/  ./     /                    \_\      \.
                         (_(___/                         \_____)_)


    
3. Decode my Password 

	Input: base64 -d ~pbui/pub/oracle/${USER}/code
	Output: 2504ee32b0a53bde19ccc85e44a0322c

4. Speak to the Doorman
	
	Input: curl xavier.h4x0r.space:9876/ophelan1/2504ee32b0a53bde19ccc85e44a0322c
	Output:

 _________________________________________
/ Ah yes, ophelan1... I've been waiting   \
| for you.                                |
|                                         |
| The ORACLE looks forward to talking to  |
| you, but you must first retrieve a      |
| secret message from the SLEEPER.        |
|                                         |
| He can be found in plain sight at       |
| ~pbui/pub/oracle/SLEEPER... You will    |
| need to wake him up and then signal him |
| to HANGUP his connection. If he         |
| recognizes you, he will give you the    |
| message in coded form.                  |
|                                         |
| Once you have the message, proceed to   |
| port 9111 and deliver the message to    |
| the ORACLE.                             |
|                                         |
| Hurry! The ORACLE is wise, but she is   |
\ not patient!                            /
 -----------------------------------------
  \
   \   \
        \ /\
        ( )
      .( o ).


5. Speak to the Sleeper 

	Input: ~pbui/pub/oracle/SLEEPER
	Output:
 _______________________________
< Uh... What? What do you want? >
 -------------------------------
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/

 ___________________________________
/ Ugh... I'm going back to sleep... \
\ ZzZzZ...                          /
 -----------------------------------
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/

6. Sleeper, Take 2

	Input: ps -ua | grep SLEEPER
	Output: 
ophelan1 29966  0.0  0.0 107332  1236 pts/19   S+   09:45   0:00 /bin/sh /afs/nd.edu/user15/pbui/pub/oracle/SLEEPER
ophelan1 29977  0.0  0.0 103252   812 pts/5    S+   09:45   0:00 grep SLEEPER

	Input: kill 29966
	Output: 

 _______________________________________
/ WTF are you trying to do here?        \
| Terminate me?                         |
|                                       |
| Get lost, ophelan1! I'm going back to |
\ sleep!                                /
 ---------------------------------------
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/


7. Sleeper, Take 3
	
	Input: kill -9 5988
	Output: (NOTICE THE "KILLED")
	 _______________________________
< Uh... What? What do you want? >
 -------------------------------
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/

Killed

8. Sleeper, Take 4

	Input: kill -1 7106 (FINALLY get what the HANGUP word was in there for)
	Output:

 ________________________________________
/ Hmm... I recognize you ophelan1...     \
| Here's the message you need to give to |
| the ORACLE:                            |
|                                        |
\ YmN1cnluYTE9MTQ1NDA4MTM1Nw==           /
 ----------------------------------------
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/
 
 9. 

 	Input: nc xavier.h4x0r.space 9111
 	Output:

 ________________________
< Hello, who may you be? >
 ------------------------
       \   \_______
 v__v   \  \   O   )
 (oo)      ||----w |
 (__)      ||     ||  \/\

NAME? ophelan1
 ___________________________________
/ Hmm... ophelan1?                  \
|                                   |
| That name sounds familiar... what |
\ message do you have for me?       /
 -----------------------------------
       \   \_______
 v__v   \  \   O   )
 (oo)      ||----w |
 (__)      ||     ||  \/\

MESSAGE? YmN1cnluYTE9MTQ1NDA4MTM1Nw==
 ______________________________________
/ Ah yes... ophelan1!                  \
|                                      |
| You're smarter than I thought. I can |
| see why the instructor likes you.    |
|                                      |
| You met the SLEEPER about 11 minutes |
\ ago... What took you so long?        /
 --------------------------------------

