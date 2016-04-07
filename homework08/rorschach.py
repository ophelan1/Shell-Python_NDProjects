#!/usr/bin/env python2.7

import getopt
import os
import sys
import yaml
import shlex
import glob
import fnmatch
from datetime import datetime
import time

# Global Variables

PROGRAM_NAME = os.path.basename(sys.argv[0])
START_TIME = time.ctime(time.time())
RULES = '.rorschach.yml'
TIME = 2
VERBOSE = False
DIRECTORIES = '.'


# Functions
def verbose(Message):
    if VERBOSE == True:
        print Message

def loadRules():
    stream = file(RULES, 'r')
    rules = yaml.load(stream)
    return rules

def itRules(filename):
    new_time = time.ctime(os.path.getmtime(filename))
    if new_time >= START_TIME:
        verbose("Newer File Found: {}".format(filename))
        for dictItem in RULES:
            Action = shlex.split(dictItem['action'].format(path = filename, name = os.path.basename(filename)))
            Pattern = str(dictItem['pattern']).strip()

            if fnmatch.fnmatch(filename, Pattern):
                verbose("File Matches Pattern: {}, Executing: {}".format(Pattern, Action))
                try:
                    pid = os.fork()
                    if pid == 0: #Child
                        os.execvp(Action[0], Action)
                        sys.exit(0)
                    else: #Parent
                        pid, status = os.wait()
                except OSError as e:
                    error(e)
        

def itFiles(dirName):
    for filename in os.listdir(dirName):
        address = os.path.join(dirName, filename)
        itRules(address)
    verbose("       All Files Checked in Directory {}".format(dirName))

def itDirs():
    for path in DIRECTORIES:
        itFiles(path)

def error(message, exit_code=1):
    print >>sys.stderr, message
    sys.exit(exit_code)

def usage(exit_code=0):
    error('''Usage: {} [-r RULES -t SECONDS] DIRECTORIES...\n\nOptions:

    -r RULES    Path to rules file (default is .rorschach.yml)
    -t SECONDS  Time between scans (default is 2 seconds)
    -v          Display verbose debugging output
    -h          Show this help message'''.format(PROGRAM_NAME), exit_code)

def begin():
    verbose("Time Selection = {}".format(TIME))
    verbose("Directories to be checked: {}".format(DIRECTORIES))
    verbose("Starting Time = {}".format(START_TIME))
    verbose("Loading Rules....")
    RULES = loadRules()
    verbose("Rules Succesfully Loaded!")


# Parse Command line arguments

try:
    options, arguments = getopt.getopt(sys.argv[1:], "r:t:vh")
except getopt.GetoptError as e:
    error(e)

for option, value in options:
    if option == '-h':
        usage(0)
    elif option == '-r':
        RULES = str(value)
    elif option == '-t':
        TIME = int(value)
    elif option == '-v':
        VERBOSE = True
    else:
        usage(1)

if len(arguments) != 0:
    DIRECTORIES = arguments
    

# Main Execution
begin()
while True:
    try:
        itDirs()
        START_TIME = time.ctime(time.time())
        verbose("Comparison Time Updated to: {}".format(START_TIME))
        time.sleep(TIME)
    except KeyboardInterrupt:
        sys.exit(0)




error('{} Not implemented!'.format(PROGRAM_NAME))
