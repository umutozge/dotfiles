#!/usr/bin/env python
import sys
import os
import re
from copy import copy
from mypy.datatools import Frame, Csv 

infilename = sys.argv[1]
outfilename = re.sub('toMixedModel','MixedModel',infilename) 

inframe = Frame(fromfile=infilename)
parts = inframe.uniqField('Participant')
items = inframe.uniqField('Item')
conds = inframe.uniqField('Condition')
tws = inframe.uniqField('TimePeriod')


newheader = inframe.header[:3] + tws

outframe = Frame(newheader)
accum = {}
for p in parts:
	accum['Participant'] = p
	pF = inframe.filter(('Participant',p))
	for i in items:
		accum['Item'] = i
		iF = pF.filter(('Item',i))		
		for c in conds:
			accum['Condition'] = c
			cF = iF.filter(('Condition',c))
			for t in tws:
				dat = cF.getData('TimePeriod',t)
				accum[t] = str(float(dat['ThemePercFix']) - float(dat['GoalPercFix']))
			outframe.addData(copy(accum))

dellist= []
for d in outframe:
	flag = True
	for t in tws:
		if d[t][0] == '0':
			pass	
		else:
			flag = False	
	if flag:
		print d
		print ''
		dellist.append(d)

for d in dellist:
	outframe.removeData(d)
	

outframe.printFrame(outfilename)
