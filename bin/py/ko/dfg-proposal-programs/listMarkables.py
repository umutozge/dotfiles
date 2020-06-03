#!/usr/bin/env python

from xml.dom import minidom, pulldom
from optparse import OptionParser
import sys


def procMarkable(node):
	if node.getAttribute('type') == 'base_indef.':
		line= ""
		for x in ['case_marking','optional','backward_linking','forward_linking','descriptive_content','animacy']:
			line += node.getAttribute(x) + ','
		line += '\n'	
		outfile.write(line)



clparser = OptionParser()
sys.stderr.write('\n')
clparser.usage="%prog [options] markables-file"
clparser.add_option('-o', dest='outfile', metavar="FILE",\
help="write the results to a csv file.")

opts, args = clparser.parse_args()


outfile = open(opts.outfile,mode='w')
outfile.write('Case,Optional,Backward,Forward,DescCont,Animacy\n')

events = pulldom.parse(open(args[0],'r'))
for event , node in events:
	if event == 'START_ELEMENT' and node.tagName=='markable':
		events.expandNode(node)	
		procMarkable(node)

outfile.flush()
outfile.close()
sys.stderr.write('\nDone.\n')

sys.exit(0)
