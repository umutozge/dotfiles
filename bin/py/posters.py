#!/usr/bin/env python
import re
import sys
from mypy.datatools import Frame



pframe = Frame(fromfile=sys.argv[1])

# outframe = Frame(['Time','Name','Talk'])

htmlfile = open('wafl-posters.html','w')

htmlfile.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head><body>\n')

for d in pframe.iterFrame():
	htmlfile.write('<br/>%s<br/><a href="abs/wafl8sub%s.pdf" target="_blank">%s</a><br/>\n'%(d['Name'],d['No'],d['Title']))


htmlfile.write('</body></html>')

htmlfile.flush()
htmlfile.close()
