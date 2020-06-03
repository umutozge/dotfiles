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
			count[f][i]['Total']=0.0
	return count

def procFrame(fieldlist,frame,accum):
	if fieldlist ==[]:
		computeFixations(frame,accum)
	else:
		fieldname=fieldlist.pop(0)
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
				count['fix'][tw]["Total"] += 1
			current = d["AOICat"]
			#In computing duration we take every gaze into account
			count["dur"][tw][d["AOICat"]] += 16.7 #this is msec of gaze taking period of Tobii
			count["dur"][tw]["Total"] += 16.7
		fix = []
		for x in aoiCats:
			fix.append(count['fix'][tw][x])
		fixtotal = count['fix'][tw]["Total"]
		try:
			fixperc = map(lambda x: '%.2f'%(x/float(fixtotal)*100),fix)
			dur = []
			for x in aoiCats:
				dur.append(count['dur'][tw][x])
			durtotal = count['dur'][tw]["Total"]
			durperc = map(lambda x: '%.2f'%(x/float(durtotal)*100),dur)

		except ZeroDivisionError:
			laccum.extend([tw]+['NA']*18)	
		else:
			laccum.extend([tw]+fixperc+durperc+fix+[fixtotal]+dur+[durtotal])	
		outFrame.addData(laccum)


if __name__=='__main__':


	clparser = OptionParser()
	clparser.usage='%prog [options] input-file'
	clparser.add_option('-f', dest='fieldlist', default='Subject,Item,Condition', metavar='FIELD LIST',\
	help="how to organize the fixation data, comma separated field names, WITHOUT space. No need to write 'TimePeriod' (default='Subject,Item,Condition'")
	clparser.add_option('-o', dest='outfile', default='out.csv', metavar='OUTFILE',\
	help='where to write the result')


	opts, args = clparser.parse_args()

	data = Frame(fromfile=args[0])

	timeWins = data.uniqField('TimePeriod')
	aoiCats = data.uniqField('AOICat')

	fieldlist = opts.fieldlist.split(',') 
	header = fieldlist + ['TimePeriod']

	for x in ['PercNumFixTo','PercDurFixTo','NumFixTo','DurFixTo']:
		for y in aoiCats:
			header.append(x+y)
		if not x.startswith('Perc'):
			header.append(x[:-2]+'Total')

	outFrame = Frame(header)
	try:
		procFrame(fieldlist,data,[])
		outFrame.printFrame(opts.outfile)
	except:
		raise
		sys.exit(0)
	else:
		sys.exit(0)
