#!/usr/bin/env python

import sys
from mypy.datatools import  *

def count(frame):
	countS = 0
	countO = 0
	countB = 0
	for d in frame.iterFrame():
		if d['Re-mention'] == '1':
			countS += 1
		elif d['Re-mention'] == '2':
			countO += 1
		elif d['Re-mention'] == '3':
			countB += 1
	return countS, countO, countB

inframe = Frame(fromfile=sys.argv[1])
#print inframe.header

parts = inframe.uniqField('Participant')
items = inframe.uniqField('Verb')

zerframe = inframe.filter(('Case','1'))
accframe = inframe.filter(('Case','2'))

partframe = Frame(['Participant','Perc-Subj-Zero','Perc-Obj-Zero','Perc-Subj-Acc','Perc-Obj-Acc'])

for part in parts:
	accu = {}	
	accu['Participant'] = part
	fr = zerframe.filter(('Participant',part))		
	s,o,b = count(fr)
	total = float(s+o+2*b)
	try:
		accu['Perc-Subj-Zero']= str((s+b)/total*100)
		accu['Perc-Obj-Zero']= str((o+b)/total*100)
	except ZeroDivisionError:
		accu['Perc-Subj-Zero']= 0 
		accu['Perc-Obj-Zero']= 0 

	fr = accframe.filter(('Participant',part))
	s,o,b = count(fr)
	total = float(s+o+2*b)
	try:
		accu['Perc-Subj-Acc']= str((s+b)/total*100)
		accu['Perc-Obj-Acc']= str((o+b)/total*100)
	except ZeroDivisionError:
		accu['Perc-Subj-Zero']= 0 
		accu['Perc-Obj-Zero']= 0 

	partframe.addData(accu)
		
partframe.printFrame('holler-perc-participant.csv')


itemframe = Frame(['Item','Perc-Subj-Zero','Perc-Obj-Zero','Perc-Subj-Acc','Perc-Obj-Acc'])

for item in items:
	accu = {}	
	accu['Item'] = item 
	fr = zerframe.filter(('Verb',item))		
	s,o,b = count(fr)
	total = float(s+o+2*b)
	try:
		accu['Perc-Subj-Zero']= str((s+b)/total*100)
		accu['Perc-Obj-Zero']= str((o+b)/total*100)
	except ZeroDivisionError:
		accu['Perc-Subj-Zero']= 0 
		accu['Perc-Obj-Zero']= 0 
	
	fr = accframe.filter(('Verb',item))
	s,o,b = count(fr)
	total = float(s+o+2*b)
	try:
		accu['Perc-Subj-Acc']= str((s+b)/total*100)
		accu['Perc-Obj-Acc']= str((o+b)/total*100)
	except ZeroDivisionError:
		accu['Perc-Subj-Zero']= 0 
		accu['Perc-Obj-Zero']= 0 

	itemframe.addData(accu)
		
itemframe.printFrame('holler-perc-item.csv')
