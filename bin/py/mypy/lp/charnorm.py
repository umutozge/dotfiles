#!/usr/bin/python
from __future__ import division
import nltk, re, pprint
import string
import codecs
import os
import getopt
import sys

try:
	opts, args = getopt.getopt(sys.argv[1:], "")
except getopt.GetoptError:
	sys.exit(2)

path = os.getcwd()+ '/' + args[0]

lines = codecs.open(path,encoding='utf-8').readlines()

# Building a translation table
from_unicode=[350,351,220,252,286,287,304,305,214,246,199,231]
to_unicode=[u'S',u'S',u'U',u'U',u'G',u'G',u'I',u'I',u'O',u'O',u'C',u'C']

acc1=[]

for i in range(len(from_unicode)): 
	acc1 = acc1 + [(from_unicode[i-1],ord(to_unicode[i-1]))]

trans_table= dict(acc1)
#############################

accum=[]
count =0
total = len(lines)
print "There are", total, "lines in total."

for i in range(0,len(lines)-1):
	lines[i] = lines[i].strip().lower().translate(trans_table)
	count = count +1
	if (count % 10000) == 0:
		print '\r' + ' Processed', count/total*100, "%",

print "Writing file..."

outfile = open(path + ".out","w")

for line in lines:
	outfile.write(line.encode('utf8') + '\n')

print "Done!"
