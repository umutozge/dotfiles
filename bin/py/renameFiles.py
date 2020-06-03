#!/usr/bin/env python

import sys
import os
import re
from optparse import OptionParser


clp=OptionParser()

clp.add_option('-p',dest='pat', help='pattern')
clp.add_option('-r',dest='repl', help='replacement string')

opts, args = clp.parse_args()

pattern = re.compile(opts.pat)

dl =  os.listdir(os.getcwd()) #get directory listing

for d in dl:
	newname = re.sub(pattern,opts.repl,d)	
	if newname == d:
		pass
	else:
		os.rename(d,newname)
		sys.stderr.write('\n'+d+' to '+ newname+'\n')
