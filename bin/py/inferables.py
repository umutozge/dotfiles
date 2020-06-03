#!/usr/bin/env python

import sys
from mypy.datatools import Frame
from optparse import OptionParser


if __name__=='__main__':
	
	#first read the correspondence
	c = Frame(fromfile=sys.argv[1])
	itemlist = [] 
 	for i in range(1,33):
		if i < 10:
			itemlist = itemlist + [('0'+ str(i))]
		else:
			itemlist = itemlist + [str(i)]

	corres = {} 	
 	for d in c.data:
 		corres[d['AppearsAs']] = d['ItemNo']

	group1 = Frame(fromfile=sys.argv[2])
	newhead = 'Participant,' 
	for h in group1.header[1:]:
		newhead += corres[h[1:3]]+','

	print newhead
	
	for d in group1:
		line = ''
		for h in group1.header:
			line += d[h]+','
		print line	
