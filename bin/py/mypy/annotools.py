#!/usr/bin/env python
"""
A module for representing annotation information.
"""

__author__='Umut Ozge'
__author_email__='tumuum@gmail.com'


from mypy.datatools import Frame
from mypy.CoderAgreement import Agreement 
from xml.dom import pulldom
import exceptions
import sys
from os import chdir, listdir, path, getcwd

def _read_span(text):
	text = text.split(',')[-1]
	bounds = [int(x.split('_')[1]) for x in text.split('..')]
	if len(bounds)==2:
		return tuple(bounds)
	elif len(bounds)==1:
		return (bounds[0],bounds[0])
	else:
		raise BadAttributeError('bad span definition')

def _includes(x,y):
	"""Decide whether span x (2-tuple of ints) includes span y"""
	return x[0] <= y[0] and x[1] >= y[1]

def _includes_nd(x,y):
	"""Decide whether either of the spans include the other"""
	return _includes(x,y) or _includes(y,x)

class Project():
	"""An annotation project with a number of Annotators"""
	def __init__(self,root_path,coders=None,mode='base_indef'):
		"""The Project instance finds directories for coders in its root path"""
		self.coders =[]
		if coders:
			for c in coders:
				sys.stderr.write('\nAdding '+ c + '\n\n')
				self.coders.append(Coder(path.join(root_path,c)))
		else:
			for dir in listdir(root_path):
				sys.stderr.write('\nAdding '+ dir+'\n\n')
				self.coders.append(Coder(path.join(root_path,dir)))
	
	
	def summarize_markables(self,keys):
		matches = self._compute_matches()
		for k in keys:
			out = open(k+'.csv','w')
			out.write('Item,Coder1,Coder2,Batch\n')
			for i,m in enumerate(matches):
				try:
					v1 = eval('m[0].'+k)
					v2 = eval('m[1].'+k)
					out.write(','.join([str(i+1),v1,v2,m[2],m[4]])+'\n')
				except AttributeError as e:
					print e.message
			out.close()

	def _compute_matches(self):
		matches = []
		c1,c2 = tuple(self.coders)
		for b1, b2 in zip(c1.batches,c2.batches):	
			for d1 in b1.discourses:
				d2 = None
				for x  in b2.discourses:
					if x.id == d1.id:
						d2 = x	
						break
				for m1 in d1.markables:
					m2 = None	
					for x in d2.markables:
						if _includes_nd(m1.span,x.span):
							m2 = x
							break
					print m1,m2,b1.id,b2.id,m1.id
					if m2:
						matches.append((m1,m2,b1.id,b2.id,m1.id,m2.id))
# 					print m1.span, m1.id, m2.span, m2.id
		return matches

	def report(self):
		for c in self.coders:
			out = open(c.id+'.txt','w')
			out.writelines('Coder: ' + c.id+'\n')
			out.writelines( 'Batches: ' + str(len(c.batches))+'\n')
			for b in c.batches:
				out.writelines('\tBatch: ' + b.id+'\n')
				out.writelines('\tDiscourses: ' + str(len(b.discourses))+'\n')
				for d in b.discourses:
					out.writelines('\t\tDiscourse: ' + d.id + ' has ' + str(len(d.markables))+'\n')
			out.close()

class Coder():
	def __init__(self,data_path):	
		self.id = path.basename(data_path)
		self.batches = []
		for dir in listdir(data_path):
			self.batches.append(Batch(self,path.join(data_path,dir)))
			
class Batch():
	"""A holder of Discourse instances"""
	def __init__(self,coder,data_path):
		self.coder=coder
		self.discourses=[]
		self.data_path = data_path
		self.id = path.basename(data_path)

		olddir = getcwd()
		chdir(data_path)

		events = pulldom.parse(open(path.join(data_path,path.basename(data_path)+'_discourse_level.xml'),'r'))

		for event, node in events:
			if event == 'START_ELEMENT' and node.tagName == 'markable' and node.getAttribute('status') == 'include':
				self.discourses.append(Discourse(data_path,node))	

		events = pulldom.parse(open(path.join(data_path,path.basename(data_path)+'_nominal_level.xml'),'r'))
		for event, node in events:
			if event == 'START_ELEMENT' and node.tagName == 'markable':
 				markable = Markable(node)
				markable.batch = self.id
				markable.coder = self.coder.id
				try:
					if markable.type=='base_indef.':
						for d in self.discourses:
							if d.includes(markable):
								markable.discourse = d.id
								d.add_markable(markable)
								break
				except KeyError:
					print self.id, markable.id
				except AttributeError:
					print 'Excluding ' + self.id, markable.id
		chdir(olddir)	

class Discourse():
	"""A holder of Markable instances"""
	def __init__(self,data_path,node):
		self.id = node.getAttribute('id').encode('utf-8') 
		self.span = _read_span(node.getAttribute('span'))
		self.markables = []
	def add_markable(self,markable):
		self.markables.append(markable)
	def includes(self,markable):
		return _includes(self.span,markable.span)

class Markable(object):
	def __init__(self,node):
		for attr in node.attributes.keys():
			if attr.endswith('.'):
				attrname = attr[:-1]
			else:
				attrname = attr
  			exec 'self.'+attrname.encode('utf-8')+"='"+node.getAttribute(attr).encode('utf-8')+"'"
		self.span = _read_span(self.span)
		try:
			if self.backward_linking != 'empty':
				self.backward_linking = 'markable'
		except AttributeError:
			pass
	def getAttrTab(self):
		return self.__dict__

class WrongType(exceptions.Exception):
	pass

class BadAttributeError(exceptions.Exception):
	def __init__(self,text):
		self.text = text
	def __str__(self):
		print self.text

