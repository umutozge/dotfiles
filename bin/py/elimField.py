#!/usr/bin/env python

import sys
from mypy.datatools import Frame
from optparse import OptionParser

def listProduct(list1,list2,connector="-"):
	newlist = []
	for x in list1:
		for y in list2:
			newlist.append(x+connector+y)
	return newlist


def procHeader(oldheader):
	for x in elimlist:
		oldheader.remove(x)
	oldheader.remove(opts.pivot)	
	newheader=[]
	expelimlist= []
	for x in elimlist:
		expelimlist.append(list(data.uniqField(x)))	

	anch = []
	_listProduct(expelimlist,anch)
	for y in oldheader:
		for x in anch:
			newheader.append(x+'-'+y)

	return newheader

def _listProduct(lol,anch):#a recursive list product taker 
	try:
		if str(type(lol[0])) != "<type 'list'>":
			raise IndexError
		_listProduct(listProduct(lol.pop(0),lol.pop(0))+lol,anch)
	except IndexError:
		anch.extend(lol)	

if __name__=='__main__':

	clparser = OptionParser()
	clparser.usage='%prog [options] input-file\n\n%prog operates on a Frame and eliminates certain fields factoring them into column names'
	clparser.add_option('-e', dest='elimlist', metavar='ELIM LIST',\
	help="fields to eliminate; fields are separated with commas WITHOUT space; order matters for new column names")
	clparser.add_option('-p', dest='pivot', default='Subject', metavar='PIVOT',\
	help='which field to treat as pivot, (default: Subject)')
	clparser.add_option('-o', dest='outfile', default='out.csv', metavar='OUTFILE',\
	help='where to write the result')
	clparser.epilog="NOTE: The program assumes that all the fields except ELIM LIST and PIVOT are dependent variable fields.\nIt also assumes that column names do not contain any '-'"
	opts, args = clparser.parse_args()

 	data = Frame(fromfile=args[0])

	
 	elimlist = opts.elimlist.split(',')

 	header = [opts.pivot] + procHeader(data.header)#returns the new header
	outFrame = Frame(header)
 	for x in data.uniqField(opts.pivot):
		accum = {opts.pivot:x}
		for y in header[1:]:	
			keys = y.split('-')
			query=[(opts.pivot,x)]
			for i, j in enumerate(keys[:-1]):
				query.append((elimlist[i],j))		
			strquery=",".join([str(p) for p in query])	
			ff = eval('data.filter('+strquery+')')
			dd = ff.iterFrame()
			if len(dd) >1:
				sys.stderr.write('a problem of non-uniqueness\n')
				sys.stderr.write(str(dd)+'\n')
			try:
				accum[y] = dd[0][keys[-1]]
			except IndexError:
				pass
		outFrame.addData(accum)

	
	outFrame.printFrame(opts.outfile)
	sys.stderr.write('Fields '+opts.elimlist+' are eliminated from '+args[0]+'\n')
