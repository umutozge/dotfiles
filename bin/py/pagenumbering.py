#!/usr/bin/env python

import sys

lines = open('authors.txt','r').readlines()
pagecount = 1

for l in lines:
	name, page = tuple(l.split(' '))
	print name, pagecount	
	pagecount += int(page)

