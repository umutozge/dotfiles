#!/usr/bin/env python

import sys
import os
import re
import xlwt,xlrd
from copy import copy
from mypy.datatools import Frame, Csv 


def proc(file):
	print file
	exp = file[:-4]
	outifle = open(exp+'-u.csv','w')
	f = open(file,'r')
	lines = f.readlines()
	line = lines.pop(0).strip()
	while True:
		if line.find('TW') >= 0:
			frame = Frame(line.split(','))
			frame.addData(lines.pop(0).strip().split(','))
			frame.addData(lines.pop(0).strip().split(','))
			outifle.writelines(proc_fr(frame))
		try:
			line = lines.pop(0).strip()
		except IndexError:
			break

def proc_fr(frame):
	accu = []  
	for case in ['Nom','Acc']:
		accu.append(case+'\n')
		accu.append(reduce(lambda x,y:x+','+y,[frame.header[0]]+[str(x) for x in range(1,81)])+'\n')
		ff = frame.filter((frame.header[0],case))
		for cat in ['Agent','Patient','Topic','Other']:
			lineaccu = cat 
			for i in [str(x) for x in range(1,81)]:
				lineaccu += ','+ff.data[0]['TW'+i+'.'+cat]
			lineaccu+= '\n'
			accu.append(lineaccu)
	return accu
	

# header=['Participant'] + reduce(lambda x,y:x+y,map(lambda x:['TW'+str(x)+'-'+y for y in ['Agent','Patient','Topic','Other']],range(1,100))) 
# aresframe = Frame(header)
# nresframe = Frame(header) 
# outfilename=''

for f in sys.argv[1:]:
	if f.endswith('.csv'):
		proc(f)
# 		aresframe.addData(a)
# 		nresframe.addData(n)

# aresframe.printFrame(outfile=outfilename+'Long-Accusative.csv')
# nresframe.printFrame(outfile=outfilename+'Long-Nominative.csv')

# wb = xlwt.Workbook()
# accsh = wb.add_sheet('Accusative')
# nomsh = wb.add_sheet('Nominative')
# aresframe.printFrame(filename=outfilename,outfile=wb,sheet=accsh)
# nresframe.printFrame(filename=outfilename,outfile=wb,sheet=nomsh)

#resframe.printFrame(outfile)

#def printFrame(self,outfile=None,sheetname=None,filename=None,rowoffset=0,empty="",delimiter=','):
