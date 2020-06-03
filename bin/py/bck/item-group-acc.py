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
for ag in agrps:
 	filtered = f.filter([["AgeGroup",ag]])
	items = [x[:-5] for x in filtered.uniqField("Sound1")]
	for it in items:
		data = {"AgeGroup":ag, "Item":it, "Condition":"", "S1":[], "S2":[], "S3":[], "S4":[], "S5":[]} 
		local = filtered.filter([["Sound1",it]]).iterFrame()
		data["Condition"] = local[0]["Condition"]
		for d in local:	
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
	
header = ["Item","AgeGroup","Condition","S1","S2","S3","S4","S5"]
outframe = Frame(header,datalist)	
outframe.printFrame("item-group-rt-results.csv")
