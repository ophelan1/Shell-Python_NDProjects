#!/usr/bin/env python2.7

import getopt
import os
import sys

# Globals

printNewline='FALSE'
printWords='FALSE'
printBytes='FALSE'
DELIM='/t'

# Usage function

def usage(status=0):
    print '''usage: wc.py [-c -l -w] files ...

    -c      print the byte/character counts
    -l      print the newline counts
    -w      print the word counts'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

# Parse command line options
try:
    opts, args = getopt.getopt(sys.argv[1:], "hclw")
except getopt.GetoptError as e:
    print e
    usage(1)

if len(opts) == 0:
    print "ERROR MUST PASS A COMMAND LINE ARGUMENT"
    usage(1)

for o, arg in opts:
    if o == '-c':
        printBytes='TRUE'
    elif o == '-l':
        printNewline='TRUE'
    elif o == '-w':
        printWords='TRUE'
    else:
        usage(1)

implicit='FALSE'

if len(args) == 0:
    args.append('-')
    implicit='TRUE'


for path in args:
    if path == '-':
        stream = sys.stdin
    else:
        stream = open(path)

if implicit=='TRUE':
    path=''

# Main execution
text=''
for line in stream:
    text=text+line
stream.close()

if printBytes == 'TRUE':
    output=str(len(text))+" "+path
    print output.rstrip()
if printWords == 'TRUE':
    words=text.split(None)
    output=str(len(words))+" "+path
    print output.rstrip()
if printNewline == 'TRUE':
    output=str(text.count('\n'))+" "+path
    print output.rstrip()
