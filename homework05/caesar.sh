#!/bin/sh

###### Main Function######
declare -i input=${1-13}
input=$(($input % 26))
Upperinput=$(($input+65))
Lowerinput=$(($input+97))
Achar=$(printf \\$(printf '%03o' $Upperinput))
Zchar=$(printf \\$(printf '%03o' $((Upperinput-1))))
achar=$(printf \\$(printf '%03o' $Lowerinput))
zchar=$(printf \\$(printf '%03o' $((Lowerinput-1))))
tr '[A-Za-z]' '['$Achar'-ZA-'$Zchar''$achar'-za-'$zchar']'