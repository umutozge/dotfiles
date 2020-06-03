#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Hasim Sak
#Description: An example python script to use the stochastic morphological parser for Turkish.

import sys
import re
import TurkishMorphology

if len(sys.argv) < 2:
	print 'usage:', sys.argv[0], 'corpus[ex:test.txt]'
	exit(1)

def parse_corpus():
	TurkishMorphology.load_lexicon('turkish.fst');
	n = 0
	e = 0
	f = open(sys.argv[1], 'r')
	for token in f:
		token = token.rstrip()
		if token.startswith('<') & token.endswith('>'):
			print token
		else:
			parses = TurkishMorphology.parse(token)
			if not parses:
				print token, token+"[Unknown]"
				continue
			print token,
			for p in parses: #There may be more than one possible morphological analyses for a word
				(parse, neglogprob) = p #An estimated negative log probability for a morphological analysis is also returned
				print parse,
			print
	f.close()

parse_corpus()
