#!/bin/sh
#Shell Script "bake.sh"

function cleanup(){						
	rm -f $tmp
}

tmp=$(mktemp /tmp/disk_usage.sh.XXXXXX)		
trap "cleanup; exit 1" INT TERM	
trap "cleanup; exit 0" EXIT

flag1=""
flag2='10'

while getopts "an:" option; do	
    case $option in				
	a) flag1=$1;;
	n) flag2=$OPTARG ;;
	esac
done

shift $(($OPTIND-1))			
directory="$@" 
echo $directory                                                                                                                     
du -h $flag1 $directory | sort -r | head -n $flag2 > $tmp

cat $tmp
