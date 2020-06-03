#!/usr/bin/python
from optparse import OptionParser
import sys

clparser = OptionParser()
clparser.add_option('-t', dest='tagname')

(opts,args) = clparser.parse_args()

tagname = vars(opts).get('tagname')

infile = open(args[0],'r')

otag = '<'+tagname+'>'
ctag = '</'+tagname+'>'

count = 0 
linecount = 0
longcount = 0
totalcount = 0
counting = False


for line in infile.readlines():
	line = line.strip()
	linecount += 1
	if line == ctag:
#		print count, linecount
		totalcount += 1
		if count > 500:
			longcount += 1
		counting = False
	elif line == otag:
		count = 0
		counting = True
	if counting:
		count += 1

print longcount,totalcount

