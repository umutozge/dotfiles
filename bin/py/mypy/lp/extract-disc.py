#!/usr/bin/python
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import nltk
import re
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


def consPattern(query, boffset, aoffset):
	query = re.sub(r'\.',r'\\.',query)
	return "<.*>{"+ boffset+"} " + " ".join(["<"+word+">" for word in query.split(" ")]) + " <.*>{" + aoffset +"}"


try:
	opts, args = getopt.getopt(sys.argv[1:], "s:b:a:t:")
except getopt.GetoptError:
	print "Usage: [-s <search_item_list> | <search text in 's>] -b <# of words before> -a <after>."
	sys.exit(2)


search_list_path = ''
before_offset = ''
after_offset = ''
search_text = ''

for opt , val in opts:
 	if '-s'== opt:
 		search_list_path =  val
	elif '-b' == opt:
		before_offset = val
	elif '-a' == opt:
		after_offset = val
	elif '-t' == opt:
		search_text = val

# Preparing the corpus file
print "Initializing the corpus file...",
path = os.getcwd()+ '/' + args[0]
lines = open(path,'r').readlines()
lines = [l.strip() for l in lines]
text = nltk.Text(lines)
print "Done."
########

if search_list_path != '':
	searchitemfile = open(search_list_path,'r')
elif search_text != '':
	regexp = consPattern(search_text,before_offset,after_offset)
	for hit in myfindall(text,regexp):
		print hit	
	sys.exit(0)
else:
	print "Usage: [-s <search_item_list> | <search text in 's>] -b <# of words before> -a <after>."
	sys.exit(2)

########




# Preparing the output
outfile= open(path+'.out',"w")
hitcount = 1
template = '0???? Text %d\n\n %s\n\n'

itemcount= 1

while True:
	item = searchitemfile.readline()
	if item != "":
		print "Processing item", itemcount, "...",
		regexp = consPattern(item,before_offset,after_offset)
		for hit in myfindall(text,regexp):
 			outfile.write( template % (hitcount, hit))
			hitcount = hitcount + 1
		print "Done."	
		itemcount = itemcount + 1
	else:
		break
