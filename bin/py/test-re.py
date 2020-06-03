#!/usr/bin/env python3
#coding: utf-8

import re
import sys


p = re.compile('([a-z]+ |\(|; ?|. )(([#A-ZÖÇÜŞİ][^. ]+,? |and )+\(?\d\d\d\d\)?)')

t = '; Göksel, Kelepir, Üntak 1992'
t2 = ';Ala, Kala, and Üzyıldız (1992))'
t3 = '(Erguvanlı Taylan 2000; Göksel, Kelepir, and Üntak 2009; Özge, Marinis, and Zeyrek 2010). In this article, we will focus o'

t4 = ' Hani is a modal adverb (G#oksel and Kerslake 2005;  G#oksel, Kelepir, and #Untak 2009) that pragmatically functions as a discourse particle. Erguvanl#i Taylan (2000) describes it as a modal particle. It appears in a number of constructions which have been investigated from different aspects in the literature (Erguvanl#i Taylan 2000; G#oksel, Kelepir, and #Untak 2009; #Ozge, Marinis, and Zeyrek 2010). In this article, we will focus on constructions with hani that have high-rising terminal intonation like wh-constructions as in (1).'

k = p.findall(t4)
print(k)

# print(p.match(t2).group(0))
# print(p.match(t2).group(1))
