#!/usr/bin/env python

from xml.dom import minidom, pulldom
from optparse import OptionParser
import sys

clparser = OptionParser()
sys.stderr.write('\n')
clparser.usage="%prog [options] input-file1, input-file2,..."
clparser.add_option('-o', dest='outfile', metavar="FILE",\
help="write the merged xml to FILE")

opts, args = clparser.parse_args()



outfile = open(opts.outfile,mode='a')
outfile.write(u'<?xml version="1.0" encoding="UTF-8"?><markables>'.encode('utf-8'))

sys.stderr.write('Merging...\n\n')
for arg in args:
	events = pulldom.parse(open(arg,'r'))
	print arg 
	for event , node in events:
		if event == 'START_ELEMENT' and node.tagName=='markable':
			events.expandNode(node)	
			outfile.write(node.toxml().encode('utf-8'))

outfile.write('</markables>')
outfile.flush()
outfile.close()
sys.stderr.write('\nDone.\n')

sys.exit(0)
