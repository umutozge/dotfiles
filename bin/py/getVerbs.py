#!/usr/bin/env python

import sys
from optparse import OptionParser
from xml.dom  import minidom, pulldom

def proc(filename):
	events = pulldom.parse(open(filename,'r'))	
	outfile.write('Analyzing project '+filename+'\n\n')

	take = 0 #when set the first encountered word is taken as a verb 
	for event, node in events:
		if event=='START_ELEMENT' and node.tagName=='bi':
			events.expandNode(node)
			outfile.write('\n\n')
			for n in node.childNodes:
				outfile.write(n.childNodes[0].wholeText.encode('utf-8')+' ')
			outfile.write('\nVerb: ')
			take += 1
		if take > 0 and event=='START_ELEMENT' and node.tagName=='w':
			events.expandNode(node)
			outfile.write(node.childNodes[0].wholeText.encode('utf-8') +' ')
			take = (take + 1)%3


if __name__=="__main__":

	clp = OptionParser()
	clp.usage="%prog [-o] input-file1 input-file2 ..."
	clp.epilog="works over mmaxx input files and returns a list of verbs coming after 'base indefinites' marked with '<bi/>'."
	clp.add_option('-o', dest='outfile', metavar="FILE", default='verbs.txt', help="write verb list to FILE")
	opts, args = clp.parse_args()	

	outfile = open(opts.outfile,'w')
	
	for f in args:
		proc(f) 
		outfile.write('\n\n')

sys.stderr.write('\nDone!\n')
sys.exit(0)	
