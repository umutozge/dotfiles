#!/usr/bin/env python

from mypy.datatools import Frame, Csv
import sys

def get_score(a,z,inter):
	if inter == 1:
		return a-z
	else:
		x = a -z
		if x > inter:
			return  1
		elif x < -1 * inter:
			return -1
		else:
			return 0
		

frame = Frame(fromfile=sys.argv[1])

total = float(len(frame.uniqField('ID')))

items = 'tanitti,atadi,davet_etti,dahil_etti,goturdu,konuk_etti,aldi,getirdi,transfer_etti,iade_etti,onerdi,kabul_etti'.split(',')

result = dict.fromkeys(items,0)

outframe = Frame(['ID']+items)

subs = frame.uniqField('ID')

for s in subs:
	d = frame.getData('ID',s)
	nd = {'ID':s}
	for i in items:
		score = get_score(int(d[i+'_acc']),int(d[i+'_zero']),1)
		nd[i] = score	
	outframe.addData(nd)
outframe.printFrame('out.csv')


	
