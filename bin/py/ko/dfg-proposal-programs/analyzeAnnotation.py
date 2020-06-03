#!/usr/bin/env python

from mypy.annotools import *

from xml.dom import minidom, pulldom

import sys
from os import listdir, path

project = Project(path.abspath('.'))

keys = 'backward_linking,animacy,forward_linking,level_of_subord,descriptive_content,optional,focal'.split(',')
project.summarize_markables(keys)

sys.exit()
