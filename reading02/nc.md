TLDR - nc
==========

Overview - arbitrary "connections" and "listens"
--------

nc [-cDhlv] [hostname] [port[s]]

Options
--------

- Example
	>>> nc recievingterminal.com 1223   [ connect to that server at port 1223 ]
	>>> Hello, server 						[ sends the data "Hello, server to that port"]


[ -c ] Send CRLF as line-ending, for HTML

[ -l ] SERVER MODE: Listens on a port, instead of initiating a connection
		>>> nc -l PORT

[ -D ] Enable debugging on the socket

[ -v ] Enable verbose output

[ -h ] Help menu



Resources
---------

[ Linux Man-Pages ]
