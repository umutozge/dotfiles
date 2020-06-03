#!/usr/bin/env python

from mypy.annotools import *

from xml.dom import minidom, pulldom

import sys
from os import listdir, path

try:
	project = Project(path.abspath('.'),sys.argv[1].split(','))
except IndexError:
	project = Project(path.abspath('.'))


keys = 'backward_linking,animacy,forward_linking,level_of_subord,descriptive_content,optional,focal'.split(',')
#keys = 'backward_linking,animacy,forward_linking,descriptive_content'.split(',')
#keys = 'np_type'.split(',')
project.summarize_markables(keys)

sys.exit()
