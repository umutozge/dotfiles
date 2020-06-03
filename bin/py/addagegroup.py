#!/usr/bin/python

from matatools import *
from optparse import OptionParser 


clparser = OptionParser()	
opts, args = clparser.parse_args()
incsv = Csv(args[0])

agcsv= Csv("age_group.csv")

rows = incsv.getRows()
rowsag = agcsv.getRows()
f = Frame(rows[0],rows[1:])
fag = Frame(rowsag[0],rowsag[1:])

for d in f.iterFrame():
	d["AgeGroup"] = fag.filter([["participant",d["Subject"]]]).iterFrame()[0]["age group"]

f.printFrame()
	
