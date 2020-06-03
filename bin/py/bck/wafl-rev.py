#!/usr/bin/python

from mypy.datatools import Frame, Csv
import subprocess
import re
import sys
from mypy import utils 

class Wafl:
	
	def __init__(self):
		self.abstracts=[]	
	def addAbstract(self,abstract):
		self.abstracts.append(abstract)
	def getAbstract(self,no):
		for abs in self.abstracts:
			if abs.no==str(no):
				return abs
	def reportAbstracts(self):
		accum=[["No","Mean","Scores","Name","Title"]]
		for abs in self.abstracts:
			accum.append([abs.no,str(abs.mean),'"'+",".join([" "+str(x) for x in abs.scores])+'"','"'+abs.author+'"',abs.title])
		return accum

class Abstract:
	def __init__(self,no,author,title,afil,email):
		self.no = no
		self.author = author
		self.title = title
		self.afil = afil
		self.email = email
		self.reviews = []
		self.revcount = 0
		self.scores = []
		self.mean = 0
	def addReview(self,review):
		self.reviews.append(review)
		self.scores.append(float(review.score))
		self.mean=utils.mean(self.scores)
		self.revcount=len(self.scores)
	
class Review:
	
	def __init__(self,reviewer,abstract,score,comment="",):
		self.reviewer=reviewer
		self.abstract = abstract
		self.score = score
		self.comment = comment


class Reviewer:
	
	def __init__(self,id,name,email):
		self.id=id
		self.name=name
		self.email=email

def compileReviews(absframe, flag=None):
	for d in absframe.iterFrame():
		abs = wafl.getAbstract(d["No"])
		dec = {None:"visible","a":"anonym"}
		if len(d["No"]) == 1:
			no = "0"+d["No"]
		else:
			no = d["No"]
		out = open("reviews."+dec[flag]+"/"+no+".txt",'w')
		out.write("Score scale:\n\t0 Strongly reject\n\t1 Reject\n\t2 Accept\n\t3 Strongly accept\n")
		for revx, rev in enumerate(abs.reviews):
			if flag:  
				header=""
				reviewer = str(revx + 1)
			else:
				header=""
				reviewer = rev.reviewer.name
			out.write(header+"Reviewer: "+ reviewer+"\n"+rev.comment)
		out.close()

							
def incompletes(absframe):
	f = open("incompletes.txt",'w')
	for d in absframe.iterFrame():
		if len(d["Scores"].split(',')) < 3:
			revlist = subs.getData("No",d["No"])["Reviewer"].split(',')
			namedrevlist = [revs.getData("No",x)["Name"] for x in revlist]
			actrevlist = [x.reviewer.id for x in wafl.getAbstract(d["No"]).reviews]
			namedactrevlist =[revs.getData("No",x)["Name"] for x in actrevlist] 
		    			
			f.write("Abstract #%s %s\nDo not send to: %s\nReturned: %s\nNeeded: %s\n" % (d["No"],d["Title"],','.join(namedrevlist),','.join(namedactrevlist), 3-len(namedactrevlist)))
			f.write("\n")
	f.close()

if __name__ == "__main__":

	wafl = Wafl()	
	subs = Frame(fromfile="sublist.csv")
	revs = Frame(fromfile="active-revs.csv")

	for sub in subs.iterFrame():
		wafl.addAbstract(Abstract(sub["No"],sub["Name"],sub["Title"],sub["Affiliation"],sub["Email"]))
	for rev in revs.iterFrame():
		if rev["Status"]=="":
			continue	
		reviewer=Reviewer(rev["No"],rev["Name"],rev["Email"])
		infile = open('returns/'+rev["No"]+".resp",'r')	
		lines = infile.readlines()	
		line = lines.pop(0)
		comment=""
		score=""
		no=""
		while True:
			a = re.search('Abstract +#(\d+)',line)
			if a !=None:
				if no!="":
					abs=wafl.getAbstract(no)
					rev = Review(reviewer,no,score,comment)
					abs.addReview(rev)
				no = a.group(1)
				comment=""
				score=""
			a = re.search('Score: *([\d\.]+).*',line)
			if a !=None:
				score = a.group(1)
			comment += line

			try:
				line = lines.pop(0)
			except IndexError:
				abs=wafl.getAbstract(no)
				rev = Review(reviewer,no,score,comment)
				abs.addReview(rev)
				break

	absreport=wafl.reportAbstracts()
	absframe= Frame(absreport[0],absreport[1:])
 	absframe.printFrame(outfile="abstract-report.csv")
	incompletes(absframe)
	compileReviews(absframe)
	compileReviews(absframe,"a")


