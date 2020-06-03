#!/usr/bin/env python

import sys
from mypy.datatools import *
from optparse import OptionParser

clp = OptionParser()

clp.usage='%prog [options] input-file1.csv [input-file2.csv...]'
clp.add_option('-f',dest='header', help='header sep by comma; do NOT use spaces',default="Subject,TrialId,Condition,TimePeriod,AOICat,AOIStimulus,ClickAcc,ValidityLeftEye,ValidityRightEye,AOI1,AOI2,AOI3,AOI1Cat,AOI2Cat,AOI")

(opts,args) = clp.parse_args()

header = opts.header.split(',')

for fn in args:

	fr=Frame(fromfile=fn)
	fr.header = header
	fr.printFrame('red-'+fn)
	sys.stderr.write('Reduced '+fn+'\n')
