#!/usr/bin/env python

import sys
import re
from optparse import OptionParser
from mypy.datatools import Frame

for file in sys.argv[1:]:
	data = Frame(fromfile=file)
	for d in data.iterFrame():
		aois = [d['AOI'+str(x)] for x in range(1,4)]
		for i in [1,2,3]:
			if d['AOI'+str(i)]=='oyuncak.bmp' and 'adam.bmp' in aois:
				d['AOI'+str(i)]='oyuncakayi.bmp'
			if d['AOI'+str(i)]=='oyuncak.bmp' and 'kiz.bmp' in aois:
				d['AOI'+str(i)]='oyuncakbebek.bmp'
			elif d['AOI'+str(i)]=='cocuk2.bmp':
				d['AOI'+str(i)]='cocuk.bmp'
			elif d['AOI'+str(i)]=='kadin2.bmp':
				d['AOI'+str(i)]='kadin.bmp'
			elif d['AOI'+str(i)]=='bebek.bmp' and 'kiz.bmp' in aois:
				d['AOI'+str(i)]='oyuncakbebek.bmp'
	data.printFrame(file)
	sys.stderr.write('\nProcessed '+file)
sys.stderr.write('\n\nDone.\n\n')
