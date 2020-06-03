#!/usr/bin/python
import nltk, re
import os
import getopt
import sys


def myfindall(text, regexp):
	if "_token_searcher" not in text.__dict__:
		text._token_searcher = nltk.text.TokenSearcher(text)

	hits = text._token_searcher.findall(regexp)
	hits = [' '.join(h) for h in hits] 
	return hits
# 	return nltk.text.tokenwrap(hits, "; ") 



try:
	opts, args = getopt.getopt(sys.argv[1:], "")
except getopt.GetoptError:
	sys.exit(2)

path = os.getcwd()+ '/' + args[0]

lines = open(path,"r").readlines()

lines = [l.strip() for l in lines]


text = nltk.Text(lines)

results = myfindall(text,r'<.*>{3,20} <bir> <.*>{2,4} <\.> <.*>{60}')


outfile= open(path+'.out',"w")

dcount= 1

template = 'Discourse %d\n %s\n\n'

for result in results:
 	outfile.write( template % (dcount,str(result)))
	dcount = dcount + 1
