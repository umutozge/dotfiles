#!/usr/bin/env python

import sys
from mypy.datatools import  *

inframe = Frame(fromfile=sys.argv[1])
#print inframe.header

parts = inframe.uniqField('Pid')
cases = inframe.uniqField('Case')
refs = inframe.uniqField('Re-mention')
roles = inframe.uniqField('Role')
header=['Cat','Zero','Acc','Total']
outframe= Frame(header)

dat={\
'Sbj':{'Cat':'Sbj'},
'Obj':{'Cat':'Obj'},
'Both':{'Cat':'Both'},
'Other':{'Cat':'Other'}}

for h in header:
	for k in dat.keys():
		if h != 'Cat':
			dat[k][h]=0	

print dat

typtr={'1':'Sbj','2':'Obj','3':'Both','4':'Other'}
casetr={'2':'Acc','1':'Zero'}

for d in inframe.iterFrame():
	if d['Case'] in ['1','2'] and d['Re-mention'] != '99': 
		case = d['Case']	
		ment = d['Re-mention']
		dat[typtr[ment]][casetr[case]]+=1	

for d in dat.itervalues():
	outframe.addData(d)
		
outframe.printFrame('holler-table.csv')

# for d in inframe.iterFrame():
# 	if d['Case']=='1' or d['Case']=='2':
# 		print d['Sentence']
# 		print d['Response']
# 		print d['Re-mention']
# 		print '>>>>>>>>>>>>>>'
# 		print
# 		print
