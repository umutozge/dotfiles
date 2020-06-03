#!/usr/bin/python
import sys
import re
from optparse import OptionParser

def writeChunk(buffer,chunk,root, source):
	opentag='<%s part="%s" source="%s">\n'	%(root,chunk,source)	
	closetag= '</%s>' % root
	content = header + opentag + buffer + closetag
	m = re.search('(\w+)\.xml', source)
	outfilename = m.group(1) + ".part%s.xml" % chunk
	outfile= open(outfilename, 'w')
	outfile.write(content)
	outfile.close()



clparser= OptionParser()
clparser.add_option("-s", dest="chunk_size",help="set the chunk size")

(opts,args) = clparser.parse_args()

infilename= args[0]
infile = open(infilename,'r')

header= infile.readline()
source_file = infilename 
chunk_size = int(opts.chunk_size)

root_tag = re.search('<(\w+)',infile.readline()).group(1)

doc_count = 0
chunk_count = 1
doc_buffer=""
line = infile.readline().strip()

while True:
	if line=="<doc>":
		while line!="</doc>":
			doc_buffer += line + "\n"
			line = infile.readline().strip()
		doc_buffer += line + "\n"
		doc_count += 1
		line = infile.readline().strip()
		if line=="</corpus>":
			writeChunk(doc_buffer,chunk_count,root_tag,source_file)
			break
		elif doc_count == chunk_size:
			writeChunk(doc_buffer,chunk_count,root_tag,source_file)
			print  str(doc_count) + " " + str(chunk_count)
			print line
			doc_count=0
			chunk_count +=1
			doc_buffer = ""

sys.exit(0)
