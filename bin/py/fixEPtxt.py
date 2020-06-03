#!/usr/bin/env python

import sys

for f in sys.argv[1:]:
	name = f[:f.index('.')]
	
	inf = open(f,'r')
	outf = open(name+'.text','w')

	for l in  inf:
		outf.write(l)	
	
	outf.close()
