#!/usr/bin/env python2.7

import getopt
import os
import sys
import signal
import time
import errno

# Global Variables

TIME = 10
VERBOSE = False

# Functions
def debug(message):
    if VERBOSE == True:
        print >>sys.stderr, (message)

    
def alrm_handler(signal, frame):
    debug("Alarm Triggered After {} Seconds!".format(TIME))
    debug("Killing PID {}".format(os.getpid()))
    os.kill(os.getpid(), 15)

def error(message, exit_code=1):
    
    if VERBOSE == True:
        print >>sys.stderr, message
        sys.exit(exit_code)

def usage(exit_code=0):
    error('''Usage: timeout.py [-t SECONDS] command...

Options:

      -t SECONDS  Timeout duration before killing command (default is 10 seconds)
      -v          Display verbose debugging output'''.format(os.path.basename(sys.argv[0])), exit_code)

# Parse Command line arguments

try:
    options, arguments = getopt.getopt(sys.argv[1:], "t:hv")
except getopt.GetoptError as e:
    error(e)

for option, value in options:
    if option == '-h':
        usage(0)
    elif option == '-t':
        TIME = int(value)
    elif option == '-v':
        VERBOSE = True
    else:
        usage(1)

if len(arguments) == 0:
    usage(1)

# Main Execution
try:
    debug("Executing {} for at most {} seconds".format(' '.join(arguments), TIME))
    debug("Forking...")
    pid = os.fork()
    if pid == 0: #Child
        os.getpid()
        debug("Execing..")
        os.execvp(arguments[0], arguments)
        sys.exit(0)
    else: #Parent
        signal.signal(signal.SIGALRM, alrm_handler)
        debug("Enabling Alarm...")
        signal.alarm(TIME)
        debug("Waiting...")
        pid, status = os.wait()
        debug("Process {} exited with status: {}".format(pid, status))
        

except OSError as e:
    error(e)
except KeyboardInterrupt:
    sys.exit(0)





