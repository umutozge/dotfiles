#!/usr/bin/python

from optparse import OptionParser
import sys

clparser = OptionParser()
(opts, args) = clparser.parse_args() 

infile = open(args[0],'r')

tokens = infile.readlines()

for token in tokens:
	token = token.strip()
	if token.startswith('<') & token.endswith('>'):
		print token
	else:
		parses = token.split()
		print '<word morph="' + parses[1] + '">' + parses[0] + '</word>'
