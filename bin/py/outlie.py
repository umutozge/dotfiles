#!/usr/bin/env python

from mypy.datatools import Frame, Csv
from mypy.utils import strToFloat, sdev, mean
import sys

def _procOut(frm):
	rt=[[],[],[],[],[],[]]			
	mn=[None,None,None,None,None,None]			
	sd=[None,None,None,None,None,None]			
	for d in frm.iterFrame():
		for i in range(1,7):
			if d['S'+str(i)+'res'] != '':	
				rt[i-1].append(strToFloat(d['S'+str(i)+'res']))

	for i in range(6):
		if rt[i] != []:
			mn[i] = mean(rt[i])
			sd[i] = sdev(rt[i])	
	
	outvals= [0.0,0.0,0.0,0.0,0.0,0.0]
	outcounts= [0,0,0,0,0,0]			
	for d in frm.iterFrame():	
		for i in range(6):
			crt_str=d['S'+str(i+1)+'res']
			if crt_str != '':
				crt = float(crt_str)
				if crt > (mn[i] + 2*sd[i]) or crt < (mn[i] - 2*sd[i]):
					outvals[i]=outvals[i] + crt
					outcounts[i]=outcounts[i]+1
	
	newmn=[None,None,None,None,None,None]
	for i in range(6):
		if rt[i] != []:
			newmn[i]=(sum(rt[i])-outvals[i])/(len(rt[i])-outcounts[i])

	for d in frm.iterFrame():	
		for i in range(6):
			crt_str=d['S'+str(i+1)+'res']
			if crt_str != '':
				crt = float(d['S'+str(i+1)+'res'])
				if crt > (mn[i] + 2*sd[i]) or crt < (mn[i] - 2*sd[i]):
					replacements.addData([[d['Subject'],d['Group'],d['Trial'],d['Condition4'],str(i+1),crt,newmn[i]]])
					d['S'+str(i+1)+'res']=newmn[i]	


def procOut(frm,labA,listA, labB, listB):
	for a in listA:
		for b in listB:
			sys.stderr.write("Processing  %s and %s...\n"%(a,b))
			newframe = frm.filter((labA,a),(labB,b))
			_procOut(newframe)


def reportOut(frm,key,fname=""):
	keys = frm.uniqField(key)
	header = [key,'Outliers','Total','Percent']
	retval = Frame(header)
	for k in keys:
		total=0
		for d  in frm.filter((key,k)).iterFrame():
			for i in range(6):
				if d['S'+str(i+1)+'res'] != '':
					total = total + 2

		outs= len(replacements.filter((key,k)).iterFrame())
		retval.addData([[k,str(outs),str(total),str(float(outs)/float(total)*100)]])	
	
	retval.printFrame(fname+'outliers-per-'+key+'.csv')



subj='Subject'
cond='Condition4'
group='Group'
trial='Trial'

frame = Frame(fromfile=sys.argv[1])


subjects= frame.uniqField(subj)
conditions= frame.uniqField(cond)
groups=  frame.uniqField(group)
trials= frame.uniqField(trial)

for g in groups:
	replacements = Frame(['Subject','Group','Trial','Condition4','Segment','OldRT','NewRT'])
	sys.stderr.write('Processing group_'+g+'\n')
	gframe= frame.filter((group,g))
	gframe.printFrame('Grp_'+g+'-data-in.csv')
	procOut(gframe,trial,trials,cond,conditions)
	fname='Grp_'+g+'-'
	reportOut(gframe,'Trial',fname)
	reportOut(gframe,'Condition4',fname)
	replacements.printFrame('Grp_'+g+'-outliers.csv')
	gframe.printFrame('Grp_'+g+'-data-out.csv')

# procOut(frame,subj,subjects,cond,conditions)
# reportOut(frame,'Group')
# reportOut(frame,'Condition4')
# replacements.printFrame('outliers.csv')
# frame.printFrame('data-out.csv')
