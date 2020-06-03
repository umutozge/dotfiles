#!/usr/bin/env python

import sys
from mypy.datatools import Frame, DataNotFound



qframe = Frame(fromfile=sys.argv[1])
pframe = Frame(fromfile=sys.argv[2])

parts = pframe.uniqField('Pid')




for d in qframe.iterFrame():

	h = qframe.header
	acc = ''
	for i in range(1,31):
		f = lambda x: x.startswith('Q'+str(i))
		head = filter(f,h)[0]
		acc = acc + d[head][-1] + '-'

	d['seq'] = acc

for p in parts:
	pf = pframe.filter(('Pid',p))
	acc='' 
	for i in range(1,31):
		resp= pf.getData('Sentno',str(i))['Response']
		acc = acc+ resp + '-'
	try:
		bd=	qframe.filter(('seq',acc))
		count = len(bd.iterFrame())
		qd = bd.iterFrame()[0]
		if count == 2:
			print  'ein moment'
			print bd.iterFrame()[0]['Participant']
			print bd.iterFrame()[1]['Participant']
			print p
			print qd['Participant']
			print qd['seq']
	except DataNotFound:
		pass
	except IndexError:
		pass
	else:
		qd['Pid'] = p
	
	if p == '33':
		print qd['Participant']
		print qd['seq']
		print acc

qframe.printFrame('new-' + sys.argv[1])

