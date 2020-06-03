#!/usr/bin/python

import argparse
import codecs
import time
import re
from mypy.lp.deptools import * 
from xml.dom import minidom, pulldom

def print_counts():
	for key in count.keys():
		print(key,count[key])


def proc_treebank(tbfile):
	events = pulldom.parse(tbfile)
	for event, node in events:
		if event == 'START_ELEMENT'and node.tagName == 't':
			events.expandNode(node)
			proc_sentence(node)

def print_csv(node):
	lst = node.print_node()
	for i in lst:
		print i[1].encode('utf-8')


def proc_sentence(node):
 	tree = DepTree(node)
	root = tree.childNodes[0]
	verb =root.heads('ROOT','i',('pos','Verb'))
 	if verb:
		obj = verb.heads('OBJECT','i',('case','Acc'))
		if obj:
			order_list=[(obj.getAttribute('ind'),'O'),(verb.getAttribute('ind'),'V')]
			subj = _check_subj(verb)
			if subj: order_list.append((subj.getAttribute('ind'),'S',))
			order_list.sort()
			order = ''.join([x[1] for x in order_list])
			counts[order]+=1
			counts['Total']+=1
# 			print ' \t \t \t'
# 			print 'Order:\t'+ order
# 			print_csv(verb)
# 			print ' \t \t \t'

def _check_subj(vnode):
	"Takes the matrix node and checks whether it has an overt subject or not"""
	snode = vnode.heads('SUBJECT','i')
	try:
		if snode and snode.getAttribute('infl').endswith('|Nom') and _check_agr(vnode,snode):
			return snode
		else:
			return None
	except:
		print "***ERROR***"
		print snode.print_attrs()
		print "***ERROR***"
		sys.exit(1)
# 	if snode and (snode.getAttribute('pos') in ['Det','Pron'] or _check_agr(vnode,snode)):
# 		return snode
# 	else:
# 		return None

def _check_agr(node1,node2):
	agr_pat = re.compile('A\d') #don't look at number, just check person
	try:
		agr1 = agr_pat.findall(node1.getAttribute('infl'))[0]
		agr2 = agr_pat.findall(node2.getAttribute('infl'))[0]
	except:
		print "***ERROR***"
		print_csv(node1)
		print_csv(node2)
		print '***ERROR***'
		sys.exit(1)
	return agr1 == agr2


def report_counts():
	cdict = dict(counts)
	print 'Order\tCount\t\tPercentage'
	for k in ['SOV','OSV','SVO','OVS','VOS','VSO','OV','VO']:
		print k +'\t'+ str(cdict[k])+'\t\t'+ str(cdict[k]*100.0/cdict['Total'])
	print 'Total\t'+ str(cdict['Total'])


parser = argparse.ArgumentParser(description='Compute case-marker distribution in dependency treebanks', prog='case-distrib.py')
parser.add_argument('treebank', nargs='+', help='treebank(s) to be searched')


args = parser.parse_args()

#Init stuff
counts = {\
'SOV':0,\
'OSV':0,\
'SVO':0,\
'OVS':0,\
'VSO':0,\
'VOS':0,\
'OV':0,\
'VO':0,\
'Total':0,}


report=False

for tb in args.treebank:
	try:
		if report:
			print
			print "Interim Count Report"
			print 
			report_counts()
		print
		print "Processing "+tb+"..."
		proc_treebank(open(tb,mode='r'))
		report = True
	except:
		report_counts()
		print
		print "Terminated due to ERROR"
		sys.exit(1)

print "Final Count Report"
report_counts()
