#!/usr/bin/env python
from xml.dom import minidom, pulldom
from optparse import OptionParser
import sys





if __name__ == "__main__":

	clparser = OptionParser()
	clparser.add_option('-s', dest='size', metavar ='CHUNK SIZE', help="the size of each chunk")
	clparser.add_option('-t', dest='tagname', metavar='SPLIT TAG', help='the tag you want to split the corpus with')
  	clparser.add_option('-d', dest='docnode', metavar ='DOCNODE', help='the document node')
	clparser.add_option('-o', dest='filecount', metavar= 'OFFSET', help='starting naming the chunk files from OFFSET') 

	discCount = 0

	(opts, args) = clparser.parse_args()
	infile = open(args[0], mode='r')

	#lazily read the large corpus with pulldom
	events = pulldom.parse(infile)

	#initialize the buffer for each discourse
	discBuffer=""
	filecount = int(opts.filecount)
	outfile = open(args[0][:-4] + '.' + str(filecount) + '.xml','a')
	outfile.write(u'<?xml version="1.0" encoding="UTF-8"?><'+opts.docnode+'>')	
	
	for event , node in events:
		if event == 'START_ELEMENT' and node.tagName==opts.tagname:
			discCount += 1
			events.expandNode(node)
			outfile.write(node.toxml().encode("utf-8"))
			if discCount == int(opts.size):
				sys.stderr.write("\nWrote file no %d with %d discourses\n"%(filecount,int(opts.size)))
				discCount = 0
				outfile.write('</'+opts.docnode+'>')
				outfile.flush()
				outfile.close()
				filecount += 1
				outfile = open(args[0][:-4] + '.' + str(filecount) + '.xml','a')
				outfile.write(u'<?xml version="1.0" encoding="UTF-8"?><'+opts.docnode+'>')	
	outfile.write('</'+opts.docnode+'>')
	outfile.flush()
	outfile.close()
