#!/usr/bin/env python

import mechanize
import sys
import re
import os

TCK='26254978452'
HN='1437907'

br = mechanize.Browser()
br.open('http://95.0.108.93:8080/Default.aspx')
sys.stderr.write('Opened site:\n'+ br.title()+'\n')

br.select_form(nr=0)

br['txtTcKimlikNo'] = TCK
br['txtHastaNo'] = HN

br.submit()

br.select_form(nr=0)

# print br.form
# sys.exit()
br['cboLabSonuclari']= ["29/05/2015#66135914"]

print br.form.find_control(type="hidden")
