#!/usr/bin/python2.6
import sys
import subprocess
from mypy.lp.deptools import * 
from xml.dom import pulldom


def procDisc(disc):
	outfile = 	open(opts.outfile, 'a')
	Discourse(disc).writeToTreeBank(outfile)
	outfile.flush()
	outfile.close()

if __name__ == "__main__":

	clparser = OptionParser()
	clparser.usage="%prog [options] input-file"
	clparser.add_option('-o', dest='outfile', help="output file")
	clparser.add_option('-s', dest='offset', metavar="OFFSET", help="start from the document OFFSET")

	(opts, args) = clparser.parse_args()
	offset = int(opts.offset)
	infile = open(args[0], mode='r')
	outfile = open(opts.outfile, 'a')
	header =u'<?xml version="1.0" encoding="UTF-8"?><tb>'

	if offset == 1:
		outfile.write(header)
	outfile.flush()
	outfile.close()

	p = subprocess.Popen("grep -c '<doc>' %s"%(args[0]),shell=True, stdout=subprocess.PIPE)
	dcount =  int(p.stdout.readlines()[0].strip())
	p.wait()


	events = pulldom.parse(infile)
	pcount = 0	
	for event , node in events:
		if event == 'START_ELEMENT' and node.tagName=='doc':
			if pcount + 1 >= offset:
				try:
					events.expandNode(node)
					procDisc(node)			
				except Exception as ex:
					for arg in ex.args:
						print arg
					sys.stderr.write('\n\n')
					sys.stderr.write('Error occured: last processed document is %d'%(pcount))
					sys.stderr.write('\n\n')
					raise
				else:
					pcount += 1
					sys.stderr.write('\tProgress\t %d/%d\t %f%% \r'%(pcount,dcount,float(pcount)/dcount*100))
			else:
				pcount += 1

	sys.stderr.write('\n')
	sys.stderr.write('Closing the file...\n')
	outfile = 	open(opts.outfile, 'a')
	outfile.write('</tb>')
	outfile.flush()
	outfile.close()
	p = subprocess.Popen("xmllint --format %s | grep -c '<d>' "%(outfile.name),shell=True, stdout=subprocess.PIPE)
	fcount =  int(p.stdout.readlines()[0].strip())
	p.wait()
	sys.stderr.write('\n')
	sys.stderr.write('Processed %d of %d documents.'%(fcount,dcount))
	sys.stderr.write('\n\n')
	sys.exit(0)
