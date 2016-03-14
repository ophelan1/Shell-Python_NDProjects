#!/bin/sh
#Shell Script "mascot.sh"

if [ $(uname) = "Linux" ]; 
then
   echo "Tux"
elif [ $(uname) = "Darwin" ]; then
   echo "Hexley"
elif [ $(uname) = "FreeBSD" ] || [ $(uname) = "NetBSD" ] || [ $(uname) = "OpenBSD" ]; then
	echo "Beastie"
fi
