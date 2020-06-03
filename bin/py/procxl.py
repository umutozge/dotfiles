#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import xlrd, xlwt 
import sys
import re
import csv
import subprocess
from mypy.datatools import Csv
from optparse import OptionParser

usage=" %prog [options] input-file.csv [input-file2.csv ...]\n\t%prog [options] input-file.xls\n\n%prog operates according to its input.\nIf it's given a set of csv files, it turns them into a single xls file.\nIf it's given an xls file, it turns xls's sheets to csv's."
clp = OptionParser(usage=usage)
clp.add_option("-p",dest="pattern",default='.*',help="a re pattern to be used in constructing csv file names out of sheet names.")
clp.add_option("-t",dest="tar",action="store_true",default=False, help="put the generated csv files into a tar archive and delete the files.")
clp.add_option("-r",dest="prefix",default="results-",help="the prefix to be put in front of the date in tar file name and excel file.")

options, args = clp.parse_args()

me = sys.argv[0].split("/")[-1]

p = subprocess.Popen("date +%F",shell=True,stdout=subprocess.PIPE)
date = p.stdout.readlines()[0].strip()
p.wait()

if args[0].endswith("xls"):
	wb= xlrd.open_workbook(args[0])
	for name in wb.sheet_names():
 		pattern = re.compile(".*("+options.pattern+").*")
 		outfilename = pattern.search(name).group(1)+".csv"
		sh = wb.sheet_by_name(name)	
		rows=[]
		for rowindex in range(sh.nrows):
			rows.append(sh.row_values(rowindex))	
		
		outfile=open(outfilename,'w')
		for row in rows:
			line = []
			for cell in row:
				cell = unicode(cell).encode("utf8")
				if re.search(',',cell)!= None:
					line+=['"'+cell+'"']
				else:
					line+=[cell]
			outfile.write(','.join(line)+"\n")
		outfile.close()

	if options.tar:
		p = subprocess.Popen("ls *.csv",shell=True,stdout=subprocess.PIPE)
		files = [x.strip() for x in p.stdout.readlines()]
		p.wait()
		fn = options.prefix+date+".tgz"
		arglist=["tar","-z","-c","-v","-f",fn]+files
		subprocess.call(arglist)
		subprocess.call(["rm"]+files)

elif args[0].endswith("csv"):
	wb = xlwt.Workbook()	
	for filename in args:
		ws=wb.add_sheet(filename[:-4])
		csvreader= csv.reader(open(filename,'r'))
		for ri, row in enumerate(csvreader):
			for ci, val in enumerate(row):
				val = unicode(val).encode("utf8")
				ws.write(ri,ci,val)
	wb.save(options.prefix+date+".xls")

else:
	sys.stderr.write(me+": Unrecognized file extension!\n")
	sys.exit(1)
