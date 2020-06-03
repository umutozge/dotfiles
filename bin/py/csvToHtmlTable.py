#!/usr/bin/env python
import re
import sys
from mypy.datatools import Frame



pframe = Frame(fromfile=sys.argv[1])

# outframe = Frame(['Time','Name','Talk'])

htmlfile = open('wafl-program.html','w')

htmlfile.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head><body>')

namepat = re.compile('^No (\d+):(.*)$')

for d in pframe.iterFrame():
	
	try:
		if d['Time'][0]=='F':
			htmlfile.write('<br/>\n<h3>'+d['Time']+'</h3>\n<br/>\n<table border="1">\n')
			continue
		elif d['Time'][0].isalpha():	
			htmlfile.write('</table>')
			htmlfile.write('<br/><h3>'+d['Time']+'</h3><br/>\n')
			htmlfile.write('<table border="1">\n')
			continue
	except IndexError:
			continue
	
	if d['Time']!='':
		name = namepat.match(d['Name'].strip())
		if name:
			htmlfile.write('<tr><td>%s</td><td>%s<br/><a href="abs/wafl8sub%s.pdf" target="_blank">%s</a></td></tr>\n'%(d['Time'],name.group(2), name.group(1),d['Talk']))
		else:	
			htmlfile.write('<tr><td>%s</td><td>%s</td></tr>\n'%(d['Time'],d['Name']))



htmlfile.write('</table>\n</body></html>')

