#!/usr/bin/env python2.7

import getopt
import os
import sys

# Globals

COUNT = 10

# Usage function

def usage(status=0):
    print '''usage: head.py [-n NUM] files ...

    -n NUM  print the first NUM lines instead of the first 10'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

# Parse command line options

try:
    opts, args = getopt.getopt(sys.argv[1:], "hn:")
except getopt.GetoptError as e:
    print e
    usage(1)

for o, arg in opts:
    if o == '-n':
        COUNT = int(arg)
    else:
        usage(1)

if len(args) == 0:
    args.append('-')

# Main execution
stream = sys.stdin
countCheck=0
for line in stream:
	if countCheck == COUNT:
		sys.exit(0)
	print line.rstrip()
	countCheck=countCheck+1
