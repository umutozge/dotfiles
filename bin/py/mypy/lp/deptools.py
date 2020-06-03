#!/usr/bin/python
import sys
import re
import codecs
import subprocess
from mypy.utils import listToStr, isString, isFile
from optparse import OptionParser
from xml.dom import minidom, EMPTY_NAMESPACE 
from xml.dom.minicompat import *

class Discourse(minidom.Document):

	def __init__(self,node):
		self.childNodes = NodeList() 
		self._elem_info = {}
		self._id_cache = {}
		self._id_search_stack = None
		self.documentElement = self.createElement('d')
		self.appendChild(self.documentElement)
		for s in node.getElementsByTagName('s'):
			self.documentElement.appendChild(Sentence(s))

	def writeToTreeBank(self,writer):
		if isString(writer):
			outfile = codecs.open(writer, encoding='utf-8', mode='a')
			outfile.write('<d>')
			for s in self.getElementsByTagName('s'):
				outfile.write(s.parse.toprettyxml(indent='  ',newl='\n',encoding='utf-8'))
			outfile.write('</d>')
			outfile.close()
		elif isFile(writer):
			writer.write('<d>')
			for s in self.getElementsByTagName('s'):
				writer.write(s.parse.toxml().encode('utf-8'))
			writer.write('</d>')
			writer.flush()

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
		for word in sent_elem.getElementsByTagName('word'):
			self.appendChild(Word(word))
		
		self.parse=self.parseDep()

	def toConll(self):
		retval=""
		count = 1
		for word in self.getElementsByTagName('w'):
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
		parser_in = open("_parser.in","w")
		parser_in.write(self.toConll().encode("utf-8"))
		parser_in.close()
		err = open("_parser.log","w")
		a = subprocess.call(["./maltparser","-f","svmoption1.txt","-L", "-s_0_-t_1_-d_2_-g_0.12_-c_0.7_-r_0.6_-e_0.01_-T_100", "-F","cl_test5", "-i","_parser.in", "-o","_parser.out"], stderr=err)  
		if a != 0:
			print "Parsing error...aborting"
			sys.exit(1)
		else:
			parser_out = codecs.open('_parser.out',encoding="utf-8",mode='r')
			rv =  DepTree(u''.join(parser_out.readlines()))
			parser_out.close()
			return rv

class Word(minidom.Element):

	def __init__(self, word_elem, namespaceURI=EMPTY_NAMESPACE, prefix=None, localName=None):
		self.tagName = self.nodeName = 'w' 
		self.prefix = prefix
		self.namespaceURI = namespaceURI
		self.childNodes = NodeList()
		self._attrs = {}   	# attributes are double-indexed:
		self._attrsNS = {} 	#    tagName -> Attribute
							#    URI,localName -> Attribute
							# in the future: consider lazy generation
							# of attribute objects this is too tricky
							# for now because of headaches with
							# namespaces.
		self.setAttribute('m',word_elem.getAttribute('morph'))
		self.appendChild(word_elem.childNodes[0])
		self.form = self.childNodes[0].wholeText
		self.IGs=[]
		igs = self.getAttribute('m').split('-')
		inds = range(len(igs))
		inds.reverse()
		for ig,ind in zip(igs,inds):
			if ind == 0:
				self.IGs.append(IG(ig,True))
			else:
				self.IGs.append(IG(ig))
		
class IG(object):
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

class DepTree(minidom.Element):
	

	def __init__(self, input, namespaceURI=EMPTY_NAMESPACE, prefix=None, localName=None):
		self.tagName = self.nodeName = 't' 
		self.prefix = prefix
		self.namespaceURI = namespaceURI
		self.childNodes = NodeList()
		self._attrs = {}   	# attributes are double-indexed:
		self._attrsNS = {} 	#    tagName -> Attribute
							#    URI,localName -> Attribute
							# in the future: consider lazy generation
							# of attribute objects this is too tricky
							# for now because of headaches with
							# namespaces.

		if isinstance(input,unicode):
			"""This is for calls by the Discourse class."""
			self.nodes=[]
			for s in input.split('\n'):
				l = s.split('\t')
				try:
					self.nodes.append(DepNode(l[0],l[3],l[1],l[2],l[5],l[6],l[7]))
				except IndexError:
					break

			self.root=DepNode(u'0',u'S',u'',u'',u'',u'',u'',u'')
			self.appendChild(self.root)
			self.decorateTree([self.root],self.nodes)
		elif isinstance(input,minidom.Node):
			"""This is for calls with a minidom.Element t."""
			self.root=DepNode(fromNode=input.childNodes[0])
			self.appendChild(self.root)
			
	def linearize(self):
		"""returns a linearized and flattened representation of the DepTree"""
		nds = self.getElementsByTagName('n')
		accum=[]
		for nd in nds:
			accum.append((int(nd.getAttribute('ind')),nd))	
		accum.sort()
		return [x[1] for x in accum]	


	def decorateTree(self,fringe,nodes):
		if len(nodes) ==0 or len(fringe)==0:
			return
		head = fringe.pop(0)
		headx = head.getAttribute('ind')
		i = 0
		while True:	
			try:
				if nodes[i].getAttribute("head")==headx:
# 					p= 'Tying node %s with index %s to node %s with index %s'%(nodes[i].getAttribute('form'),nodes[i].getAttribute('ind'),head.getAttribute('form'),head.getAttribute('ind'))
# 					print p.encode('utf-8')
					head.appendChild(nodes[i])
					fringe.append(nodes[i])
					nodes.remove(nodes[i])
					continue
			except IndexError:
				break
			i = i + 1
		self.decorateTree(fringe,nodes)
		
class DepNode (minidom.Element):

	def __init__(self,ind=None,pos=None,form=None,stem=None,infl=None,head=None,link=None, fromNode=None,namespaceURI=EMPTY_NAMESPACE, prefix=None, localName=None):
		self.tagName = self.nodeName = 'n' 
		self.prefix = prefix
		self.namespaceURI = namespaceURI
		self.childNodes = NodeList()
		self._attrs = {}   	# attributes are double-indexed:
		self._attrsNS = {} 	#    tagName -> Attribute
							#    URI,localName -> Attribute
							# in the future: consider lazy generation
							# of attribute objects this is too tricky
							# for now because of headaches with
							# namespaces.
		if ind:
			self.setAttribute("ind",ind)
			self.setAttribute("pos",pos)
			self.setAttribute("form",form)
			self.setAttribute("stem",stem)
			self.setAttribute("infl",infl)
			self.setAttribute("head",head)
			self.setAttribute("link",link)
			self.setAttribute("case","")
			self.setAttribute("poss","")
			if pos=="Noun":
				self.setAttribute("case",infl.split('|')[-1])
		elif fromNode:
			for attr in ['ind','pos','form','stem','infl','head','link','case']:
				self.setAttribute(attr,fromNode.getAttribute(attr))
				if self.getAttribute('pos')=='Noun':
					self.setAttribute("poss",fromNode.getAttribute('infl').split('|')[-2])
			for n in fromNode.childNodes:
				self.appendChild(DepNode(fromNode=n))
				
	def heads(self,link, mode, *queries):
		return self._heads(link,mode,tuple(queries))

	def _heads(self,link, mode, queries):
		"""queries are tuples of (attr,val) XXX: this function returns the first dependent it finds, so it needs to be elaborated if one needs a *set* of dependents"""
		if mode == 'i': #immediately heads
			query = "dn.getAttribute('link') == link"+self._buildQuery(queries)
			for dn in self.childNodes:
				if eval(query):
					return dn
			return None
		elif mode == 'r': #recursively heads
			query = "dn.getAttribute('link') == link"+self._buildQuery(queries)
			for dn in self.childNodes:
				if eval(query):
					return dn
				elif self.inMax(dn):
					down = dn._heads(link,'r',queries)
					if down:
						return down
					else:
						pass

	def _buildQuery(self,tuples):
		"""TODO: make this recursive"""
		if tuples==():
			return ""
		else:
			retval = ""
			for key, val in tuples:
# 				if str(type(val)) == "<type 'unicode'>":
# 					val = val.encode('utf-8')
				if val.startswith('!'):
					retval= retval + " and dn.getAttribute('%s').encode('utf-8').find('%s') == -1"%(key,val[1:])
				elif val.find('or') > 0:
					left, right = val.split(' or ')
					retval= retval + " and (dn.getAttribute('%s').encode('utf-8').find('%s') > -1 or dn.getAttribute('%s').encode('utf-8')find('%s') > -1"%(key,left,key,right)
				else:
					retval= retval + " and dn.getAttribute('%s').encode('utf-8').find('%s') > -1"%(key,val)
		return retval

	def depends(self,link,mode, *queries):
		return self._depends(link,mode,tuple(queries))

	def _depends(self,link,mode, queries):
		if  mode == 'i':
			dn = self.parentNode
			query = "self.getAttribute('link') == link"+self._buildQuery(queries)
			if eval(query):
				return dn
			else:
				return None
		else:
			pass

	def coverage(self):
		"""returns the list of indices of the nodes covered by node"""			
		retval =[int(self.getAttribute('ind'))]
		for nd in self.getElementsByTagName('n'):
			retval.append(int(nd.getAttribute('ind')))
			retval.sort()
		return retval

	def print_node(self):
		retval =[(int(self.getAttribute('ind')),self.print_attrs())]
		for nd in self.getElementsByTagName('n'):
			retval.append((int(nd.getAttribute('ind')),nd.print_attrs()))
			retval.sort()
		return retval

	def print_attrs(self):
		fields = [ 'ind', 'form', 'pos', 'case', 'head', 'link', 'infl']
		retval = ""
		for f in fields:
			retval = retval + "\t"+self.getAttribute(f)
		return retval

	def inMax(self,node):
		if self.getAttribute('pos') == 'Noun':
			return  node.getAttribute('link') in ['CLASSIFIER','DERIV']
		else:
			return False 
