#!/usr/bin/env python2.7

import getopt
import os
import sys

# Global Variables

PROGRAM_NAME = os.path.basename(sys.argv[0])
SOURCE=''
TARGET=''
BS = 512
COUNT = sys.maxint
SEEK=0
SKIP=0

# Functions

def error(message, exit_code=1):
    print >>sys.stderr, message
    sys.exit(exit_code)

def usage(exit_code=0):
    error('''Usage: {}

Options:

    if=FILE     Read from FILE instead of stdin
    of=FILE     Write to FILE instead of stdout

    count=N     Copy only N input blocks
    bs=BYTES    Read and write up to BYTES bytes at a time

    seek=N      Skip N obs-sized blocks at start of output
    skip=N      Skip N ibs-sized blocks at start of input'''
    .format(PROGRAM_NAME), exit_code)

def open_fd(path, mode):
    try:
        return os.open(path, mode)
    except OSError as e:
        error('Could not open {}: {}'.format(SOURCE, e))

def read_fd(fd, n):
    try:
        return os.read(fd, n)
    except OSError as e:
        error('Could not read {} BS from FD {}: {}'.format(n, fd, e))

def write_fd(fd, data):
    try:
        return os.write(fd, data)
    except OSError as e:
        error('Could not write {} BS from FD {}: {}'.format(len(data), fd, e))

def printArgs():
    print "Input File", SOURCE, type(SOURCE)
    print "Output File", TARGET, type(TARGET)
    print "BLOCK COUNT", COUNT, type(COUNT)
    print "BS per BLOCK", BS, type(BS)
    print "SEEK", SEEK, type(SEEK)
    print "SKIP", SKIP, type(SKIP)

# Parse Command line arguments

args = sys.argv
for i in range(1, len(sys.argv)):
    args[i]=args[i].split('=')

for i in range(1, len(sys.argv)):
    if args[i][0] == "if":
        SOURCE = args[i][1]
    elif args[i][0] == "of":
        TARGET = args[i][1]
    elif args[i][0] == "count":
        COUNT = int(args[i][1])
    elif args[i][0] == "bs":
        BS = int(args[i][1])
    elif args[i][0] == "seek":
        SEEK = int(args[i][1])
    elif args[i][0] == "skip":
        SKIP = int(args[i][1])
    else:
        usage(1)

# Handling of Source / Destination Files

if SOURCE:
    source = open_fd(SOURCE, os.O_RDONLY)
    os.lseek(source, (BS*SKIP), 0)
else: 
    source=0

if TARGET:
    target = open_fd(TARGET, os.O_WRONLY|os.O_CREAT)
    os.lseek(target, (BS*SEEK), 0)
else: 
    target = 1

# Main Execution

data = read_fd(source, BS)
countTotal=0

while data and (countTotal < COUNT):
        write_fd(target, data)
        data = read_fd(source, BS)
        countTotal=countTotal+1

os.close(source)
os.close(target) 



