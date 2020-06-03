#!/usr/bin/python

from mypy.datatools import Frame, Csv
import subprocess
import re

s=Csv("sublist.csv").getRows()
subs=Frame(s[0],s[1:])

dec = Csv("decisions.csv").getRows()
decs =Frame(dec[0],dec[1:]).iterFrame()

name_pattern = re.compile('^([\w-]+),\s+([\w-]+).*$')
subject="WAFL 8 Notification"

for dec in decs:
	
	email = subs.getData("No",dec["No"])["Email"]	
	
	surname, name = name_pattern.match(dec["Name"]).groups()
	title = dec["Title"]
	reviewfile = open("/home/tumuum/wafl/review/reviews.anonym/"+dec["No"].strip()+".txt",'r')
	reviews = "\n".join(reviewfile.readlines())
	body=""
	if dec["Status"].strip() =="o":
		body = "Dear %s,\n\nThank you for submitting the following abstract to WAFL 8:\n\n'%s'\n\nWe are pleased to let you know that your submission has been accepted as an oral presentation. Please find the reviewer scores and comments below.\n\nPlease note that you can send a revised abstract to be published on the conference site till April 13th.\n\nInformation about accommodation will be sent shortly.\n\nWe are looking forward to seeing you in Stuttgart.\n\nRegards,\n\nWAFL 8 Organizing Committee\n\n\n***REVIEWS***\n\n%s"%(name+" "+surname,title,reviews)
	elif dec["Status"].strip() == "r":
		body = "Dear %s,\n\nThank you for submitting the following abstract to WAFL 8:\n\n%s\n\nWe are sorry to inform you that we will not be able to include your submission in WAFL 8. Decisions were based on blind reviewer scores and comments. (We had every abstract reviewed by at least 3 reviewers, and majority of abstracts had 4). Please find your reviewer scores and comments below. Please feel free to contact us for any questions you might have concerning the review process.\n\nRegards,\n\nWAFL 8 Organizing Committee\n\n\n***REVIEWS***\n\n%s"%(name+" "+surname,title,reviews)
	elif dec["Status"].strip() == "p":
		body = "Dear %s,\n\nThank you for submitting the following abstract to WAFL 8:\n\n%s\n\nWe would like to inform you that your submission has been accepted as a poster presentation. Decisions were based on blind reviewer scores and comments. We had every abstract reviewed by at least 3 reviewers, and majority of abstracts had 4. Please find your reviewer scores and comments below.\n\nPlease note that you can send a revised abstract to be published on the conference site till April 13th.\n\nInformation about accommodation will be sent shortly.\n\nWe are looking forward to seeing you in Stuttgart.\n\nRegards,\n\nWAFL 8 Organizing Committee\n\n\n\n***REVIEWS***\n\n%s"%(name+" "+surname,title,reviews)
	elif dec["Status"].strip().startswith("a"):
		ran = dec["Status"].strip()[1]
		rank = ""
		if ran == "1":
			rank = "1st"
		elif ran == "2":
			rank = "2nd"
		elif ran == "3":
			rank = "3rd"
		else:
			rank = ran+"th"
	
		body = "Dear %s,\n\nThank you for submitting the following abstract to WAFL 8:\n\n%s\n\nWe would like to inform you that your submission has been accepted as an alternate presentation with the %s ranking on the cue. You are also very welcome to present your work as a poster, regardless of whether you find a place in the oral presentation sessions or not. Decisions were based on blind reviewer scores and comments. We had every abstract reviewed by at least 3 reviewers, and majority of abstracts had 4. Please find your reviewer scores and comments below.\n\nPlease note that you can send a revised abstract to be published on the conference site till April 13th.\n\nInformation about accommodation will be sent shortly.\n\nWe are looking forward to seeing you in Stuttgart.\n\nRegards,\n\nWAFL 8 Organizing Committee\n\n\n***REVIEWS***\n\n%s"%(name+" "+surname,title,rank,reviews)

	args = ["mutt"]
	address=email
	no = dec["No"]
	name=name
	out=open("body","w")
	empty=True
	out.write(body)	
	out.close()
	args.extend(["-s"+subject,"-ibody"]+["--",address])	
 	subprocess.call(args)
 


