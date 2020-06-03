#!/usr/bin/env python

import re
import sys

infile = open(sys.argv[1],'r')


mpat = re.compile('(.*morph=")([^[]*)(\[.*">.*)')

for l in infile:
	g = mpat.search(l)
	if g:
		newl = g.group(1)+g.group(2).replace('-','DASH').replace('+','PLUS').replace('"','QQ')+g.group(3)
		print newl
	else:
		print l,

