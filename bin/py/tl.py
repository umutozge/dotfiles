#!/usr/bin/env python

from optparse import OptionParser
from tlog import tlog

cl = OptionParser()
cl.usage='%prog [-sr]\n\nIf no option is given, logging starts or stops according to the current status.'
cl.epilog='\n'
cl.add_option('-s', '--status', dest='mode', action='store_const', const='status', default='log', help='print the status, do not log.')  
cl.add_option('-r', '--report', dest='mode', action='store_const', const='report', default='log', help='report the logging data.')  

opts,args = cl.parse_args()
try:
	tlog(opts.mode,args[0])
except IndexError:
	tlog(opts.mode)
