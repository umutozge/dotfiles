#!/usr/bin/python
import sys
import re
from optparse import OptionParser
from xml.dom import pulldom

def writeDoc(node):
	outfile.write(u'<?xml version="1.0" encoding="UTF-8"?>\n'.encode('utf-8'))
	outfile.write(node.toxml().encode('utf-8'))
	outfile.flush()
	outfile.close()



clparser= OptionParser()
clparser.add_option("-d", dest="doctag",help="name of the document tag")
clparser.add_option("-n", dest="whichdoc",help="doc number")
clparser.add_option("-o", dest="outfile",help="output file")

(opts,args) = clparser.parse_args()

outfile = open(opts.outfile, 'w')
events = pulldom.parse(open(args[0],'r'))
count = 1

for event, node in events:
	if event == 'START_ELEMENT' and node.tagName==opts.doctag:
		if count == int(opts.whichdoc):
			events.expandNode(node)	
			writeDoc(node)
			sys.exit(0)
		else:
			count += 1
