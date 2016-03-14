#usr/bin/sh 

####### Main Script #######
if [ $# = 2 ]; then
	lineNum=${2}
else
	lineNum=10
fi
awk -v num=$lineNum 'BEGIN { 
	RS = "\n" 
} 
{
	if (NR <= num){
		print $0
	}
}'