#!/bin/sh

####### Main Script #######
declare -i lineNum=10
shuffleTest=cat
sortTest=cat
while test $# -gt 0; do
        case "$1" in
                -*r)
                        shuffleTest='shuf'
                        shift
                        ;;
                -*s)
                        sortTest='sort'
                        shift
                        ;;
                -n|-N)
                        shift
                        if [ $# -gt 1 ]; then
                                lineNum=$1
                                shift
                        else
                                lineNum=10
                        fi
                        ;;
                *)      
                        break
                        ;;
        esac
done
subReddit="$1"
echo "The Sub Reddit is: $subReddit"
curl -s http://www.reddit.com/r/$subReddit/.json | python -m json.tool | \
grep -F '"url":' | \
sed 's/^.*"url": "\(.*\)",/\1/g' | \
$sortTest | \
$shuffleTest | \
head -n$lineNum
