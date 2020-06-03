#!/usr/bin/env python

import sys
import re
from mypy.datatools import Frame

def consHitTest(factors):
	quad=factors['QuadSlide.OnsetTime']
	def f(rtime):
		if int(rtime) <= int(quad) + int(factors['NP1Onset']):
			return 'Fixation'
		elif int(rtime) <= int(quad) + int(factors['AuxOnset']):
			return 'TW1'
		elif int(rtime) <= int(quad) + int(factors['VerbOnset']):
			return 'TW2'
		elif int(rtime) <= int(quad) + int(factors['NP2Onset']):
			return 'TW3'
		elif int(rtime) <= int(quad) + int(factors['NP2Offset']):
			return 'TW4'
		else:
			return 'TW5'
	return f


def consItemDict(file):
	retval = dict()
	lines = file.readlines()	
	factors = {'NP1Onset':0, 'NP2Onset':0 ,'AuxOnset':0, 'VerbOnset':0 , 'NP2Offset':0, 'QuadSlide.OnsetTime':0,'NP2Offset':0,'UpLeftImage':""}

	while True:
		try:
			line = lines.pop(0)
			if line.find('LogFrame Start') !=-1:
				factors = {'NP1Onset':0, 'NP2Onset':0 ,'AuxOnset':0, 'VerbOnset':0 , 'NP2Offset':0, 'QuadSlide.OnsetTime':0,'QuadSlide.OnsetDelay':0,'AnimSlide.OnsetTime':0,'AnimSlide.OnsetDelay':0'NP2Offset':0,'UpLeftImage':"",'UpRightImage':"",'LowCenterImage':""}
			m = pattern.match(line.strip())
			if m:
				key = m.group(1) 	
				if key in factors.keys():
					factors[key]=m.group(2)

			if line.find('LogFrame End') !=-1:
				hitFunc = consHitTest(factors)
				retval[factors['UpLeftImage']]=hitFunc
		except IndexError:
			return retval
		

pattern= re.compile('(.*): (.*)')

for file in sys.argv[1:]:

	incsv = open(file,'r')
	intxt = open(file[:-4]+'.text','r')
	
	itemDict = consItemDict(intxt)

	frame = Frame(fromfile=file)

	for d in frame.iterFrame():  
		d['TimePeriod']= itemDict[d['AOI1']](d['RTTime']) 
	
	frame.printFrame(file)
