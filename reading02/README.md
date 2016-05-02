ENTIRE ASSIGNMENT SUBMITTED LATE

Reading 02
==========
1. Capture the output of the uname command to a file called uname.txt.
		>>> uname > uname.txt

2. Find out the IP address of the local machine.
		>>> ifconfig | less

3. Find out the IP address associated with a domain name.
		>>> nslookup URL

4. Check if a machine is responsive (reachable via the network).
		>>> ping IPADDRESS

5. Securely transfer a file from between two machines. [ Transfer SAMPLE.txt to the current directory ]
		>>> scp ophelan1@student00.cse.nd.edu:/some/path/to/SAMPLE.txt /path/to/current/directory

6. Execute a persistent shell session that you can detach and then re-attach. [better to give it a name instead of just typing"tmux"]
		>>> tmux new-session -s NAME

7. Download a file from a website.
		>>> curl URL

8. Scan a remote machine to see what ports are open [student01]
		>>> nc -z -v student01.cse.nd.edu 1-1023


