#!/usr/bin/env python

import sys
from mypy.datatools import Frame

fnlist = sys.argv[1:]

for fn in fnlist:
	fr =  Frame(fromfile=fn) 
	fr.addField('ExpList','Subject',fn[0])
	fr.printFrame(fn)
