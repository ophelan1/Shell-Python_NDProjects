#!/bin/sh
#Shell Script "enviornment.sh"

cat << _EOF_
USER				is:$USER
HOME				is:$HOME
SHELL 				is:$SHELL
TERM				is:$TERM
EDITOR				is:$EDITOR
HOSTNAME			is:$HOSTNAME
PATH				is:$PATH
LD_LIBRARY_PATH 		is:$LD_LIBRARY_PATH
PWD				is:$PWD
_EOF_