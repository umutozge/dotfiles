#!/usr/bin/python

from datatools import Frame, Csv
import subprocess

revs=Frame(["No","Name","Email","Topic","Afil","Num"],Csv("revlist.csv").getRows())
s=Csv("sublist.csv").getRows()
subs=Frame(s[0],s[1:]).iterFrame()


subject="WAFL 8 Review--Please disregard the previous email"

for r in revs.iterFrame():
	body = "[Please ignore the previous email, due to an error in the attachments. Please take this version into consideration for your reviewing. Sorry for the inconvenience.]\n\nDear Prof. "+r["Name"].split(",")[0]+",\n\nWe would like to invite you to review the attached abstracts.\nPlease follow the instructions below:\n\n1) Use the scale:\n\n\t0 Strongly reject\n\t1 Reject\n\t2 Accept\n\t3 Strongly accept\n\n2) Indicate your score and comments (if any) in the space allocated below the abstract title replying to this email.\n\nWe would really appreciate if you can return your comments no later than 15th February.\n\nThank you very much for your kind cooperation.\n\nRegards,\n\nWAFL 8 Organizing Committee\n\n"
	args = ["mutt"]
	address=r["Email"]
	no = r["No"]
	name=r["Name"]
	file=r["Name"].split(",")[0]+".zip"
	zip=[]
	out=open("body","w")
	empty=True
	for s in subs:
		if r["No"] in [x.strip() for x in s["Reviewer"].split(",")]:	
			empty=False
			zip.append("-a../waflAbstracts/wafl8sub"+s["No"]+".pdf")
			body+="\nAbstract #"+s["No"]+": '"+s["Title"]+"'\nScore:\nComments:\n\n"
	out.write(body)	
	out.close()
	if not empty:	
		print no+","+name.split(",")[0]+","+address
		args.extend(["-s"+subject,"-ibody"]+zip+["--",address])	
  #		subprocess.call(args)
 


