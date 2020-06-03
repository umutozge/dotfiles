#!/usr/bin/env python

import sys
from mypy.datatools import  *

inframe = Frame(fromfile=sys.argv[1])
#print inframe.header

parts = inframe.uniqField('Participant')
items = inframe.uniqField('Verb')

zerframe = inframe.filter(('Case','1'))
accframe = inframe.filter(('Case','2'))

partframe = Frame(['Participant','Zero-Subj-Pref','Acc-Subj-Pref'])

for part in parts:
	accu = {}	
	accu['Participant'] = part
	fr = zerframe.filter(('Participant',part))		
	countS = 0
	countO = 0
	for d in fr.iterFrame():
		if d['Re-mention'] == '1':
			countS += 1
		elif d['Re-mention'] == '2':
			countO += 1
	accu['Zero-Subj-Pref']= str(countS-countO)
	
	fr = accframe.filter(('Participant',part))
	countS = 0
	countO = 0
	for d in fr.iterFrame():
		if d['Re-mention'] == '1':
			countS += 1
		elif d['Re-mention'] == '2':
			countO += 1
	accu['Acc-Subj-Pref']= str(countS-countO)
	partframe.addData(accu)
		
partframe.printFrame('holler-to-anova-participant.csv')


itemframe = Frame(['Item','Zero-Subj-Pref','Acc-Subj-Pref'])

for item in items:
	accu = {}	
	accu['Item'] = item
	fr = zerframe.filter(('Verb',item))		
	countS = 0
	countO = 0
	for d in fr.iterFrame():
		if d['Re-mention'] == '1':
			countS += 1
		elif d['Re-mention'] == '2':
			countO += 1
	accu['Zero-Subj-Pref']= str(countS-countO)
	
	fr = accframe.filter(('Verb',item))
	countS = 0
	countO = 0
	for d in fr.iterFrame():
		if d['Re-mention'] == '1':
			countS += 1
		elif d['Re-mention'] == '2':
			countO += 1
	accu['Acc-Subj-Pref']= str(countS-countO)
	itemframe.addData(accu)
		
itemframe.printFrame('holler-to-anova-item.csv')


