#!/usr/bin/env python
import sys
import csv
import re
import copy
import exceptions
import xlwt, xlrd
from mypy import utils

class Frame:
	def __init__(self, header=None, rows=None, fromfile=None):
		"""Initialize a data frame.

			Keyword args:
			header -- list of column names, order matters
			rows -- rows of the data frame; it can be either a list of lists or dicts
			fromfile -- a data frame can be initialized directly from a csv file
		"""
		if fromfile:
			rs = Csv(fromfile).getRows()	
			self.header=rs[0]
			self.data = [] #a list of dictionaries
			for r in rs[1:]:
				acc= dict()
				for h in self.header:
					acc[h]=r[self.header.index(h)]	
				self.data.append(acc) 
		elif header:
			self.header = header	
			self.data = []
			if rows:
				if isinstance(rows[0],dict):
					self.data = rows
				elif isinstance(rows[0],list):	
					for r in rows:
						acc= dict()
						for h in self.header:
							acc[h]=r[self.header.index(h)]
						self.data.append(acc) 
		else:
			self.header = []	
			self.data = []

	def __iter__(self):
		return iter(self.data)

	def set_header(self,header): 
		self.header = header

	def removeData(self,dat):
		self.data.remove(dat)
		
	def addData(self,data):
		"""
		Add data to the frame.
		data can be:
			-a list of dicts
			-a list of lists
			-a dict
		"""
		if isinstance(data,list):
			if isinstance(data[0],dict):
				self.data.extend(data)
			elif isinstance(data[0],list):	
				for r in data:
					acc= dict()
					for h in self.header:
						acc[h]=r[self.header.index(h)]	
					self.data.append(acc) 
		elif isinstance(data,dict):
			self.data.append(data)
		else:
			raise datatools.WrongTypeError(data)

	def getData(self,key,value):
		try:
			return Frame(self.header, self._filter(self.data,[[key,value]])).iterFrame()[0]
		except IndexError:
			raise DataNotFound(key,value)
		

	def get_rows(self):
		"""Return a list of rows"""
		rows = [self.header]
		for d in self.data:
			row = []
			for h in self.header:
				try:
					row.append(d[h])
				except KeyError:
					row.append(empty)
			rows.append(row)
		return rows

	def isEmpty(self):
		return self.data == []

	def addField(self,fieldname,afterwhich=None,defval=""):
		"""
		Insert a field named fieldname to the frame, placing it after afterwhich and with a default value defval.
		If no afterwhich is given, insert at the end.
		"""
		if afterwhich is None:
			self.header.append(fieldname)
		else:
			self.header.insert(self.header.index(afterwhich)+1,fieldname) 	

		"""Set the default value for the added field"""
		for d in self.data:
			d[fieldname]=defval

	def getField(self,fieldname):
		accum = []
		for d in self.data:
			accum.append(d[fieldname])
		return accum

	def sum_field(self,fieldname):
		lst = self.getField(fieldname)	
		sum = 0
		for x in lst:
			sum += int(x)
		return sum

	def get_prop(self):
		"""Extract and return a proportion table from the frame."""
		newframe = copy.deepcopy(self)
		for f in newframe.header[1:]:	
			sum = newframe.sum_field(f)
			for d in newframe:
				try:
					d[f]= d[f]/float(sum)*100
				except ZeroDivisionError:
					d[f] = 0
		
		return newframe

	def iterFrame(self):
		return self.data

	def filter(self,*queries):
		return Frame(self.header,self._filter(self.data,list(queries)))

	def _filter(self,rows,qlist):
		if qlist == []:
			return rows
		else:
			key = qlist[0][0]
			val = qlist[0][1]
			accum = []
			for r in rows:
				if r[key] and r[key].strip() == val.strip():
					accum.append(r)	
			return self._filter(accum,qlist[1:]) 

	def uniqField(self, fieldname):
		"""Return the values of fieldname without repetitions."""
		retval = list(set(self.getField(fieldname)))
		retval.sort()
		return retval 

	def printFrame(self,outfile=None,sheetname=None,filename=None,rowoffset=0,empty=""):
		"""
		Write the frame to a file with the name outfile. 
		If no outfile is given, return a list of rows; each row is itself a list of cells. 
		"""
		rows = [self.header]
		for d in self.data:
			row = []
			for h in self.header:
				try:
					row.append(d[h])
				except KeyError:
					row.append(empty)
			rows.append(row)


		if outfile == None:
			return rows
		elif isinstance(outfile,xlwt.Workbook) and sheetname and filename:
			ws = outfile.add_sheet(sheetname)
			for ri, row in enumerate(rows):
				for ci, val in enumerate(row):
#  					val = unicode(val).encode("utf8")
					ws.write(ri+rowoffset,ci,val,xlwt.easyxf(num_format_str='#0.00'))
			outfile.save(filename)
		else:
			wr = csv.writer(open(outfile,'w'))
			wr.writerows(rows)

	def append(self,frame):
		if self.header == frame.header:
			self.data.extend(frame.data)
		elif self.isEmpty():
			self.header = frame.header
			self.data.extend(frame.data)
		else:
			raise FrameAppendError()

	def elim_fields(self,pivot,elimlist):

		header = [pivot] + self._proc_header(pivot,elimlist)#returns the new header

		outFrame = Frame(header)
		data = copy.deepcopy(self)
		for x in data.uniqField(pivot):
			accum = {pivot:x}
			for y in header[1:]:	
				keys = y.split('-')
				query=[(pivot,x)]
				for i, j in enumerate(keys[:-1]):
					query.append((elimlist[i],j))		
				strquery=",".join([str(p) for p in query])	
				ff = eval('data.filter('+strquery+')')
				dd = ff.iterFrame()
				if len(dd) > 1:
					sys.stderr.write('a problem of non-uniqueness\n')
					sys.stderr.write(str(dd)+'\n')
				try:
					accum[y] = dd[0][keys[-1]]
				except IndexError:
					pass
			outFrame.addData(accum)
		
		return outFrame
# 		outFrame.printFrame(opts.outfile)
# 		sys.stderr.write('Fields '+opts.elimlist+' are eliminated from '+args[0]+'\n')
		
	def _proc_header(self,pivot,elimlist):
		oldheader = copy.deepcopy(self.header)
		for x in elimlist:
			oldheader.remove(x)
		oldheader.remove(pivot)	

		newheader=[]
		expelimlist= []
		for x in elimlist:
			expelimlist.append(list(self.uniqField(x)))	

		anch = []

		self._listProduct(expelimlist,anch)
		for y in oldheader:
			for x in anch:
				newheader.append(x+'-'+y)
		return newheader

	def _listProduct(self,lol,anch):#a recursive list product taker 
		"""Recursive list product taker. A little complicated, but needed to get a particular ordering of the elements of the final product. So do NOT replace it with a simpler product taker."""
		try:
			if str(type(lol[0])) != "<type 'list'>":
				raise IndexError
			self._listProduct(utils.xproduct(lol.pop(0),lol.pop(0))+lol,anch)
		except IndexError:
			anch.extend(lol)	

class Csv:
	def __init__(self, input, mode='r', delimiter=",", clean=False):
		self.data_rows=[]
		self.delimiter=delimiter
		if mode =='r':
			if clean:
				cleanedfile = self.cleanFile(open(input,'r'))
				reader=csv.reader(cleanedfile,delimiter=self.delimiter)	
			else:
				reader= csv.reader(open(input,'r'),delimiter=self.delimiter)
			for row in reader:
				self.data_rows.append(row)
		elif mode == 'w':
			self.data_rows=input
	def cleanFile(self,file):
		"cleans a csv file from empty rows, and converts everything to\
		lower case"
		lines = file.readlines()
		cleanedfile= []
		pattern = re.compile('.+\w.+')
		for line in lines:
			if pattern.match(line) != None:
				cleanedfile.append(line.strip().lower())
		return cleanedfile
	def getRows(self):
		return self.data_rows
	def getRow(self, key):
		"returns the row if called with an  index (int), and all the matching raws if\
		called with a key (str)"
		if str(type(key)) == "<type 'int'>":
			return self.data_rows[key]
		elif str(type(key)) == "<type 'str'>":
			accum=[]
			for row, idx in zip(self.data_rows, range(len(self.data_rows))):
				if row[0]==key:
					accum.append(self.data_rows[idx])
			return accum
	def getCols(self):
		return self.data_cols
	def getCol(self, index):
		return self.data_cols[index]
	def getPart(self,rows,cols):
		"returns a set of rows"
		retval = []
		for ri in rows:
			row = self.data_rows[ri] 
			accum= []
			for ci in cols:
				accum.append(row[ci])	
			retval.append(accum)
		return retval
	
	def writeToFile(self, filename='out.csv'):
		fileout = open(filename,'wb')
		csv_writer=csv.writer(fileout,'excel',delimiter=self.delimiter)
		f = open(filename,"w")
		f.writelines([','.join(x)+'\n' for x in self.data_rows])
		f.close()

class FrameAppendError(exceptions.Exception):
	
	def __init__self():
		pass	
	def __str__(self):
		print "\tFrame headers do not match, append failed!"

class DataNotFound(exceptions.Exception):
	
	def __init__(self,key,value):
		self.key = key
		self.value = value

	def __str__(self):
		print "\tData not found for query '%s' is '%s'"%(self.key,self.value)

class WrongTypeError(exceptions.Exception):
	
	def __init__(self,x):
		self.type = type(x)

	def __str__(self):
		print "\tWrong type for this operation: '%s' "%(str(self.type))

