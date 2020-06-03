#!/usr/bin/env python
import sys

from xml.dom import minidom, pulldom

events = pulldom.parse(open(sys.argv[1],'r'))

for event, node in events:
	if event == 'START_ELEMENT' and node.tagName == 'bi':
		events.expandNode(node)	
		words = node.getElementsByTagName('w')
		print words[-1].toxml().encode('utf8')
