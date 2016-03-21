#!/usr/bin/env python2.7

import getopt
import re
import os
import sys

# Globals

DELIM='\t'
FIELDS='NONE'

# Usage function

def usage(status=0):
    print '''usage: wc.py [-d DELIM -f] files ...

    -d DELIM  use DELIM instead of TAB for field delimiter
    -f FIELDS select only these FIELDS'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

# Parse command line options

try:
    opts, args = getopt.getopt(sys.argv[1:], "hd:f:")
except getopt.GetoptError as e:
    print e
    usage(1)

for o, arg in opts:
    if o == '-d':
        DELIM = arg
    elif o == '-f':
        fieldString=str(arg)
        FIELDS=fieldString.split(",")
    else:
        usage(1)

if len(args) == 0:
    args.append('-')

if FIELDS=='NONE':
  print "ERROR: MUST SPECIFY FIELDS"
  usage(1)

# Main execution
stream = sys.stdin
inputLines=[]
for line in stream:
	inputLines.append(line)
stream.close()

for txt in inputLines:
  splitTxt=txt.split(DELIM)
  finalPrint=''
  for i in FIELDS:
    if ( int(i) <= len(splitTxt) ):
      printablefield=splitTxt[int(i)-1].rstrip()
      finalPrint=finalPrint+printablefield+' '
  print finalPrint
