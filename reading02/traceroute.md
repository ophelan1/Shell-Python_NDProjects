TLDR - traceroute
==========

Overview -  When you send packets to a domain, print the route packets take to network host
--------

traceroute [-dv] [-w waittime] HOST

Examples
--------

- Track the path of a ping to the ND Domain URL "nd.edu" 
	>>> traceroute nd.edu

- Track the path of a ping to the ND IP Address "52.6.129.12" 
	>>> traceroute 52.6.129.12

[ -w waitime] Set the time to wait for a response to "waitime"
	>>> traceroute -w 10 nd.edu

[ -d ] Enable socket-level debugging
	
[ -v ] Verbose mode, print bugging pages.



Resources
---------

[ Linux Man-Pages ] 
