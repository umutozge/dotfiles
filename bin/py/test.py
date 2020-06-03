#!/usr/bin/env python


import sys

for f in sys.argv[1:]:
	infile = open(f,'r')
	outfile = open(f[:-3]+'text','w') 
	for l in infile:
		outfile.write(l)
	outfile.close()
