#!/usr/bin/env python

import sys
from mypy.datatools import Frame
from optparse import OptionParser


def buildCount():
	count = dict()
	for f in ['fix','dur']:
		count[f]=dict()
		for i in data.uniqField('TimePeriod'):
			count[f][i] = dict()
			for t in data.uniqField('AOICat'):
				count[f][i][t]=0.0
			count[f][i]['total']=0.0
	return count

def procFrame(fieldlist,frame,accum):
	fieldname=fieldlist.pop(0)
	if fieldlist ==[]:
		computeFixations(frame,accum)
	else:
		for x in sorted(frame.uniqField(fieldname)):
			newframe = frame.filter((fieldname,x))
			procFrame(list(fieldlist),newframe,accum+[x])

def computeFixations(frame, accum):
	count = buildCount()
	for tw in sorted(frame.uniqField('TimePeriod')):
		laccum = list(accum)
		nframe = frame.filter(("TimePeriod",tw))
		current = "dummy"
		for d in nframe.iterFrame():
			#In computing fixation counts we just check whether there is a change in the gaze
			if d["AOICat"] != current:
				count['fix'][tw][d["AOICat"]] += 1
				count['fix'][tw]["total"] += 1
			current = d["AOICat"]
	
			#In computing duration we take every gaze into account
			count["dur"][tw][d["AOICat"]] += 16.7 #this is msec of gaze taking period of Tobii
			count["dur"][tw]["total"] += 16.7
		fix =[count['fix'][tw]["NP1"],count['fix'][tw]["NP2"],count['fix'][tw]["Other"]]	
		fixtotal = count['fix'][tw]["total"]
		try:
			fixperc = map(lambda x: '%.2f'%(x/float(fixtotal)*100),fix)
			dur =[count['dur'][tw]["NP1"],count['dur'][tw]["NP2"],count['dur'][tw]["Other"]]
			durtotal = count['dur'][tw]["total"]
			durperc = map(lambda x: '%.2f'%(x/float(durtotal)*100),dur)
		except ZeroDivisionError:
			laccum.extend([tw]+['NA']*14)	
		else:
			laccum.extend([tw]+fixperc+durperc+fix+[fixtotal]+dur+[durtotal])	
		outFrame.addData(laccum)


if __name__=='__main__':


	clparser = OptionParser()
	clparser.usage='%prog [options] input-file'
	clparser.add_option('-f', dest='fieldlist', metavar='FIELD LIST',\
	help="how to organize the fixation data, fields are separated with commas WITHOUT space, and no need to write 'TimePeriod'")
	clparser.add_option('-o', dest='outfile', default='out.csv', metavar='OUTFILE',\
	help='where to write the result')

	opts, args = clparser.parse_args()

	data = Frame(fromfile=args[0])

	fieldlist= opts.fieldlist.split(',')+['TimePeriod']
	header = fieldlist	+ ["PercNumFixToNP1","PercNumFixToNP2","PercNumFixToOther","PercDurFixToNP1","PercDurFixToNP2","PercDurFixToOther","NumFixToNP1","NumFixToNP2","NumFixToOther","NumFixTotal", "DurFixToNP1","DurFixToNP2","DurFixToOther","DurFixTotal"]


	outFrame = Frame(header)

	try:
		procFrame(fieldlist,data,[])
		outFrame.printFrame(opts.outfile)
	except:
		raise
		sys.exit(0)
	else:
		sys.stderr.write('\nDone\n')
		sys.exit(0)




