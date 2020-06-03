#!/usr/bin/python

from matatools import *
from optparse import OptionParser 
import umut

clparser = OptionParser()	
opts, args = clparser.parse_args()
incsv = Csv(args[0])

rows = incsv.getRows()
f = Frame(rows[0],rows[1:])


# construct item names
itnames=[]
for i in range(1,5):
	for j in range(1,9):
		itnames.append(str(i)+str(j))
cond_corres={"2":"2", "3":"3", "4":"4", "5":"5","a":"208" , "b":"308" , "c":"207", "d":"307" ,  "e":"217", "f":"317", "g":"218", "h":"318"}
conds = cond_corres.keys()
conds.sort()
segs =  ["S1","S2","S3","S4","S5"]
agrps= [0,1,2]
datalist = []
header = ["AgeGroup","Group", "Item"]
for k in conds:
	for s in segs:
		header.append("C"+cond_corres[k]+s)

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
			for i in [1,2,3,5]:
				ls = fc.getField("Segment"+str(i))
				if ls == []:
					data["C"+cond_corres[c]+"S"+str(i)]=""
				else:
					data["C"+cond_corres[c]+"S"+str(i)]= umut.mean(ls)

			f4a = fc.getField("Segment4a") 
			f4b = fc.getField("Segment4b") 
			if  len(f4a)==0 or f4a[0]== "0" or f4a[0]=="":
				if len(f4b)==0 or f4b[0]== "0" or f4b[0]=="":
					data["C"+cond_corres[c]+"S4"]=""
				else:
					data["C"+cond_corres[c]+"S4"]=umut.mean(f4b)
			else:
				data["C"+cond_corres[c]+"S4"]=umut.mean(f4a)
		datalist.append(data)
	
outframe = Frame(header,datalist)	
outframe.printFrame("ag-item-results.csv")
