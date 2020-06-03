import csv
import re

import copy

from mypy import utils

import sys

from mypy.datatools import Frame, Csv
from optparse import OptionParser

class Exp:

	def __init__(self,id="experiment",data=[]):
		"data is a list of TestItem's"
		self.data = data
		self.id = id
		self.report = []
		self.ttl={} # totals
		self.ttlps={} # totals per sentence
		for f in "dieser","ein":
			for r in "S","O","Speaker","Other":
				frame = Frame([f]+["S"+str(x) for x in range(1,7)]+["Total"],[{f:r}])
				for s in "Topic Shift","Topic Pers", "Ref Pers":
					frame.addData({f:s})
				self.ttlps["tps-"+r.lower()+"-"+f[0]] = frame
		for r in "S","O","Speaker","Other":
			frame = Frame([r,"dieser","ein"])
			for s in "Topic Shift","Topic Pers", "Ref Pers":
				frame.addData({r:s})
			self.ttl["t-"+r.lower()] = frame

	def addTestItem(self, ti):
		self.data.append(ti)

	def getTestItem(self,id):
		for ti in self.data:
			if ti.id == id:
				return ti 
		return None

	def generateReport(self):
		report=[]
		for ti in self.data:
			sys.stderr.write("Processing test item "+ti.id+"...\n")
			# topic pers
			sys.stderr.write("Reporting topic persistence...\n")
			tp =ti.reportTopicPers()
			for t in tp:
				self._compTotalsPS(t,"Topic Pers","TP")	
				report.extend(t.printFrame(empty="0"))
				report.extend([""])
			self.report.extend([[],[]])
			# ref pers
			sys.stderr.write("Reporting referential persistence...\n")
			rp =ti.reportRefPers()
			for t in rp:
				self._compTotalsPS(t,"Ref Pers","RP")	
				report.extend(t.printFrame(empty="0"))
				report.extend([""])
			self.report.extend([[],[]])
			# topic shift 
			sys.stderr.write("Reporting topic shift...\n")
			ts =ti.reportTopicShift()
			for t in ts:
				self._compTotalsPS(t,"Topic Shift","TS")	
				report.extend(t.printFrame(empty="0"))
				report.extend([""])
			report.extend([[],[]])
 			outcsv = Csv(report,"w")
 			outcsv.writeToFile(ti.id+"-analysis.csv")	
			report=[]
		self._reportTotals()

	def _reportTotals(self):
		"""Totals per sentence"""
		report =[]
		reportcum =[]
		for de in "dieser","ein":
			for r in "S","O","Speaker","Other":
				fttlps = self.ttlps["tps-"+r.lower()+"-"+de[0]]
				cumtlps = copy.deepcopy(fttlps)
				for d in cumtlps.data:
					if 'S1' in d.keys():
						before = 0
						for s in ['S'+str(x) for x in range(1,7)]:
							d[s] = d[s]+ before
							before = d[s]
						d['Total']=d['S6']
				for d in fttlps.data:
					if "S1" in d.keys():
						d["Total"] = utils.sumList([d[x] for x in d.keys() if x.startswith("S")])
				report.extend(fttlps.printFrame(empty=""))
				report.extend([[]])
				reportcum.extend(cumtlps.printFrame(empty=""))
				reportcum.extend([[]])
			report.extend([[],[]])
			reportcum.extend([[],[]])
 		outcsv = Csv(report,"w")
 		outcsv.writeToFile("tot-per-sent.csv")
 		outcsv = Csv(reportcum,"w")
 		outcsv.writeToFile("tot-per-sent-cum.csv")

		"""Totals per type"""
		typ = {'dieser':Frame(['dieser']+['S'+str(x) for x in range(1,7)]+['Total']),\
				'ein':Frame(['ein']+['S'+str(x) for x in range(1,7)]+['Total'])}
		for k in typ.keys():
			for a in "Topic Shift","Topic Pers","Ref Pers":
				data = dict()
				data[k]=a
				for i in range(1,7):
					data['S'+str(i)]=0
				data['Total']=0
				typ[k].addData(data)

		for k in self.ttlps.keys():
			tot = self.ttlps[k] 
			if k.endswith('e'):
				mode = 'ein'
			elif k.endswith('d'):
				mode = 'dieser'
			else:
				raise Exception 
			for a in "Topic Shift","Topic Pers","Ref Pers":
				row = tot.getData(mode,a)	
				for s in ['S'+str(x) for x in range(1,7)]:
					try:
						typ[mode].getData(mode,a)[s]+=row[s]
					except KeyError:
						pass	
		for k in typ.keys():
			for d in typ[k].data:
				d['Total']= utils.sumList([d['S'+str(x)] for x in range(1,7)])

		outcsv = Csv(typ['dieser'].printFrame()+[[],[]]+typ['ein'].printFrame(), mode='w')
		outcsv.writeToFile('tot-per-typ.csv')
		
		cum = copy.deepcopy(typ)

		for k in cum.keys():
			for d in cum[k].data:
				before = 0
				for s in ['S'+str(x) for x in range(1,7)]:
					d[s] = d[s]+ before
					before = d[s]
				d['Total']=d['S6']
		
		outcsv = Csv(cum['dieser'].printFrame()+[[],[]]+cum['ein'].printFrame(), mode='w')
		outcsv.writeToFile('tot-per-typ-cum.csv')

	
		"""Grand Total"""
		report = []
		for r in "S","O","Speaker","Other":
			fttl = self.ttl["t-"+r.lower()]
			for a in "Topic Shift","Topic Pers","Ref Pers":
				for de in "dieser","ein":
					if r == "Other" and a =="Ref Pers":
						continue
					fttl.getData(r,a)[de] = self.ttlps["tps-"+r.lower()+"-"+de[0]].getData(de,a)["Total"]
			report.extend(fttl.printFrame(empty=""))
			report.extend([[]])
 		outcsv = Csv(report,"w")
 		outcsv.writeToFile("totals.csv")


	def _compTotalsPS(self,frame,longname,shortname):
			corr = {"S":"Subj","O":"Obj","Speaker":"Speaker","Other":"Other"}
			de = frame.header[0]
			for r in "S","O","Speaker","Other":
				if shortname=="RP" and r =="Other":
					continue
				for i in range(1,7):
					si = "S"+str(i)
					try:
						second= frame.getData(de,shortname+" "+corr[r])[si]
					except KeyError:
						second=0
					try:
						self.ttlps["tps-"+r.lower()+"-"+de[0]].getData(de,longname)[si] += second
					except KeyError:
 						self.ttlps["tps-"+r.lower()+"-"+de[0]].getData(de,longname)[si] = second

class TestItem:
	def __init__(self,id,outframe):
		self.id=id[:-4]
		self.dieser_field=[]
		self.ein_field=[]
		self.outframe = outframe

	def addTrial(self, trial):
		self.outframe.addData(trial.writeOut())
		if trial.dieserein == "ein":
			self.ein_field.append(trial)
		elif trial.dieserein == "dieser":
			self.dieser_field.append(trial)


	def getTrials(self,fieldname):
		if fieldname == "dieser":
			return self.dieser_field
		else:
			return self.ein_field

	def getTrial(self,partname, fieldname=None):
		for trial in self.dieser_field:
			if trial.participant == partname:
				return (trial,"dieser")
		for trial in self.ein_field:
			if trial.participant == partname:
				return (trial,"ein")
		return None

	def reportTopicShift(self):
		"returns a pair of Frames (dieser,ein)"
		report= []
		corr={"s":"TS Subj", "o":"TS Obj","speaker":"TS Speaker","other":"TS Other"}
		for f in "dieser","ein":
			frame = Frame([f]+["S"+str(x) for x in range(1,7)]+["Total"], [{f:x} for x in "TS Subj","TS Obj","TS Speaker","TS Other"])
			for trial in self.getTrials(f):
				sents = trial.sentences
				t = "" # topic
				flags= {"s":True,"o":True,"speaker":True,"other":True}
				for ind, sent in zip(range(len(sents)),sents):
					ct = sent.getValue("topic").strip() # current topic
					if ct != t and ct != "" and flags[ct]:
						try:
							frame.getData(f,corr[ct])["S"+str(ind+1)] += 1
						except KeyError:
							frame.getData(f,corr[ct])["S"+str(ind+1)] = 1
						t = ct
						flags[ct] = False
			for key in corr.keys():
				d = frame.getData(f,corr[key])
				d["Total"] = utils.sumList([d[x] for x in d.keys() if x.startswith("S")])
			report.append(frame)
		return report

	def reportTopicPers(self):
		"returns a pair of Frames (ein, dieser)"
		report= []
		for f in "dieser","ein":	
			frame = Frame([f]+["S"+str(x) for x in range(1,7)]+["Total"], [{f:"TP Subj"},{f:"TP Obj"},{f:"TP Speaker"}, {f:"TP Other"}])
			for trial in self.getTrials(f):
				for ind, sent in zip(range(1,len(trial.sentences)+1),trial.sentences):
					topic = sent.getValue("topic",0).strip()	
					if topic.endswith('s'):
						try:
							frame.getData(f,"TP Subj")["S"+str(ind)] +=1
						except KeyError:
							frame.getData(f,"TP Subj")["S"+str(ind)] = 1
					elif topic == "oo" or topic =="o":
						try:
							frame.getData(f,"TP Obj")["S"+str(ind)] +=1
						except KeyError:
							frame.getData(f,"TP Obj")["S"+str(ind)] = 1
					elif topic == "speaker":
						try:
							frame.getData(f,"TP Speaker")["S"+str(ind)] +=1
						except KeyError:
							frame.getData(f,"TP Speaker")["S"+str(ind)] = 1
					elif topic == "other":
						try:
							frame.getData(f,"TP Other")["S"+str(ind)] +=1
						except KeyError:
							frame.getData(f,"TP Other")["S"+str(ind)] = 1
					elif topic == "":
						pass
					else:
						sys.stderr.write("Error in Topic_HS field: " + topic)
			for key in "Subj","Obj","Speaker","Other":
				d = frame.getData(f,"TP "+key)
				d["Total"]=0
				for i in range(1,7):
					try:
						v = d["S"+str(i)]
					except KeyError:
						continue	
					d["Total"]+= v 
			report.append(frame)	
		return report

	def reportRefPers(self):
		"returns a pair of Frames (dieser,ein)"
		report= [] 
		keys = "Subj","Obj","Speaker"
		keyss= "subj","obj","spk"
		for f in "dieser","ein":	
			frame = Frame([f]+["S"+str(x) for x in range(1,7)]+["Total"], [{f:"RP "+x} for x in keys])
			for trial in self.getTrials(f):
				for ind, sent in zip(range(len(trial.sentences)),trial.sentences):
					for kk, k in zip(keyss,keys):
						count = 0
						for i in range(4):
							value =sent.getValue(kk+"_pers",i).split('.')[0]
							try:
								count = count + int(value)
							except ValueError:
								pass
						try:
							frame.getData(f,"RP "+k)["S"+str(ind+1)] += count
						except KeyError:
							frame.getData(f,"RP "+k)["S"+str(ind+1)] = count
			for k in keys:
				d = frame.getData(f,"RP "+k)
				d["Total"] = utils.sumList([d["S"+ str(x)] for x in range(1,7)])
			report.append(frame)
		return report


class Trial:
	def __init__(self, participant, sentences,dieserein,ti):
		self.participant= participant
		self.dieserein=dieserein
		self.sentences= sentences
		self.ti = ti

		self.tp = self.compTopicPers()
		self.rp = self.compRefPers()
	
	def writeOut(self):
		"""returns a dictionary"""
		retval = dict()
		retval['Participant']=self.participant[1:]
		retval['TestItem']=self.ti
		retval['dieserein']=self.dieserein

		for k in "Subj","Obj","Speaker":
			retval['TP '+k]=self.tp['TP '+k]
			retval['RP '+k]=self.rp['RP '+k]
		retval['TP Other']= self.tp['TP Other']
		return retval

	def compTopicPers(self):
		retval = {'TP Subj':0,'TP Obj':0,'TP Speaker':0,'TP Other':0}
		for ind, sent in enumerate(self.sentences):
			topic = sent.getValue("topic",0).strip()	
			if topic.endswith('s'):
				retval["TP Subj"] +=1
			elif topic == "oo" or topic =="o":
				retval["TP Obj"] +=1
			elif topic == "speaker":
				retval["TP Speaker"] +=1
			elif topic == "other":
				retval["TP Other"] +=1
			elif topic == "":
				pass
			else:
				sys.stderr.write("Error in Topic_HS field: " + topic + self.participant)
		return retval 

	def compRefPers(self):
		retval= {'RP Subj':0,'RP Obj':0,'RP Speaker':0} 
		keys = "Subj","Obj","Speaker"
		keyss= "subj","obj","spk"
		for ind, sent in enumerate(self.sentences):
			for kk, k in zip(keyss,keys):
				count = 0
				for i in range(4):
					value =sent.getValue(kk+"_pers",i).split('.')[0]
					try:
						count = count + int(value)
					except ValueError:
						pass
				retval["RP "+k] += count

		return retval


class Sentence:
	def __init__(self,vector):
		"a Sentence is a four-tuple of dictionaries. First item is the matrix and the rest are subordinate clauses."
		header = ["form","topic","type_topic","subj_pers","subj_type","obj_pers","obj_type","spk_pers","form","subj_pers","subj_type","obj_pers","obj_type","spk_pers","form","subj_pers","subj_type","obj_pers","obj_type","spk_pers","form","subj_pers","subj_type","obj_pers","obj_type","spk_pers"]
		z = zip(header,vector)	
		self.data = (dict(z[0:8]),dict(z[8:14]),dict(z[14:20]),dict(z[20:26]))
	def getValue(self,key,clause=0):
		return self.getClause(clause)[key]
	def getClause(self, index):
		return self.data[index]


def procFile(filename,outframe):
	outframe=outframe
	incsv = Csv(filename,'r',delimiter=',',clean=True)
	rows = incsv.getRows()
	field_flag=""	
	p_pattern= re.compile('p(\d+)')
	ti = TestItem(filename,outframe)
	crow = ["DUMMY"]
	while len(rows) > 0:
		if (crow[0] == "dieser") or (crow[0] == "ein"):
			field_flag=crow[0]
			crow = rows.pop(0)
		elif crow[0].startswith("p") and len(crow[0]) < 5:
			accum = []	
			while crow[0].startswith("p") and len(crow[0]) < 5:
				accum.append(crow)
				try: crow = rows.pop(0) 
				except IndexError: break
			for item in accum:
				sentences = [Sentence(item[1:27]),\
							 Sentence(item[28:54]),\
							 Sentence(item[55:81]),\
							 Sentence(item[82:108]),\
							 Sentence(item[109:135]),\
							 Sentence(item[136:162])]
				ti.addTrial(Trial(item[0],sentences,field_flag,ti.id[2:]))
		else:
			try: crow = rows.pop(0)
			except IndexError: break	
	return ti
