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

results = myfindall(text,r'<bir> <.*>{2,4} <\.>')

print "Number of results before filtering:", len(results)


accum=[]
index=0
while index < len(results):
	if re.search(r'(var|yok|deGil| ol\w+ \.| \w+n[IiUu]n | \w+d[ae]n?| \w+[ea] \w+ \.)',results[index]) != None:
		accum.append(results.pop(index))
	else:
		index = index + 1


print "Number of results after filtering:", len(results)

outfile= open(path+'.out',"w")
logfile= open(path+'.log',"w")

dcount= 1

for res in results:
	outfile.write(res + '\n')
for acc in accum:
	logfile.write(acc + '\n')

# template = 'Discourse %d\n %s\n\n'
# 
# for result in results:
#  	outfile.write( template % (dcount,str(result)))
# 	dcount = dcount + 1
# 

