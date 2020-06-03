#!/usr/bin/env python

from mypy.datatools import Frame, Csv
from mypy.utils import strToFloat, sdev, mean
import sys

frame = Frame(fromfile=sys.argv[1])

verbs = frame.uniqField('Verb')

output='Verb,"Acc effect","%NP1-zero","%NP1-acc"\n'


for verb in verbs:
	toverb = frame.filter(('Verb',verb))
	cond1 = toverb.getData('Condition','1')	
	cond2 = toverb.getData('Condition','2')	

	np2diff = float(cond2['% NP2']) - float(cond1['% NP2'])
	np1cond1 = float(cond1['% NP1'])
	np1cond2 = float(cond2['% NP1'])

	output += '%s,%f,%f,%f\n'%(verb,np2diff,np1cond1,np1cond2)

print output


# output2='Pid,NP1,NP2,Left,Right,Total,% NP1, % NP2, % Left, % Right,"NP1/NP2 Pattern","LR Pattern"\n'
# 
# parts = frame.uniqField('Pid') 
# 
# for part in  parts:
# 	pf = frame.filter(('Pid',part))
# 	left = 0
# 	right = 0
# 	np1 = 0
# 	np2= 0
# 	lrpat=''
# 	nppat=''
# 	for d in pf.iterFrame():
# 		if d['Response']=='1':
# 			resp = '1'
# 			np1 +=1
# 			nppat +='1-'
# 		elif d['Response']=='2':
# 			resp = '2'
# 			np2 +=1
# 			nppat +='2-'
# 		else:
#  			sys.stderr.write('Something strange!!')
# 		fc = d['First choice']
# 		sc = d['Second choice']
# 		if fc.startswith('NP'+resp):
# 			left +=1
# 			lrpat +='1-'
# 		elif sc.startswith('NP'+resp):
# 			right +=1 
# 			lrpat +='2-'
# 		else:
#  			sys.stderr.write('Something strange!!')
# 		total = float(np1 + np2)
# 		if not (total == float(left + right)):
#  			sys.stderr.write('Totals do not match!!')
# 		pnp1 = np1/total*100
# 		pnp2 = np2/total*100
# 		pleft = left/total*100
# 		pright = right/total*100
# 
# 	output2 += '%s,%d,%d,%d,%d,%f,%f,%f,%f,%f,%s,%s\n'%(part,np1,np2,left,right,total,pnp1,pnp2,pleft,pright,nppat,lrpat)
# 
# print output2





# for case in [1,2]:
# 
# 	cframe = frame.filter(('case',str(case)),  ('response','1'))
# 
# 	print 'case ' + str(case) + ' NP1: ' + str(len(cframe.iterFrame()))
# 
# 	cframe = frame.filter(('case',str(case)), ('response','2'))
# 	print 'case ' + str(case) + ' NP2: ' + str(len(cframe.iterFrame()))
	

