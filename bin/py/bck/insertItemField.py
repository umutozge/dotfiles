#!/usr/bin/env python

import sys
from mypy.datatools import Frame

infile = sys.argv[1]

f = Frame(fromfile=infile)
f.header.insert(f.header.index('Condition'),'Item')

def trim2(name):
	if name.endswith('2'):
		return name[:-1]
	else:
		return name


for d in f.iterFrame():
	aois=[]
	for i in range(1,4):
		aois.append(trim2(d['AOI'+str(i)][:-4]))	
	
	d['Item'] = '-'.join(sorted(aois))

f.printFrame('items-added-'+infile)
