#!/usr/bin/python
from optparse import OptionParser
from datatools import Frame, Csv
import subprocess
import umut
import os

def ag(x):
	if int(x) in [1, 2, 3, 12, 13, 16, 27, 28, 36, 40, 41, 42, 43, 44, 45, 46, 47]: 
		return "0" 
	elif int(x) in [5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 21, 22, 23, 24, 26, 30, 31, 32, 33, 34, 35]:	
		return "1" 
	elif int(x) in [102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138]:
		return "2"	 
	else:
		return None

def ag2g(x):
	if int(x) < 2:
		return "0"
	else:
		return "1"


p = subprocess.Popen("date +%F",shell=True, stdout=subprocess.PIPE)
date =  p.stdout.readlines()[0].strip()
p.wait()

clparser = OptionParser()	
opts, args = clparser.parse_args()
incsv = Csv(args[0],delimiter=',').getRows()

frame = Frame(incsv[0],incsv[1:])

frame.addField("AgeGroup")
frame.addField("Group")



for d in frame.iterFrame():
	a=ag(d["Subject"].strip())
	d["AgeGroup"]= a
	d["Group"]=ag2g(a)



for d in frame.iterFrame():
	if len(d["Condition"])==3:
		d["Condition"]=d["Condition"][0]+"2"
	elif d["Condition"]=="52" and d["Group"]=="0":
		d["Condition"]="51"

frame.printFrame("wmt-raw-trimmed-"+date+".csv")


cons=[str(x)+str(y) for x in [1,2,3,4,5] for y in [1,2]]
cond_corr=dict(zip(cons,["gp","gp","o","o","cm","cm","cd","cd","s","s"])) 
items = [str(x) for x in range(1,9)]
header = ["AgeGroup","Group","Item"]

cond=[]
for x in cons:
	gram =""	
	if x[-1]=="1":
		gram="g"
	elif x[-1]=="2":
		gram="u"
	cond.append("C"+x+cond_corr[x]+"_"+gram)

header.extend(cond)

itemres=Frame(header)



for ag in [str(x) for x in range(0,3)]: 
	filt_ag = frame.filter([["AgeGroup",ag]])
	for i in items:	
		row =[ag,ag2g(ag),i]
		for c in cons:
			filt_it = filt_ag.filter([["Item",cond_corr[c]+"_"+i],["Condition",c]])
			rts = filt_it.getField("RT")
			if rts != []:
				row.append(umut.mean(rts))
			else:
				row.append("")
		itemres.addData(row)		

itemres.printFrame("wmt-trimmed-item-analysis-"+date+".csv")
			
header = ["Subject","AgeGroup","Group"]+cond

subjres=Frame(header)

for s in frame.uniqField("Subject"):
	filt_sub=frame.filter([["Subject","^"+s+"$"]])
	ag= filt_sub.iterFrame()[0]["AgeGroup"]
	row =[s,ag,ag2g(ag)]
	for c in cons:
		filt_c = filt_sub.filter([["Condition",c]])
		rts = filt_c.getField("RT")
		if rts != []:
			row.append(umut.mean(rts))
		else:
			row.append("")
	subjres.addData(row)		



subjres.printFrame("wmt-trimmed-subject-analysis-"+date+".csv")

