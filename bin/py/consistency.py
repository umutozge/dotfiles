#!/usr/bin/env python

import sys
from mypy.datatools import Frame


data = Frame(fromfile=sys.argv[1])
header = data.header
print header

newheadertail = []
for i in ['Nom','Acc']:
	for j in ['Expected','Unexpected','RefOther','Consistent','Inconsistent','CaseOther']:
		newheadertail.append(i+j)	

print newheadertail

outFrame = Frame(header=['Participant','Age']+newheadertail)
parts = data.uniqField('Participant')

for p in parts:
	filtered = data.filter(('Participant',p))
	dat = {}	
	dat['Participant'] = p
	dat['Age'] = filtered.uniqField('Age')[0]
	for d in filtered.data:	
		cond = d['Condition']
		exp = d['Exp']
		cons = d['Cons']
		explabel = ''
		conslabel = ''
		label = ''
		if cond == '0':
			label += 'Nom'
		else:
			label += 'Acc'

		explabel += label
		conslabel += label

		if exp == '0':
			explabel += 'Unexpected'
		elif exp == '1':
			explabel += 'Expected'
		else:
			explabel += 'RefOther'
	
		if cons == '0':
			conslabel += 'Inconsistent'
		elif cons == '1':
			conslabel += 'Consistent'
		else:
			conslabel += 'CaseOther'


		try:
			dat[explabel] = dat[explabel] + 1
		except KeyError:
			dat[explabel] = 1

		try:
			dat[conslabel] = dat[conslabel] + 1
		except KeyError:
			dat[conslabel] = 1

	outFrame.addData(dat)


outFrame.printFrame('output.csv')
