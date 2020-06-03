#!/usr/bin/python

from mypy.datatools import Frame, Csv

ekey = 'r'

s=Csv("sublist.csv").getRows()
subs=Frame(s[0],s[1:])

dec = Csv("decisions.csv").getRows()
decs =Frame(dec[0],dec[1:]).iterFrame()

email = ""
for d in decs:
	if d["Status"].strip() != ekey:
		no = d["No"]
		em = subs.getData("No",no)["Email"]
		email = email + em + ",\n"

print email
