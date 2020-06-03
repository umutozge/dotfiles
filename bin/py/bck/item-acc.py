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
itnames=[]
for i in range(1,5):
	for j in range(1,9):
		itnames.append(str(i)+str(j))
cond_corres={"2":"2", "3":"3", "4":"4", "5":"5","a":"208" , "b":"308" , "c":"207", "d":"307" ,  "e":"217", "f":"317", "g":"218", "h":"318"}
conds = cond_corres.keys()
conds.sort()
agrps= [0,1,2]
tags= ["Correct","Incorrect","Accuracy"]
datalist = []
header = ["AgeGroup","Group", "Item"]
for c in conds:
	for t in tags:
		header.append("C"+cond_corres[c]+t)




for ag in agrps:
	fag = f.filter([["AgeGroup",str(ag)]])
	for it in itnames:
		data = {"AgeGroup":ag}
		if ag > 1:
			data["Group"] = 2
		else:
			data["Group"] = 1
		data["Item"] = it 
		for c in conds:
			fc = fag.filter([["Item",c+it]])
			if fc.isEmpty():
				data["C"+cond_corres[c]+"Correct"]= "" 
				data["C"+cond_corres[c]+"Incorrect"]= "" 
				data["C"+cond_corres[c]+"Accuracy"]= ""
				continue
			acc = fc.getField("Accuracy")	
			corr= acc.count("1")
			incorr= acc.count("0")
			tot = corr+incorr
			data["C"+cond_corres[c]+"Correct"]= corr
			data["C"+cond_corres[c]+"Incorrect"]= incorr
			data["C"+cond_corres[c]+"Accuracy"]=float(corr)/float(tot)
		datalist.append(data)
	
outframe = Frame(header,datalist)	
outframe.printFrame("item-accuracy-results.csv")
