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

if len(args) == 0:
    args.append('-')

# Main execution
stream = sys.stdin
text=''
for line in stream:
    text=text+line
stream.close()

if printBytes == 'TRUE':
    print "You chose to print the Character Count"
    print len(text)
if printWords == 'TRUE':
    print "You Chose to print the word Count"
    words=text.split(None)
    print len(words)
if printNewline == 'TRUE':
    print "You Chose to print the number of new lines"
    print text.count('\n')
