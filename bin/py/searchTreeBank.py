#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time
import re
from mypy.lp.deptools import * 
from xml.dom import minidom, pulldom


import curses
import locale

def procDisc(node,query):
	for idx, dt in enumerate(node.getElementsByTagName('t')):
		dep_tree = DepTree(dt)
		hit = eval(query + '(dep_tree)')
		if hit and checkLex(hit,dep_tree):
			if opts.display:
				resp = displayDiscourse(node,hit,idx)									
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
				

def checkLex(inds,dt):
	"""takes a set of indices and a dependency tree"""
	words=dt.linearize()
	lex =[] 
	for w in words:
		if w.getAttribute('form') != '_' and int(w.getAttribute('ind')) in inds:
			lex.append(w.getAttribute('form').encode('utf-8'))
	logfile.write(' '.join(lex)+'\n')
	return lexpattern.search(' '.join(lex))

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

# def displaySentence(wlist,high):
# 	stdscr.clear()
# 	stdscr.addstr(0,10,'Do you want to include the following sentence? [y(es)/n(o)/u(ndecided)/q(uit)]',curses.A_BOLD)
# 	stdscr.addstr(1,20,'Docs processed: %d\tDocs included: %d\tPercent completed: %f%%'%(count['disc'],count['incl'],float(count['disc']/tdisc*100)))
# 
# 	stdscr.addstr(3,10,'')	
# 
# 	for w in wlist:
# 		at=0
# 		if not w.getAttribute('form') == '_':
# 			if int(w.getAttribute('ind')) in high:
# 				at = curses.A_BOLD
# 			if w.getAttribute('pos')=='Punc':
# 				stdscr.addstr(w.getAttribute('form').encode('utf-8'), at)
# 			else:
# 				stdscr.addstr(' '+ w.getAttribute('form').encode('utf-8'), at)
# 	stdscr.refresh()
# 	return stdscr.getch()	

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
		if n.getAttribute('pos') == 'Verb' and not isPassive(n) and verbCheck(n):
			object = n.heads('OBJECT', 'i', ('case','Nom'))
			if object and object.heads('DETERMINER', 'r', ('stem','bir')):
				if object.getAttribute('poss') == 'Pnon' or object.getAttribute('poss') == 'Apos' or object.heads('CLASSIFIER', 'i'): 
					return object.coverage()
					
def bareCheck(tree):
	for n in tree.getElementsByTagName('n'):
		if n.getAttribute('pos') == 'Verb' and not isPassive(n) and verbCheck(n):
			try:			
				object = n.heads('OBJECT', 'i', ('case','Nom'),('infl','!A3pl'))
				if object and not object.heads('DETERMINER', 'r', ('stem','bir')):	
					return object.coverage()
				else:
					pass
			except AttributeError:
				pass	

def topicCheck(tree):
	for n in tree.getElementsByTagName('n'):
		if n.getAttribute('case') == 'Acc'\
			and n.getAttribute('link') == 'OBJECT'\
			and n.heads('DETERMINER', 'r', ('stem','bir'))\
			and (n.getAttribute('poss') == 'Pnon' or n.getAttribute('poss') == 'Apos' or n.heads('CLASSIFIER', 'i')):
					return n.coverage()

def testCheck(tree):
	for n in tree.getElementsByTagName('n'):
		sys.stderr.write('\n')
 		sys.stderr.write(n.toprettyxml().encode("utf-8"))
 		sys.stderr.write('\n')
	stop()	

def isPassive(node):
	return node.depends('DERIV','i',('stem','Hn')) or node.depends('DERIV','i',('stem','Hl'))

	
def verbCheck(node):
	if verbfilters == []:
		return True
	for q in verbfilters:
#		if node.heads('DERIV','r',('stem','gerçek')):
#			sys.stderr.write('aloha\n')
		try:
			if eval(q)(node):
 				verblog.write(node.getAttribute('form').encode('utf-8')+'\n')
				return True
		except AttributeError:
			pass
#lambda x: x.getAttribute('stem') == 'DHr' and x.heads('DERIV','i',('stem','lAş')) and x.heads('DERIV','r',('stem','gerçek'))
	return False

# def verbCheck(node):
# 	stem = _getStem(node)
# # 	sys.stderr.write('Stem: '+stem+"\n")
# 	for verb in verbs:
# # 		sys.stderr.write(verb+" "+stem+'\n')
# 		if verb.find(' ') == -1:
# 			if stem.startswith(verb):
# 				sys.stderr.write(verb+' '+stem)
# 				return True	
# 		else:
# 			a,b =verb.split(' ')
# 			if b.heads('DATIVE.ADJUNCT','i',('form',a)):
# 				return True
# 	return False

def _getStem(node):
	return node.getAttribute('stem').encode('utf-8')

def stop():
	#logfile.write('File:\t%s\nTo Mmax:\t%d\nUndecided:\t%d\nRejected:\t%d\nTotal:\t%d\n\n'%(args[0],count['incl'],count['undec'],count['reject'],count['total']))
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
	sys.exit()

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
	clparser.add_option('-f', dest='verbfilters', default=None, metavar='VERB_LIST',\
	help='a VERB_LIST (stem) file for filtering search results')
	clparser.add_option('-l', dest='lexfilter', default='^.*$', metavar='LEX_FILTER',\
	help='a regex pattern to filter the lexical content of the indefinite -- uses re.search().')


	(opts, args) = clparser.parse_args()
	offset = int(opts.offset)
	query = opts.query
	infile = open(args[0], mode='r')
	logfile = open('session.log','a')
	verblog = open('verb.log','a')
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

	verbfilters = []
	try:
		vfile = open(opts.verbfilters,'r')
		for line in vfile.readlines():
			if not line.startswith('#'):
				verbfilters.append(line.strip())
	except TypeError:
		pass

	#compile the regex for filtering the lexical content of the indefinite
	lexfilter = opts.lexfilter
	if lexfilter:
		lexpattern = re.compile(lexfilter)

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
			if count['disc'] >= offset:
				events.expandNode(node)
				try:
 					procDisc(node,query)			
				except Exception as ex:
					curses.nocbreak()
					curses.echo()
					curses.endwin()
					#logfile.write('\n\nlast proccesed doc'+ str(count['disc']))
					logfile.flush()
					undecfile.flush()
					mmaxfile.flush()
					raise
	stop()
	
