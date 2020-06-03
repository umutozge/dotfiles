#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time
from mypy.lp.deptools import * 
from xml.dom import minidom, pulldom

import curses
import locale

def procDisc(node,query):
	for idx, dt in enumerate(node.getElementsByTagName('t')):
		deptree = DepTree(dt)
		hit = eval(query + '(DepTree(dt))')		
		if hit:
			if opts.display:
				resp = displayDiscourse(node,hit,idx)									
	# 			linear=deptree.linearize()
	#  			resp=displaySentence(linear,hit)
				stdscr.clear()
				stdscr.addstr(20,40,'Processing, please wait...')
				stdscr.refresh()
				if resp == ord('q'):
					stop()					
				elif resp == ord('y'):
					writeDiscourse(node,hit,idx,mmaxfile,mmaxTBfile)
					count['incl']+=1
				elif resp == ord('u'):
					writeDiscourse(node,hit,idx,undecfile,undecTBfile)	
					count['undec']+=1
				elif resp == ord('n'):
					count['reject']+=1
					rejectTBfile.write(node.toxml().encode('utf-8'))
				else:
					procDisc(node,query)	
			else:
				writeDiscourse(node,hit,idx,mmaxfile,mmaxTBfile)
				count['incl']+=1
				

def displayDiscourse(node,hit,idx):
	stdscr.clear()
	stdscr.addstr(0,10,'Do you want to include the following discourse? [y(es)/n(o)/u(ndecided)/q(uit)]',curses.A_BOLD)
	stdscr.addstr(1,20,'Docs processed: %d\tDocs included: %d\tPercent completed: %f%%'%(count['disc'],count['incl'],float(count['disc']/count['total']*100)))

	stdscr.addstr(3,10,'')	

	for id, dt in enumerate(node.getElementsByTagName('t')):
		if id == idx:
			high = hit
		else:
			high = []
		displaySent(DepTree(dt).linearize(),high)	

	stdscr.refresh()
	return stdscr.getch()	

def displaySent(wlist,high):
	for w in wlist:
		at=0
		if not w.getAttribute('form') == '_':
			if int(w.getAttribute('ind')) in high:
				at = curses.A_BOLD
			if w.getAttribute('pos')=='Punc':
				try:
					stdscr.addstr(w.getAttribute('form').encode('utf-8'), at)
				except curses.error:
					pass
			else:
				try:
					stdscr.addstr(' '+ w.getAttribute('form').encode('utf-8'), at)
				except curses.error:
					pass

def displaySentence(wlist,high):
	stdscr.clear()
	stdscr.addstr(0,10,'Do you want to include the following sentence? [y(es)/n(o)/u(ndecided)/q(uit)]',curses.A_BOLD)
	stdscr.addstr(1,20,'Docs processed: %d\tDocs included: %d\tPercent completed: %f%%'%(count['disc'],count['incl'],float(count['disc']/tdisc*100)))

	stdscr.addstr(3,10,'')	

	for w in wlist:
		at=0
		if not w.getAttribute('form') == '_':
			if int(w.getAttribute('ind')) in high:
				at = curses.A_BOLD
			if w.getAttribute('pos')=='Punc':
				stdscr.addstr(w.getAttribute('form').encode('utf-8'), at)
			else:
				stdscr.addstr(' '+ w.getAttribute('form').encode('utf-8'), at)
	stdscr.refresh()
	return stdscr.getch()	

def writeDiscourse(node,hit,idx,file,tfile):
	file.write('<d>')	
	tfile.write(node.toxml().encode('utf-8'))
	for id, dt in enumerate(node.getElementsByTagName('t')):
		file.write('<s>')
		if id == idx:
			_writeSent(dt,hit,file)
		else:
			_writeSent(dt,None,file)
		file.write('</s>')
	file.write('</d>')

def _writeSent(dt,hit,file):
	nds = [(int(x.getAttribute('ind')), x) for x in dt.getElementsByTagName('n')]
	nds.sort()
	last = nds[-1][0]
	for idx,nd in nds:
		form = nd.getAttribute('form')
		if hit and idx==hit[0]:
			file.write('<bi>')
		if form != '_' and form != '':
			text = '<w pos="%s" infl="%s">%s</w>'%(nd.getAttribute('pos'),nd.getAttribute('infl'),form)
			file.write(text.encode('utf-8'))
		if idx == last and form !='.':
			text = '<w pos="Punc" infl="">.</w>'
			file.write(text.encode('utf-8'))
		if hit and idx == hit[-1]:
			file.write('</bi>')


def accCheck(tree):
	for n in tree.getElementsByTagName('n'):
		if n.getAttribute('pos') == 'Verb' and n.getAttribute('stem') != 'ol':
			object = n.heads('OBJECT', 'i', ('case','Acc'))
			if object and object.heads('DETERMINER', 'r', ('stem','bir')):
				if object.getAttribute('poss') == 'Pnon' or object.getAttribute('poss') == 'Apos' or object.heads('CLASSIFIER', 'i'): 
					return object.coverage()
				
def zeroCheck(tree):
	for n in tree.getElementsByTagName('n'):
		if n.getAttribute('pos') == 'Verb' and not isPassive(n):
			object = n.heads('OBJECT', 'i', ('case','Nom'))
			if object and object.heads('DETERMINER', 'r', ('stem','bir')):
				if object.getAttribute('poss') == 'Pnon' or object.getAttribute('poss') == 'Apos' or object.heads('CLASSIFIER', 'i'): 
					if verbCheck(n):
						return object.coverage()

def isPassive(node):
	return node.depends('DERIV','i',('stem','Hn')) or node.depends('DERIV','i',('stem','Hl'))

	
def verbCheck(node):
	stem = _getStem(node)
	for verb in verbs:
		if stem.startswith(verb):
			return True	
	return False

def _getStem(node):
	return node.getAttribute('stem').encode('utf-8')

def stop():
	logfile.write('File:\t%s\nTo Mmax:\t%d\nUndecided:\t%d\nRejected:\t%d\nTotal:\t%d\n\n'%(args[0],count['incl'],count['undec'],count['reject'],count['total']))
	logfile.flush()
	logfile.close()
	mmaxfile.write('</c>')
	mmaxfile.flush()
	mmaxfile.close()	
	mmaxTBfile.write('</tb>')
	mmaxTBfile.flush()
	mmaxTBfile.close()	
	undecfile.write('</c>')
	undecfile.flush()
	undecfile.close()	
	undecTBfile.write('</tb>')
	undecTBfile.flush()
	undecTBfile.close()	
	rejectTBfile.write('</tb>')
	rejectTBfile.flush()
	rejectTBfile.close()	

	curses.nocbreak()
	curses.echo()
	curses.endwin()
	sys.exit(0)

def expandVerbs(lst):
	accum = []
	for v in lst:
		if v.islower():
			accum.append(v)
		elif v.find('B') != -1:
			for x in ['a','ı','o','u']:
				accum.append(v.replace('B',x))
		elif v.find('F') != -1:
			for x in ['e','i','ü','ö']:
				accum.append(v.replace('F',x))
		elif v.find('D') != -1:
			for x in ['t','d']:
				accum.append(v.replace('D',x))
	return accum

if __name__ == "__main__":

	locale.setlocale(locale.LC_ALL,"")
	
	clparser = OptionParser()
	clparser.usage="%prog [options] input-file"
	clparser.add_option('-m', dest='mmaxfile', default="m.xml", metavar="FILE",\
	help="write the Mmax input to FILE (default: m.xml)")
	clparser.add_option('-o', dest='offset', default ="1", metavar="OFFSET",\
	help="start extracting from discourse OFFSET (default: 1)")
	clparser.add_option('-u', dest='undecfile', default="u.xml", metavar="FILE",\
	help="write the undecided discourses to FILE (default: u.xml)")
	clparser.add_option('-q', dest='query',\
	help="type of query, see the source for details")
	clparser.add_option('-d', dest='display',action='store_true',default=False,\
	help='set if you want results to be displayed for selection')

	(opts, args) = clparser.parse_args()
	offset = int(opts.offset)
	query = opts.query
	infile = open(args[0], mode='r')
	logfile = open('session.log','a')
	mmaxfile = open(opts.mmaxfile,mode='w')
	mmaxfile.write(u'<?xml version="1.0" encoding="UTF-8"?><c>'.encode('utf-8'))
	mmaxTBfile = open('tb-'+opts.mmaxfile,mode='w')
	mmaxTBfile.write(u'<?xml version="1.0" encoding="UTF-8"?><tb>'.encode('utf-8'))
	undecfile = open(opts.undecfile,mode='w')
	undecfile.write(u'<?xml version="1.0" encoding="UTF-8"?><c>'.encode('utf-8'))
	undecTBfile = open('tb-'+opts.undecfile,mode='w')
	undecTBfile.write(u'<?xml version="1.0" encoding="UTF-8"?><tb>'.encode('utf-8'))
	rejectTBfile = open('tb-rejected.xml',mode='w')
	rejectTBfile.write(u'<?xml version="1.0" encoding="UTF-8"?><tb>'.encode('utf-8'))

	verbs = []
	if query =="zeroCheck":
		vfile = open('verbs-small.txt','r')
		for line in vfile.readlines():
			verbs.append(line.strip())
# 	verbs = expandVerbs(verbs)
# 

	#Display stuff starts here
	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()

	sys.stderr.write('Initing....')
	count = {'disc':0,'incl':0,'undec':0,'reject':0,'total':1}
	events = pulldom.parse(infile)
	p = subprocess.Popen("xmllint --format %s | grep -c '<d>' "%(args[0]),shell=True, stdout=subprocess.PIPE)
	count['total'] =  float(p.stdout.readlines()[0].strip())
	p.wait()
	sys.stderr.write('Done!\n')
	

	for event , node in events:
		if event == 'START_ELEMENT' and node.tagName=='d':
			count['disc'] += 1
			if count['disc'] > offset:
				events.expandNode(node)
				try:
 					procDisc(node,query)			
				except Exception as ex:
					curses.nocbreak()
					curses.echo()
					curses.endwin()
					logfile.write('\n\nlast proccesed doc'+ str(count['disc']))
					logfile.flush()
					undecfile.flush()
					mmaxfile.flush()
					raise
	stop()
	
