#!/usr/bin/env python2.7

import getopt
import os
import sys
import re
import fnmatch

# Global Variables

PROGRAM_NAME = os.path.basename(sys.argv[0])
TYPE = ''
DIRECTORY = ''
NAME = ''
PATH = ''
REGEX = ''
PERMISSIONS = ''
NEWERFILE = ''
EXECUTABLE = False
READABLE = False
WRITABLE = False
EMPTY = False
UID = 0
GID = 0

# Functions

def error(message, exit_code=1):
    print >>sys.stderr, message
    sys.exit(exit_code)

def usage(exit_code=0):
    error('''Usage: {}


Options:

    -type [f|d]     File is of type f for regular file or d for directory

    -executable     File is executable and directories are searchable to user
    -readable       File readable to user
    -writable       File is writable to user

    -empty          File or directory is empty

    -name  pattern  Base of file name matches shell pattern
    -path  pattern  Path of file matches shell pattern
    -regex pattern  Path of file matches regular expression

    -perm  mode     File's permission bits are exactly mode (octal)
    -newer file     File was modified more recently than file

    -uid   n        File's numeric user ID is n
    -gid   n        File's numeric group ID is n'''
    .format(PROGRAM_NAME), exit_code)

def include(path):
    ''' Returns True if item should be included in output, otherwise False '''
    linkStatus = "unbroken"
    try: 
        inode = os.stat(path)
    except OSError:
        inode = os.lstat(path)
        linkStatus = "broken"

    if TYPE == 'f':
        if not os.path.isfile(path):
            return False

    if TYPE == 'd':
        if not os.path.isdir(path):
            return False

    if EXECUTABLE:
        if not (os.path.isfile(path) or os.path.isdir(path)):
            return False
        elif os.path.isfile(path):
            if not os.access(path, os.X_OK):
                return False
        elif os.path.isdir(path):
            try: 
                os.listdir(path)
            except OSError:
                return False
        elif not os.path.isfile(path) and not os.path.isdir(path):
            return False

    if EMPTY:
        if not ( os.path.isfile(path) or os.path.isdir(path) or os.path.islink(path) ):
            return False
        elif os.path.isfile(path):
            if not inode.st_size == 0:
                return False
        elif os.path.isdir(path):
            try:
                if not len(os.listdir(path)) == 0:
                    return False
            except:
                return False
        elif os.path.islink(path) and linkStatus == "broken":
            return False



    if READABLE:
        if not os.access(path, os.R_OK):
            return False

    if WRITABLE:
        if not os.access(path, os.W_OK):
            return False

    if NAME:
        nameVal = os.path.basename(path)
        if not fnmatch.fnmatch(nameVal, NAME):
            return False

    if PATH:
        if not fnmatch.fnmatch(path, PATH):
            return False

    if REGEX:
        if re.match(REGEX, path) is None:
            return False

    if UID:
        if stat.ST_UID(inode.st_mode) != UID:
            return False

    if GID:
        if stat.ST_GID(inode.st_mode) != GID:
            return False


    return True

# Parse Command line arguments
args = sys.argv
if os.path.isdir(args[1]):
    DIRECTORY = args[1]
else:
    error("Need to Specify Directory As First Argument")

for i in range(1, len(sys.argv)):
    if args[i] == "-type":
        TYPE = args[i+1]
    elif args[i] == "-executable":
        EXECUTABLE = True
    elif args[i] == "-readable":
        READABLE = True
    elif args[i] == "-writable":
        WRITABLE = True
    elif args[i] == "-empty":
        EMPTY = True
    elif args[i] == "-name":
        NAME = args[i+1]
    elif args[i] == "-path":
        PATH = args[i+1]
    elif args[i] == "-regex":
        REGEX = args[i+1]
    elif args[i] == "-perm":
        PERMISSIONS = args[i+1]
    elif args[i] == "-newer":
        NEWERFILE = args[i+1]
    elif args[i] == "-uid":
        UID = args[i+1]
    elif args[i] == "-gid":
        GID = args[i+1]
    elif args[i] == "-h":
        usage(1)

# Main Execution
if include(DIRECTORY):
    print DIRECTORY

for root, dirs, files in os.walk(DIRECTORY, onerror=None, followlinks=True):
    for name in dirs + files:
        pathVal = os.path.join(root, name)
        if include(pathVal):
            print pathVal

