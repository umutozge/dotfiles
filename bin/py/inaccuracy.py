#!/usr/bin/env python
import sys
import os

from mypy.datatools import *


inframe= Frame(fromfile=sys.argv[1])
parts = inframe.uniqField('Participant')
parts = [int(x) for x in parts]
parts.sort()
parts = [str(x) for x in parts]

conds = inframe.uniqField('Condition')
items = inframe.uniqField('Item')

print 'Participant,AccCorrectPerc,AblCorrectPerc'
sys.stderr.write('Participant,AccWholePref,AblWholePref\n')
for p in parts:
	abl = len(inframe.filter(('Participant',p)).filter(('Condition','abl')))
	acc = len(inframe.filter(('Participant',p)).filter(('Condition','acc')))
	wabl = 2*abl - 3 
	wacc = 3 - 2*acc 
	print '%s,%i,%i'%(p,(3-acc)/3.0*100,(3-abl)/3.0*100) 
	sys.stderr.write('%s,%i,%i\n'%(p,wacc,wabl))


