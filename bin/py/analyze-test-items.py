#!/usr/bin/env python2.6

from mypy.sentenceCompletion import Exp, procFile
from mypy.datatools import Csv, Frame


from optparse import OptionParser

clparser = OptionParser()	
opts, args = clparser.parse_args()
experiment = Exp() 

outframe = Frame(['Participant','TestItem','dieserein','RP Subj','RP Obj','RP Speaker','TP Subj','TP Obj','TP Speaker','TP Other'])


for arg in args:
	experiment.addTestItem(procFile(arg,outframe))
experiment.generateReport()

outframe.printFrame('trials.csv')

