#!/usr/bin/env python

import re
import sys
from mypy.datatools import Frame

try:
	verbframe = Frame(fromfile=sys.argv[1])
	mainframe = Frame(fromfile=sys.argv[2])
except:
	print 'usage: addVerbType.py <verbfile> <datafile>'
	sys.exit(1)

for d in mainframe.iterFrame():
	np2 = d['NP2'].strip()
	try:
		verbdata = verbframe.getData('NP2',np2)
	except:
		d['Verb'] = ''
		d['VerbType'] = ''
	else:
		d['Verb'] = verbdata['Verb']
		d['VerbType'] = verbdata['Type']

outframe = Frame(['Pid','Sentno','Sentence','NP1','NP2','Response','Verb','VerbType','Case','Re-mention','Role'],mainframe.iterFrame())
outframe.printFrame('new-'+sys.argv[2])
