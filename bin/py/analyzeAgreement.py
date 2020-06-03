#!/usr/bin/env python

from mypy.CoderAgreement import Agreement
import sys
import re


cat_tab = {'backward_linking.csv':['empty','markable','undecided'],\
'animacy.csv':['human','animate','inanim_conc_obj','inanim_underspec_obj','abstract','undecided'],\
'case_marking.csv':['acc','zero'],\
'forward_linking.csv':['none','anaphora','elaboration','elab_anaph'],\
'level_of_subord.csv':['0','1','2'],\
'descriptive_content.csv':['none','adj.','more'],\
'optional.csv':['yes','no'],\
'focal.csv':['yes','no','undecided'],\
'binding.csv':['none','intens.','nominal']}


def write_table(lot):
	out = open('agreement.tex','w')
	out.write("""\\begin{tabular}{|l|ccc|}
\\hline
\\multirow{2}{*}{Category} & \multicolumn{3}{c|}{{Agreement}} \\\\ 
& $\\sigma$ & $\\pi$ & $\\kappa$\\\\ \\hline
""")
	for x in lot:
		cat = x[0][:x[0].find('.')]
		cat = re.sub('_',' ',cat)
		cat = cat[0].upper()+cat[1:]
		cat = re.sub('cal','cal or not',cat)
		cat = re.sub('nal','nality of case',cat)
		cat = re.sub('ord','ordination',cat)
		out.write("%s&%s&%s&%s\\\\ \\hline \n"%(cat,x[1]['s'],x[1]['pi'],x[1]['k']))
	out.write("""\\end{tabular}""")

accum=[]
for arg in sys.argv[1:]:
	print arg
	agreement = Agreement(arg,cat_tab[arg])
	agr = agreement.get_agreement()
	print agr
	accum.append((arg,agr))

write_table(accum)
