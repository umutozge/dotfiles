#!/usr/bin/python

from matatools import *
from optparse import OptionParser 
import umut

clparser = OptionParser()	
opts, args = clparser.parse_args()
incsv = Csv(args[0])

rows = incsv.getRows()
f = Frame(rows[0],rows[1:])


items=f.uniqField("Item")
subjects = f.uniqField("Subject")
datalist = []

for s in subjects: 
 	fs = f.filter([["Subject",s]])
	for it in items:
		data = {"Subject":s, "Item":it, "S1":[], "S2":[], "S3":[], "S4":[], "S5":[]} 
		data["AgeGroup"]= fs.iterFrame()[0]["AgeGroup"]
		if int(data["AgeGroup"]) > 1:
			data["Group"] = 2
		else:
			data["Group"] = 1
		fi = fs.filter([["Item",it]])
		if fi.isEmpty():
			continue	
		data["Condition"]=fi.iterFrame()[0]["Condition"]
		for d in fi.iterFrame():	
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
	
header = ["Subject", "AgeGroup","Group","Item","Condition","S1","S2","S3","S4","S5"]
outframe = Frame(header,datalist)	
outframe.printFrame("subj-item-rt-results.csv")
