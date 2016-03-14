#!/bin/sh
#Shell Script "bake.sh"
PATH=$PATH:/afs/nd.edu/user15/pbui/pub/bin
export PATH

function SIGHUP_MESSAGE(){
	echo "Special SIGHUP Message"
	rm -f $tmp
}
function TAUNT_MESSAGE(){
	echo "You Can't Touch This"
	rm -f $tmp
}

tmp=$(mktemp /tmp/tmp.XXXXXX)

trap "SIGHUP_MESSAGE; exit" 1
trap "TAUNT_MESSAGE; exit" 2 15

echo "The Cow Goes \"MOO\"" | cowsay

read -t 10 input || echo "You're slower than Mollasses" && exit