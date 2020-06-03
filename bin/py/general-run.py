#!/usr/bin/env python

import sys
import os
import subprocess
import re

infile = open(sys.argv[1])

for i in infile.readlines():
	p = subprocess.Popen("echo '"+i+"' |sh",shell=True,stdout=subprocess.PIPE)
	p.wait()
