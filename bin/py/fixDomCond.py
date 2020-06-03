#!/usr/bin/env python

import sys
from mypy.datatools import Frame

ff = open(sys.argv[1],'r')
dd = {}

for l in ff:
	s= l.split(' ')
	dd[s[0]] = s[1].strip()		

# print dd;sys.exit()

for f in sys.argv[2:]:
	inf = open(f,'r')
	fr = Frame(fromfile=f,delimiter='\t')

	for d in fr:
		if not d['Condition'] == 'Practice':
			item =  '-'.join(sorted([d['AOI1'][:-4],d['AOI2'][:-4]]))
			d['Condition'] = dd[item] 
	
	fr.printFrame(f,delimiter='\t')
