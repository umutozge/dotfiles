#!/usr/bin/env python

import sys
from mypy.datatools import Frame
from mypy import utils 

def numSort(listofstrings):
	listofints = [int(x) for x in listofstrings]
	listofints.sort()
	return [str(x) for x in listofints]

def listMerger(list):
	if not list:
		return []
	else:
		return list[0] + listMerger(list[1:])


inframe = Frame(fromfile=sys.argv[1])



subjects = numSort(inframe.uniqField('Subject'))
conditions = numSort(inframe.uniqField('Condition'))
segments = [str(x) for x in range(1,6)]
alist = [(lambda x: ['S'+x+'-'+y for y in conditions])(z) for z  in segments]

outframe = Frame(['Subject','Group'] + listMerger(alist))

for sub in subjects:
	subframe = inframe.filter(('Subject',sub))	
	datapoint = {'Subject':sub,'Group':subframe.uniqField('Group')[0]}
	for cond in conditions:
		condframe = subframe.filter(('Condition',cond))
		for seg in segments:
			if seg != '4':
				values = condframe.getField('Segment'+seg)
			else:
				values = condframe.getField('Segment4a')
				if not values or not values[0]:
					values = condframe.getField('Segment4b')

			if values and values[0]:
				values = [float(x) for x in values]	
				mean = utils.mean(values)
				datapoint['S'+seg+'-'+cond] = mean		
			else:
				datapoint['S'+seg+'-'+cond] = ''	
	print datapoint			
	outframe.addData(datapoint)	
	
outframe.printFrame('output.csv')

sys.exit()

