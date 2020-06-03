#!/usr/bin/python

import re
import os
import getopt
import sys

try:
	opts, args = getopt.getopt(sys.argv[1:], "")
except getopt.GetoptError:
	sys.exit(2)

inpath = os.getcwd() + "/" + args[0]
infile = open(inpath, "r")
outfile = open(inpath + ".xml", "w")


lines = [l.strip() for l in infile.readlines()] 

outfile.write('<?xml version="1.0" encoding="utf-8"?>\n')

for line in lines:
	if not (line.startswith("0") or line == ""):
		outfile.write("<discourse>\n")	
		for i in line.split(" "):
			outfile.write("\t<word>" + i +"</word>\n")
		outfile.write("</discourse>\n")	
