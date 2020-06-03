#!/usr/bin/python

from matatools import *
from optparse import OptionParser 
import umut

clparser = OptionParser()	
opts, args = clparser.parse_args()
incsv = Csv(args[0])

rows = incsv.getRows()
f = Frame(rows[0],rows[1:])


agrps=f.uniqField("AgeGroup")


datalist = []
items = f.uniqField("Item")
for it in items:
 	fit = f.filter([["Item",it]])
	for ag in agrps:
		data = {"AgeGroup":ag, "Item":it, "Condition":fit.iterFrame()[0]["Condition"], "S1":[], "S2":[], "S3":[], "S4":[], "S5":[]} 
		if int(ag) > 1:
			data["Group"] = 2
		else:
			data["Group"] = 1
		fag = fit.filter([["AgeGroup",ag]])
		if fag.isEmpty():
			continue	
		for d in fag.iterFrame():	
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
	
header = ["Item","AgeGroup","Group","Condition","S1","S2","S3","S4","S5"]
outframe = Frame(header,datalist)	
outframe.printFrame("item-group-rt-results.csv")
