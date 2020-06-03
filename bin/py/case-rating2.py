#!/usr/bin/env python

from mypy.datatools import Frame, Csv
import sys


frame = Frame(fromfile=sys.argv[1])

items = frame.header[1:]

header = ['ID']
for i in items:
	header.extend([i+x for x in ['_AccFavor','_Neutral','_ZeroFavor']])

outframe = Frame(header)


get_cat = lambda x:{0:'_Neutral',1:'_AccFavor',-1:'_ZeroFavor'}[x]


for d in frame:
	nd = {'ID':d['ID']}
	for x in header[1:]:
		nd[x] = '0'
	for i in items:
		val = int(d[i])
		nd[i+get_cat(val)] = 1
	outframe.addData(nd)

outframe.printFrame('long-out.csv')


	
