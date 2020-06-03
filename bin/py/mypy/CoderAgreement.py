#!/usr/bin/env python
"""
A module for computing inter-coder agreement in corpus annotation.
The current version is limited to two coders.
"""

__author__='Umut Ozge'
__author_email__='tumuum@gmail.com'

from mypy.datatools import Frame
from mypy.utils import trunc2 

class Agreement(object):
	"""A class for computing and reporting agreement information."""

	def __init__(self,datafile,categories):
		"""
		Init an Agreement instance

		Args:

		datafile -- name of a csv file to read the annotation data, with the following structure:

		Item,Coder1,Coder2
		1,some cat, some cat
		2,some cat, some cat
		...


		categories -- list of categories that the markables can be assigned to
		"""

		#Categories
		self._Cats = Cats(categories)
		self._Name = datafile[:datafile.find('.')]
		#open the input file and read data 
		self._Data = Frame(fromfile=datafile)
		header = self._Data.header
		c1 = header[1]
		c2 = header[2]
		self._Coders = {c1:Coder(c1,self),c2:Coder(c2,self)}
		item_label = header[0]

		matches = 0

		for d in self._Data:
				self._Coders[c1][d[c1]] += 1
				self._Cats._assign(d[c1])
				self._Coders[c2][d[c2]] += 1
				self._Cats._assign(d[c2])

				if d[c1] == d[c2]:
					matches += 1

		#Number of items
		self.I = len(self._Data.data)
		self._Ao = matches/float(self.I)
		#Number of categories
		self.K = len(self._Cats)

	def get_agreement(self):
		return {'s':trunc2(self.compute_S(),3),'pi': trunc2(self.compute_Pi(),3),'k':trunc2(self.compute_K(),3)}

	@property
	def Cats(self):
		"""The list of category names"""
		return self._Cats.keys()

	@property
	def Name(self):
		"""Name of the agreement instance--category of the markable being compared."""
		return self._Name.keys()

	@property
	def Coders(self):
		"""The list of Coder instances"""
		return self._Coders
	@Coders.setter
	def Coders(self,value):
		self._Coders = value

	def _comp_agr(self,exp):
		"""Apply the common formula for all coefficient types

		Args:
		exp (float) -- expected agreement
		"""
		print 'Expected agreement: ' + str(exp)
		return (self._Ao - exp)/(1 - exp)


	def compute_S(self):
		"""Copute coefficient S"""
		return self._comp_agr(1/float(self.K))

	def compute_Pi(self):
		"""Copute coefficient Pi"""
		exp = 1/(4*float(self.I)**2)*reduce(lambda x,y:x+y,[(self._Cats[k])**2 for k in self.Cats])
		return self._comp_agr(exp)

	def compute_K(self):
		"""Copute coefficient K"""
		sum = 0
		for k in self.Cats:
			sum += reduce(lambda x,y:x*y,[self._Coders[c][k] for c in self._Coders.keys()])
		return self._comp_agr(1/float(self.I)**2*sum)

class Cats(dict):
	"""A holder for annotation category"""
	def __init__(self,keylist):
		for key in keylist:
			self[key] = 0
	def _assign(self,key):
		self[key] += 1

class Coder(dict):
	"""A coder"""
	def __init__(self,id,agr):
		"""Init a Coder

			id -- ID for the coder
			agr -- mother Agreement instance
		"""
		self._ID = id
		for cat in agr.Cats:
			self[cat] = 0

	@property
	def ID(self):
		return self._ID

	def _assign(self,cat):
		self[cat] += 1
