#!/usr/bin/env python
import tempfile
import getopt
import sys
import os 

# Global Variables

INDEX=1
NAME=""

# Usage 
def usage(status=0):
	print '''usage: imv.py files ...'''.format(os.path.basename(sys.argv[0]))
	sys.exit(status)

# Create Temporary File
os.system("touch tmp")

OUT = os.open("tmp",os.O_RDWR)
for arg in sys.argv[1:]:
	os.write(OUT, arg)
	os.write(OUT,"\n")

try: 
	os.system('$EDITOR tmp')
except:
	os.system('nano tmp')

ISTREAM = open('tmp')
for fileTitle in ISTREAM:
	for val in fileTitle:
		if not val.isspace():
			NAME += val
	try:
		os.rename(sys.argv[INDEX],NAME)
	except OSError as e:
		print e
		sys.exit(0)
	INDEX += 1
	NAME = ""

os.system('rm tmp')