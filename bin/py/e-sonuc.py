#!/usr/bin/env python

import sys
import os
import subprocess
import re

def procpdf(pdf):
	infile = open('pdfs/'+pdf,'r')
	p = subprocess.Popen('pdftotext -layout pdfs/'+pdf+' -',shell=True,stdout=subprocess.PIPE)
	return p.stdout.readlines()

def proctext(txl):
	l = txl.pop(0)
	date = ''
	while True:
		m = datepattern.search(l)
		if m:
			date = list(m.groups())
			date.reverse()
			date = '-'.join(date)
			break
		l = txl.pop(0)
			
	while l.find(query) == -1: 
		try:
			l = txl.pop(0)
		except IndexError:
			return None	
	prev = l
	next = txl.pop(0)
	res = ''
	if next.startswith('           '):
		res = next	
	else:
		res = prev
	return date,valpattern.search(res).group(1)
	  
query = sys.argv[1]
pdfs = os.listdir('pdfs/')
pdfs.sort()
valpattern  = re.compile("[^\d]+([,\d]+)")
datepattern = re.compile("rnek T:(\d\d)/(\d\d)/(\d\d\d\d)") 

plist = []
for p in pdfs:
	try:
		date,val = proctext(procpdf(p))
		plist.append((date+'\t'+val+'\n').replace(',','.'))
	except TypeError:
		pass

plist.sort()
plist.insert(0,'Date\t'+query+'\n')

prevv=0

dfile = open(query+'-degisim.csv','w')

for i in plist:
	try:
		d,v = i.split('\t')
		fv = float(v)
		dfile.write(d+'\t'+str(fv-prevv)+'\n')
		prevv = float(v)
	except ValueError:
		pass
	print i,



