#!/usr/bin/env python

import sys
from mypy.datatools import Frame
from optparse import OptionParser


if __name__=='__main__':


	data = Frame(fromfile=sys.argv[1])
	items = data.uniqField('Item')
	outfile = open(sys.argv[1][0:14]+'ItemAnalysis.csv','w')

	for i in items:
		itemRow=[i,]
		caseRows={'Nominative':['Nominative'],'Accusative':['Accusative']}
		for t in ['TW'+str(x) for x in range(1,6)]:
			for a in ['Agent','Patient','Topic','Other']:
				itemRow.append(t+'-PercNumFixTo'+a)
				for c in ['Nominative','Accusative']:
					try:
						value = data.filter(('Item',i),('Condition',c),('TimePeriod',t)).iterFrame()[0]['PercNumFixTo'+a]
					except IndexError:
						value = ""
					caseRows[c].append(value)
		outfile.write(','.join(itemRow)+'\n'+','.join(caseRows['Nominative'])+'\n'+','.join(caseRows['Accusative'])+'\n,,\n')

