#!/usr/bin/env python2.7

import getopt
import os
import sys

# Globals

COUNT = 'FALSE'

# Usage function

def usage(status=0):
    print '''usage: uniq.py [-c]...

    -c 	Print the Number of Occurances With Each Line'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

# Parse command line options

try:
    opts, args = getopt.getopt(sys.argv[1:], "c")
except getopt.GetoptError as e:
    print e
    usage(1)

for o, arg in opts:
    if o == '-c':
        COUNT = 'TRUE'
    else:
        usage(1)

if len(args) == 0:
    args.append('-')

# Main execution
stream = sys.stdin
inputLines=[]
for line in stream:
	inputLines.append(line)
stream.close()

if COUNT == 'FALSE': 
   checked = []
   for e in inputLines:
       if e not in checked:
           checked.append(e)
   print ''.join(map(str, checked))

else:
	checked={}
	for e in inputLines:
		if e not in checked:
			checked[e]=1
		else:
			checked[e]=checked[e]+1
	for x in checked:
		print checked[x], x.rstrip()


print "End of program reached"
