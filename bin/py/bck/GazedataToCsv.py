#!/usr/bin/env python

import sys

for infile in sys.argv[1:]:

	outfile = open(infile[:-9]+'.csv','w')

	for l in open(infile,'r').readlines():
		outfile.write(l.replace('\t',','))
	outfile.flush()
	outfile.close()
sys.exit(0)
