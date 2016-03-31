#!/usr/bin/env python2.7

import getopt
import os
import sys
import time

# Global Variables

PROGRAM_NAME = os.path.basename(sys.argv[0])
INTERVAL = 2
COMMAND = ''
# Functions

def error(message, exit_code=1):
    print >>sys.stderr, message
    sys.exit(exit_code)

def usage(exit_code=0):
    error('''Usage: {}

Options:

    -n INTERVAL   Specify update interval (in seconds)
    '''
    .format(PROGRAM_NAME), exit_code)

# Parse Command line arguments

try:
    options, arguments = getopt.getopt(sys.argv[1:], "hn:")
except getopt.GetoptError as e:
    error(e)

for option, value in options:
    if option == '-n':
        INTERVAL = float(value)
        print "INTERVAL is: ", INTERVAL
    elif option == '-h':
        usage(0)
    else:
        usage(1)

COMMAND = ''.join(map(str, arguments))
print COMMAND

# Main Execution
while(True):
    try:
        os.system('clear')
        print "Every %.1fs: %s\n" % (INTERVAL, COMMAND)
        os.system(COMMAND)
        time.sleep(INTERVAL)
    except KeyboardInterrupt:
        sys.exit(0)

error('{} Not implemented!'.format(PROGRAM_NAME))