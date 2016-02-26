#!/bin/sh -x

####### Main Script #######
declare DELIM="#"
rmBlanks="sed -e /^$/d"
   
while [ $# -gt 0 ]; do
        case "$1" in
                -W)
                        rmBlanks="cat"
                        shift
                        ;;
                -d)
                        shift
                        if [ $# -gt 0 ]; then
                                DELIM=$1
                                shift
                        else
                                DELIM="#"
                        fi
                        ;;
                *)      
                        break
                        ;;
        esac
done
rmComments='sed 's/$DELIM.*$//g'' 

$rmBlanks | \
$rmComments | \
$rmBlanks | \
cat