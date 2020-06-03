#!/usr/bin/env python
import sys
import os
import time
from mypy.lp.deptools import * 
from xml.dom import minidom, pulldom

import curses
import locale

def procDisc(node):
	resp = displayDiscourse(node)
	if resp == ord('q'):
		stop()					
	elif resp == ord('y'):
		mmaxfile.write(node.toxml().encode('utf-8'))
		count['incl']+= 1
	elif resp == ord('u'):
		undecfile.write(node.toxml().encode('utf-8'))
		count['undec']+=1
	elif resp == ord('n'):
		count['reject']+=1
	else:
		procDisc(node)	


def displayDiscourse(node):
	stdscr.clear()
	stdscr.addstr(0,10,'Do you want to include the following discourse? [y(es)/n(o)/u(ndecided)/q(uit)]',curses.A_BOLD)
	stdscr.addstr(1,20,'Docs processed: %d\tDocs included: %d\tPercent completed: %f%%'%(count['disc'],count['incl'],float(count['disc']/count['total']*100)))

	stdscr.addstr(3,10,'')	
	try:
		for s in node.getElementsByTagName('s'):
			displaySentence(s)	
	except:
			stdscr.clear()
			stdscr.addstr(30,30,"Reduce xterm font.")
			stdscr.refresh()	
			return stdscr.getch()
	stdscr.refresh()
	return stdscr.getch()	


def displaySentence(sent):
	for node in sent.getElementsByTagName('w'):
		word = node.firstChild.wholeText
		if node.parentNode.nodeName == 's':
			if word[0].isalpha():
				stdscr.addstr(' '+word.encode('utf-8'), 0)
			else:
				stdscr.addstr(word.encode('utf-8'), 0)
		else:
 			stdscr.addstr(' '+word.encode('utf-8'), curses.A_REVERSE)


	
def stop():

	logfile.write('File:\t%s\nTo Mmax:\t%d\nUndecided:\t%d\nRejected:\t%d\nTotal:\t%d\n\n'%(args[0],count['incl'],count['undec'],count['reject'],count['total']))
	logfile.flush()
	logfile.close()
	mmaxfile.write('</c>')
	mmaxfile.flush()
	mmaxfile.close()	
	undecfile.write('</c>')
	undecfile.flush()
	undecfile.close()	


	curses.nocbreak()
	curses.echo()
	curses.endwin()

	sys.exit(0)

if __name__ == "__main__":

	locale.setlocale(locale.LC_ALL,"")
	
	clparser = OptionParser()
	clparser.add_option('-m', dest='mmaxfile', default='m.xml')
	clparser.add_option('-o', dest='offset', default='1')
	clparser.add_option('-u', dest='undecfile',default='u.xml')



	(opts, args) = clparser.parse_args()

	offset = int(opts.offset)

	infile = open(args[0], mode='r')

	logfile = open('filter.log','a')
# 	logfile.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></head><body>')		
	mmaxfile = open(opts.mmaxfile,mode='w')
	mmaxfile.write(u'<?xml version="1.0" encoding="UTF-8"?><c>'.encode('utf-8'))

	undecfile = open(opts.undecfile,mode='w')
	undecfile.write(u'<?xml version="1.0" encoding="UTF-8"?><c>'.encode('utf-8'))


	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()


	count = {'disc':0,'incl':0,'undec':0,'reject':0,'total':1}

	events = pulldom.parse(infile)
	sys.stderr.write('Initing....')
	p = subprocess.Popen("xmllint --format %s | grep -c '<d>' "%(args[0]),shell=True, stdout=subprocess.PIPE)
	count['total'] =  float(p.stdout.readlines()[0].strip())
	p.wait()
	sys.stderr.write('Done!')	

	for event , node in events:
		if event == 'START_ELEMENT' and node.tagName=='d': 
			count['disc']+=1	
			if count['disc'] >= offset:
				events.expandNode(node)
				try:
					procDisc(node)			
				except Exception as ex:
					curses.nocbreak()
					curses.echo()
					curses.endwin()
# 					logfile.write('last procesed doc'+ str(count['disc']))
					logfile.flush()
					undecfile.flush()
					mmaxfile.flush()
					raise
	stop()
	
