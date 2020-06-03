#!/usr/bin/env python

import re
import sys
from mypy.datatools import Frame



aframe = Frame(fromfile=sys.argv[1])
pframe = Frame(fromfile=sys.argv[2])

# outframe = Frame(['Time','Name','Talk'])


namepat = re.compile('^No \d+:(.*)$')

for d in pframe.iterFrame():
	name = namepat.match(d['Name'].strip())
	if name:
		print name.group(1)
		affraw = aframe.getData('Name', name.group(1))['Affiliation']
		affra = ['(' +x+ ')' for x in affraw.split(' and ')]
		aff = ""
		for i in affra:
			aff += i	
		d['Name'] = '"'+ d['Name'] + ' ' + aff + '"'
	else:
		continue
	
pframe.printFrame('newprog.csv')
