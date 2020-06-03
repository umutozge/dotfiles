#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Adapted from the example xls2csv.py from pyExcelerator
# Copyright (C) 2005 Kiseliov Roman

from pyExcelerator import *
import sys
import re
import subprocess
from mypy.datatools import Csv
from optparse import OptionParser

clp = OptionParser()
clp.add_option("-p",dest="pattern",default='.*')
clp.add_option("-t",dest="tar",action="store_true",default=False)
clp.add_option("-r",dest="prefix",default="")

options, args = clp.parse_args()

for sheet_name, values in parse_xls(args[0], 'cp1251'): # parse_xls(arg) -- default encoding
		matrix = [[]]
		pattern = re.compile(".*("+options.pattern+").*")
		outfilename = pattern.search(sheet_name).group(1)+".csv"
		print 'Sheet = "%s"' % sheet_name.encode('cp866', 'backslashreplace')
		print '----------------'

		for row_idx, col_idx in sorted(values.keys()):
			v = values[(row_idx, col_idx)]
			if isinstance(v, unicode):
				v = v.encode('cp866', 'backslashreplace')
			else:
				v = str(v)
			last_row, last_col = len(matrix), len(matrix[-1])
	
			while last_row < row_idx:
				matrix.extend([[]])
				last_row = len(matrix)
	
			while last_col < col_idx:
				matrix[-1].extend([''])
				last_col = len(matrix[-1])
	
			matrix[-1].extend([v])
   	        
# 		csvrows=[]
# 		for row in matrix:
# 			csvrows.append(','.join(row))
			
		Csv(matrix,'w').writeToFile(outfilename)
		print outfilename+'\n'
		print 'written\n'


if options.tar:
	p = subprocess.Popen("date +%F",shell=True,stdout=subprocess.PIPE)
	date = p.stdout.readlines()[0].strip()
	p.wait()
	p = subprocess.Popen("ls *.csv",shell=True,stdout=subprocess.PIPE)
	files = [x.strip() for x in p.stdout.readlines()]
	p.wait()
	fn = options.prefix+date+".tgz"
	arglist=["tar","-z","-c","-v","-f",fn]+files
	subprocess.call(arglist)
	subprocess.call(["rm"]+files)
