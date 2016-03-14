#!/bin/sh
#Shell Script "resolve_links.sh"

for testLink in $1/*;
do
	if [ -L $testLink ]; then 
		resolvedLink=$(readlink $testLink)
		echo $resolvedLink
	fi
done
