#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import argparse
import subprocess


if __name__ == "__main__":

	aparser = argparse.ArgumentParser()
	aparser.add_argument('-d', '--display', action='store_true', help='set for result display')
	aparser.add_argument('-l', '--lexpat', type=str, help='a pattern for the noun') 
	aparser.add_argument('-f', '--verbfilter', type=str, help='file for verbfilters') 
	aparser.add_argument('-q', '--query', type=str, help='query type') 
	aparser.add_argument('-n', '--name', type=str, help='output file prefix') 
#	aparser.add_argument('r', '--range', default='1.1-3.6'), help='range of corpus files to process: start-end')
	
	args = aparser.parse_args()

	display=(lambda x:{True:'-d',False:''}[x])(args.display)
	for i in [str(a)+'.'+str(b) for a in range(1,4) for b in range(1,7)]:
		p = subprocess.Popen("searchTreeBank.py -f %s -m %s-%s.xml -u %s-%s-undec.xml -q %s %s -l %s ~/sp/_mill%s.out.%s.xml"\
		%(args.verbfilter,args.name,i,args.name,i,args.query,display,args.lexpat,i[0],i[2]), shell=True)
 		exitstat= p.wait()
		if exitstat != 0:
			sys.exit(1)
	
	sys.exit(0)
