#!/usr/bin/env python

import sys
import os
import re
import xlwt,xlrd
from copy import copy
from mypy.datatools import Frame, Csv 


def proc(file):
	pid = file[:-4]
	f = open(file,'r')
	flag = ''
	accbuf = []
	nombuf = []
	for l in f.readlines():
		if l.find('\n') == 0:
			continue
		elif l.startswith('Acc'):
			flag= 'accbuf'
		elif l.startswith('Nom'):
			flag= 'nombuf'
		else:
			eval(flag+".append(l.strip().split(','))")
	
	accframe = Frame(accbuf[0],accbuf[1:])
	nomframe = Frame(nombuf[0],nombuf[1:])	

	return proc_fr(accframe,pid),proc_fr(nomframe,pid)
	
def proc_fr(frame,pid):
	accu = {'Participant':pid}
	for cat in frame.uniqField('AOICat'):
		ff = frame.filter(('AOICat',cat))
		for i in [str(x) for x in range(1,100)]:
			accu['TW'+i+'-'+cat]=str(float(ff.data[0][i]))
	return accu
	

header=['Participant'] + reduce(lambda x,y:x+y,map(lambda x:['TW'+str(x)+'-'+y for y in ['Agent','Patient','Topic','Other']],range(1,100))) 
aresframe = Frame(header)
nresframe = Frame(header) 
outfilename=''

for f in sys.argv[1:]:
	if f.endswith('.csv'):
		a,n = proc(f)
		aresframe.addData(a)
		nresframe.addData(n)
	elif f.endswith('.xls'):
		outfilename=f[:21]


aresframe.printFrame(outfile=outfilename+'Long-Accusative.csv')
nresframe.printFrame(outfile=outfilename+'Long-Nominative.csv')

# wb = xlwt.Workbook()
# accsh = wb.add_sheet('Accusative')
# nomsh = wb.add_sheet('Nominative')
# aresframe.printFrame(filename=outfilename,outfile=wb,sheet=accsh)
# nresframe.printFrame(filename=outfilename,outfile=wb,sheet=nomsh)

#resframe.printFrame(outfile)

#def printFrame(self,outfile=None,sheetname=None,filename=None,rowoffset=0,empty="",delimiter=','):
