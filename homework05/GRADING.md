Homework 05 - Grading
=====================

**Score**: 14 / 15

Deductions
----------
Activity 01: Caesar Cipher 
-0.25 	Doesn't handle -h flag (ie. print usage)

Activity 02: Reddit Links 
-0.25		Does not support multiple subreddits (ie. should loop over $@)
see my comments below about how to do the getopts loop


Activity 03: Broification
inside of your getops loop you should just set the variables, putting other things in there makes the code hard to read. Example:
while getopts 'hd:W' option; do
    case $option in
    d)  DELIMITER=$OPTARG;;
    W)  EMPTY_LINES=1;;
    *)  usage 0;;
    esac
done
shift $((OPTIND - 1))

-.5; did not pass all of the tests

interesting solution, I see where you were going with it, but bc the tests did not pass, take a look at a correct solution:
#!/bin/sh

DELIMITER='#'
EMPTY_LINES=0

usage() {
    cat <<EOF
usage: $(basename $0)

    -d  DELIM   Use this as the comment delimiter
    -W          Don't strip empty lines
EOF
    exit $1
}

filter() {
    if [ $EMPTY_LINES -eq 1 ]; then
        cat
    else
        sed '/^\s*$/d'
    fi
}

while getopts 'hd:W' option; do
    case $option in
    d)  DELIMITER=$OPTARG;;
    W)  EMPTY_LINES=1;;
    *)  usage 0;;
    esac
done

shift $((OPTIND - 1))

sed -e "s|$DELIMITER.*$||" -e "s|\s*$||" | filter


Comments
--------
