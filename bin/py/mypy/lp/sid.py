#!/usr/bin/python2.6
import sys
import re
import subprocess
from umut import listToStr
from optparse import OptionParser
from xml.dom import minidom, EMPTY_NAMESPACE 
from xml.dom.minicompat import *

class Discourse(minidom.Document):

	def __init__(self,xmlstring):
		self.childNodes = NodeList() 
		self._elem_info = {}
		self._id_cache = {}
		self._id_search_stack = None
		self.root = self.createElement('d') 	
		for s in minidom.parseString(xmlstring).getElementsByTagName('s'):
			self.root.appendChild(Sentence(s))
		sys.exit(0)
		self.hits=[]
		self.parseSents()
		self.printSents()
	def parseSents(self):
		for s in self.sents:
 			s.parseDep()
	def printSents(self):
		for s in self.sents:
			ns = s.parse.getNode([("pos","Noun"),("case","Acc")])
			for n in ns:
				print n.get("pos"), "  ", n.get("infl"), "  ", n.get("form")
	def detectIndef(self):
		for s in self.sents:
			parse = s.parse
				

class Sentence(minidom.Element):
	def __init__(self, sent_elem, namespaceURI=EMPTY_NAMESPACE, prefix=None, localName=None):
		self.tagName = self.nodeName = 's' 
		self.prefix = prefix
		self.namespaceURI = namespaceURI
		self.childNodes = NodeList()
		self._attrs = {}   # attributes are double-indexed:
		self._attrsNS = {} #    tagName -> Attribute
							#    URI,localName -> Attribute
							# in the future: consider lazy generation
							# of attribute objects this is too tricky
							# for now because of headaches with
							# namespaces.
		for word in  sent_elem.getElementsByTagName('word'):
			self.appendChild(word)

	def toConll(self):
		retval=""
		count = 1
		for word in self.words:
			for ig in word.IGs:
				form="_"
				if ig.is_head:
					form=word.form
				if ig.pos=='Unknown':
					ig.pos= 'Noun'
					ig.infl= 'A3sg|Pnon|Nom'
				retval += '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %(count, form, ig.stem, ig.pos, ig.pos, ig.infl, "_", "_", "_", "_")
				count += 1
		return retval
	def parseDep(self):
		parser_in = open("_parser.in","wb")
		parser_in.write(self.toConll().encode("utf-8"))
		parser_in.close()
		err = open("_parser.log","wb")
		a =\
		subprocess.call(["./maltparser","-f","svmoption1.txt","-L", "-s_0_-t_1_-d_2_-g_0.12_-c_0.7_-r_0.6_-e_0.01_-T_100",
		"-F","cl_test5", "-i","_parser.in", "-o","_parser.out"], stderr=err)  
		if a != 0:
			print "Parsing error...aborting"
			sys.exit(1)
		else:
			parser_out = open('_parser.out','r')
			self.parse= DepTree(listToStr(parser_out.readlines()))
			parser_out.close()

class DepTree:
	def __init__(self, sentconll):
		self.nodes=[]
		for s in sentconll.split('\n'):
			l = s.split('\t')
			try:
				self.nodes.append(Node(l[0],l[3],l[1],l[2],l[5],l[6],l[7]))
			except IndexError:
				break
	def getNodes(self):
		return self.nodes
	def getNode(self,keysvals):
		accum = []	
		for n in self.nodes:
			for key, val in keysvals:
				if n.get(key) != val:
					break
			else:
				accum.append(n)
		return accum

class Node:
	def __init__(self,ind,pos,form,stem,infl,head,link):
		case =""
		if pos=="Noun":
			case = infl.split('|')[-1]
		self.data= {"ind":ind,"pos":pos,"form":form,"stem":stem, "infl":infl,"head":head,"link":link,"case":case}
	def get(self,key):
		return self.data[key]

class Word:
	def __init__(self,morph,form):
		self.morph=morph
		self.form=form
		self.IGs=[]
		igs = self.morph.split('-')
		inds = range(len(igs))
		inds.reverse()
		for ig,ind in zip(igs,inds):
			if ind == 0:
				self.IGs.append(IG(ig,True))
			else:
				self.IGs.append(IG(ig))

class IG:
	def __init__(self,string,head=False):
		self.is_head=head
		a =	self.parseIG(string)
		self.stem, self.pos, self.infl = a

	def parseIG(self,string):
		p = re.compile('^([^+]*)\[(.*)\]') 
		m = p.match(string)
		infl=""	
		stem = m.group(1) 
		d = m.group(2).split('+')
		pos = self._strip(d[0])
		for i in d[1:]:
			infl += '|'+self._strip(i)
		if infl.startswith('|'):
			infl= infl[1:]
		elif infl=='':
			infl='_'
		return stem,pos,infl

	def _strip(self,st):
		try: 
			a = st.index('[') + 1 
			st = st[a:]
		except ValueError: 
			pass
		try: 
			a = st.index(']') 
			st = st[:a]
		except ValueError: 
			pass
		return st
		

if __name__ == "__main__":

	clparser = OptionParser()
	clparser.add_option('-o', dest='outfile')
	(opts, args) = clparser.parse_args()
	infile = open(args[0], 'r')
	outfile = open(opts.outfile, 'w')
	header ='<?xml version="1.0" encoding="UTF-8"?>\n'
	line = infile.readline().strip()

	while line != "</corpus>": 
		doc_buffer=""
		if line=="<doc>":
			doc_buffer += line
			while line !="</doc>":
				line = infile.readline().strip()
				doc_buffer += line
			disc = Discourse(header + doc_buffer)
		line = infile.readline().strip()
