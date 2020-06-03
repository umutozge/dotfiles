#!/usr/bin/python

from matatools import *
from optparse import OptionParser 
import umut

clparser = OptionParser()	
opts, args = clparser.parse_args()
incsv = Csv(args[0])

rows = incsv.getRows()
f = Frame(rows[0],rows[1:])


conds=f.uniqField("Condition")


datalist = []
subjects = f.uniqField("Subject")

for s in subjects: 
 	fs = f.filter([["Subject",s]])
	for c in conds:
		data = {"Subject":s, "Condition":c, "S1":[], "S2":[], "S3":[], "S4":[], "S5":[]} 
		data["AgeGroup"]= fs.iterFrame()[0]["AgeGroup"]
		if int(data["AgeGroup"]) > 1:
			data["Group"] = 2
		else:
			data["Group"] = 1
		fc = fs.filter([["Condition",c]])
		if fc.isEmpty():
			continue	
		for d in fc.iterFrame():	
			for x in [1,2,3,5]:
				data["S"+str(x)].append(d["Segment"+str(x)])
			if d["Segment4a"] =="":
				data["S4"].append(d["Segment4b"])
			else:
				data["S4"].append(d["Segment4a"])

		for d in range(1,6):
			if data["S"+str(d)][0] == "":
				data["S"+str(d)]= ""
			else:
				data["S"+str(d)]= umut.mean(data["S"+str(d)])
		datalist.append(data)
	
header = ["Subject", "AgeGroup","Group","Condition","S1","S2","S3","S4","S5"]
outframe = Frame(header,datalist)	
outframe.printFrame("subj-cond-rt-results.csv")
