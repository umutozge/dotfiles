#!/usr/bin/python

from matatools import *
from optparse import OptionParser 
import umut

clparser = OptionParser()	
opts, args = clparser.parse_args()
incsv = Csv(args[0])

rows = incsv.getRows()
f = Frame(rows[0],rows[1:])


f.addField("AgeGroup","Subject")

# consturct age group table
agcsv= Csv("../lib/age-group.csv")

rs = agcsv.getRows()

agtab= {}
for r in rs:
	agtab[r[0]]	= r[1]


for d in f.iterFrame():
	d["AgeGroup"]=agtab[d["Subject"]]

# construct item names


subjects = f.uniqField("Subject")
conds = f.uniqField("Condition")

subjects.sort()
conds.sort()

datalist=[]
tags= ["Correct","Incorrect","Accuracy"]
header = ["Subject","AgeGroup","Group"]
for c in conds:
	for t in tags:
		header.append("C"+c+t)

for s in subjects:
	fas = f.filter([["Subject",s]])
	data={"Subject":s,"AgeGroup":fas.iterFrame()[0]["AgeGroup"]}
	if int(data["AgeGroup"]) > 1:
		data["Group"] = 2
	else:
		data["Group"] = 1

	for c in  conds: 
		fc = fas.filter([["Condition",c]])	
		if fc.isEmpty():
			data["C"+c+"Correct"]= "" 
			data["C"+c+"Incorrect"]= "" 
			data["C"+c+"Accuracy"]= ""
			continue
		acc = fc.getField("Accuracy")	
		corr= acc.count("1")
		incorr= acc.count("0")
		tot = corr+incorr
		data["C"+c+"Correct"]= corr
		data["C"+c+"Incorrect"]= incorr
		data["C"+c+"Accuracy"]=float(corr)/float(tot)
	datalist.append(data)
		

outframe = Frame(header,datalist)	
outframe.printFrame("subject-accuracy-results.csv")
