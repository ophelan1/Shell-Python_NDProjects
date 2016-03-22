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
    opts, args = getopt.getopt(sys.argv[1:], "hc")
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

for path in args:
    if path == '-':
        stream = sys.stdin
    else:
        stream = open(path)

# Main execution
inputLines=[]
for line in stream:
	inputLines.append(line)
stream.close()

if COUNT == 'FALSE': 
	print inputLines[0].rstrip()
	for e in range(1,len(inputLines)):
		if inputLines[e].rstrip('\n') != inputLines[e-1].rstrip('\n'):
			print inputLines[e].rstrip()

else:
	repCount=1
	for e in range(0,len(inputLines)-1):
		
		if inputLines[e].rstrip('\n') != inputLines[e+1].rstrip('\n'):
			print str(repCount).rjust(7), inputLines[e].rstrip()
			repCount=1
		else:
			repCount=repCount+1
	print str(repCount).rjust(7), inputLines[len(inputLines)-1].rstrip()



