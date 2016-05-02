TLDR - tmux
==========

Overview - Open a session that will remain open even after exiting
--------

Starting Syntax
---------------

tmux [-vV] [new-session -s NAME] [-c shell-command] 


 - Begin a tmux session 
 >>> tmux

[ new-session -s NAME ] Begin a tmux session with a specified name
 >>> tmux new-session -s TestSession

[ -c shell-command ] Begin a tmux session for a specific command
 >>> tmux new-session -s TestSession

[ -V ] Return the tmux version.
	
[ -v ] Verbose mode, print bugging pages.


Tmux Commands
-------------
[ ls ] List the current tmux sessions 
>>> tmux ls

[ detach ] Detach from tmux, session will run.
>>> tmux detach

[ attach-session -t NAME ] Attach to a tmux session 
>>> tmux attach-session -t NAME

[ kill-session -t NAME ] End a tmux session 
>>> tmux kill-session -t NAME

[ kill-server ] End all tmux stuff 
>>> tmux kill-server



Resources
---------

[ Linux Man-Pages ] 
