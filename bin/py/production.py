#!/usr/bin/env python

from mypy.datatools import Frame, Csv
from mypy.utils import strToFloat, sdev, mean
import sys

def addCounts(counts,accum,pivot):
		
	acc_np1 =  	counts['2']['1']
	acc_np2 = 	counts['2']['2']
	acc_both = 	counts['2']['3']
	acc_np1_cum = acc_np1 + acc_both
	acc_np2_cum = acc_np2 + acc_both
	acc_other = counts['2']['4']
	acc_empty = counts['2']['99']

	zero_np1 =  counts['1']['1']
	zero_np2 = 	counts['1']['2']
	zero_both = counts['1']['3']
	zero_np1_cum = zero_np1 + zero_both
	zero_np2_cum = zero_np2 + zero_both
	zero_other= counts['1']['4']
	zero_empty= counts['1']['99']

	acc_cum_total = float(acc_np1 + acc_np2 + 2*acc_both + acc_other)
	zero_cum_total = float(zero_np1 + zero_np2 + 2*zero_both + zero_other)

	acc_total = float(acc_np1 + acc_np2 + acc_both + acc_other)
	zero_total = float(zero_np1 + zero_np2 + zero_both + zero_other)
	
	p_acc_np1 = acc_np1/acc_total*100
	p_acc_np2 = acc_np2/acc_total*100
	p_acc_both = acc_both/acc_total*100
	p_acc_other = acc_other/acc_total*100
	p_acc_np1_cum = acc_np1_cum/acc_cum_total*100
	p_acc_np2_cum = acc_np2_cum/acc_cum_total*100
	p_acc_other_cum = acc_other/acc_cum_total*100

	p_zero_np1 = zero_np1/zero_total*100
	p_zero_np2 = zero_np2/zero_total*100
	p_zero_both = zero_both/zero_total*100
	p_zero_other = zero_other/zero_total*100
	p_zero_np1_cum = zero_np1_cum/zero_cum_total*100
	p_zero_np2_cum = zero_np2_cum/zero_cum_total*100
	p_zero_other_cum = zero_other/zero_cum_total*100

	accum.append([pivot,str(p_acc_np1),str(p_acc_np2),str(p_acc_both),str(p_acc_other),str(p_acc_np1_cum),str(p_acc_np2_cum),str(p_acc_other_cum),str(p_zero_np1),str(p_zero_np2),str(p_zero_both),str(p_zero_other),str(p_zero_np1_cum),str(p_zero_np2_cum),str(p_zero_other_cum),str(acc_np1),str(acc_np2),str(acc_both),str(acc_other),str(zero_np1),str(zero_np2),str(zero_both),str(zero_other)])

frame = Frame(fromfile=sys.argv[1])

vframe = Frame(fromfile='verb-type-correspondence.csv')
verbs = {'simple' : vframe.filter(('Type','simple')).uniqField('Verb'),'complex': vframe.filter(('Type','complex')).uniqField('Verb')}


# oframe = Frame(fromfile='comprehension-outliers.csv')

outliers= []

# for d in oframe.iterFrame():
# 	if d['Reason']=='1':
# 		outliers.append(d['Pid'])
# 	outliers.append(d['Pid'])

item_out_accum = []

for verb in verbs['simple'] + verbs['complex']:
	toverb = frame.filter(('Verb',verb))
	counts = {'1':{'1':0,'2':0,'3':0,'4':0,'99':0}, '2':{'1':0,'2':0,'3':0,'4':0,'99':0}} # 1 for Zero, 2 for Acc
	for d in toverb.iterFrame():
# 		if d['Pid'] in outliers:
# 			continue
		if int(d['Case']) < 3:
			counts[d['Case']][d['Re-mention']] +=1
	addCounts(counts,item_out_accum,verb)

item_out = Frame(['Verb','Acc-NP1%','Acc-NP2%','Acc-Both%','Acc-Other%','Acc-NP1-Cum%','Acc-NP2-Cum%','Acc-Other-Cum%','Zero-NP1%','Zero-NP2%','Zero-Both%','Zero-Other%','Zero-NP1-Cum%','Zero-NP2-Cum%','Zero-Other-Cum%','Acc-NP1-Freq','Acc-NP2-Freq','Acc-Both-Freq','Acc-Other-Freq','Zero-NP1-Freq','Zero-NP2-Freq','Zero-Both-Freq','Zero-Other-Freq'], item_out_accum)

item_out.printFrame('item.csv')


#Participant-based

part_out_accum = []

parts = frame.uniqField('Pid') 


for part in  parts:
	if part in outliers:
		continue

	pf = frame.filter(('Pid',part))
	counts = {'1':{'1':0,'2':0,'3':0,'4':0,'99':0}, '2':{'1':0,'2':0,'3':0,'4':0,'99':0}} # 1 for Zero, 2 for Acc

	for d in pf.iterFrame():
		if int(d['Case']) < 3:
			counts[d['Case']][d['Re-mention']] +=1

	addCounts(counts,part_out_accum,part)


part_out = Frame(['Pid','Acc-NP1%','Acc-NP2%','Acc-Both%','Acc-Other%','Acc-NP1-Cum%','Acc-NP2-Cum%','Acc-Other-Cum%','Zero-NP1%','Zero-NP2%','Zero-Both%','Zero-Other%','Zero-NP1-Cum%','Zero-NP2-Cum%','Zero-Other-Cum%','Acc-NP1-Freq','Acc-NP2-Freq','Acc-Both-Freq','Acc-Other-Freq','Zero-NP1-Freq','Zero-NP2-Freq','Zero-Both-Freq','Zero-Other-Freq'], part_out_accum)

part_out.printFrame('part.csv')


#Participant-based per verb type

""" Verbs are grouped according to whether they favor Acc or Zero in
the count of re-mention. We did this classification manually by
looking at the differences between the cumulative percent of the NP2
re-mentions. Key:. Acc:2 Zero:1
"""
verb_types={'iade etti':'2','goturdu':'2','davet etti':'2','getirdi':'2','konuk etti':'2','aldi':'1','kabul etti':'1','dahil etti':'1','onerdi':'1','tanitti':'1','transfer etti':'1','atadi':'1'}


part_out_accum = []

parts = frame.uniqField('Pid') 


for part in  parts:
# 	if part in outliers:
# 		continue

	pf = frame.filter(('Pid',part))
	counts = {'1':{'1':{'1':0,'2':0,'3':0,'4':0,'99':0}, '2':{'1':0,'2':0,'3':0,'4':0,'99':0}}, '2':{'1':{'1':0,'2':0,'3':0,'4':0,'99':0}, '2':{'1':0,'2':0,'3':0,'4':0,'99':0}}} # 1 for Zero, 2 for Acc

	for d in pf.iterFrame():
		if int(d['Case']) < 3:
			counts[verb_types[d['Verb']]][d['Case']][d['Re-mention']] +=1

	print part

	acc_np1_atype =  	counts['2']['2']['1']
	acc_np2_atype = 	counts['2']['2']['2']
	acc_both_atype = 	counts['2']['2']['3']
	acc_np1_cum_atype = acc_np1_atype + acc_both_atype
	acc_np2_cum_atype = acc_np2_atype + acc_both_atype
	acc_other_atype = counts['2']['2']['4']
	acc_empty_atype = counts['2']['2']['99']

	acc_np1_ztype =  	counts['1']['2']['1']
	acc_np2_ztype = 	counts['1']['2']['2']
	acc_both_ztype = 	counts['1']['2']['3']
	acc_np1_cum_ztype = acc_np1_ztype + acc_both_ztype
	acc_np2_cum_ztype = acc_np2_ztype + acc_both_ztype
	acc_other_ztype = counts['1']['2']['4']
	acc_empty_ztype = counts['1']['2']['99']

	zero_np1_atype =  	counts['2']['1']['1']
	zero_np2_atype = 	counts['2']['1']['2']
	zero_both_atype = 	counts['2']['1']['3']
	zero_np1_cum_atype = zero_np1_atype + zero_both_atype
	zero_np2_cum_atype = zero_np2_atype + zero_both_atype
	zero_other_atype = counts['2']['1']['4']
	zero_empty_atype = counts['2']['1']['99']

	zero_np1_ztype =  	counts['1']['1']['1']
	zero_np2_ztype = 	counts['1']['1']['2']
	zero_both_ztype = 	counts['1']['1']['3']
	zero_np1_cum_ztype = zero_np1_ztype + zero_both_ztype
	zero_np2_cum_ztype = zero_np2_ztype + zero_both_ztype
	zero_other_ztype = counts['1']['1']['4']
	zero_empty_ztype = counts['1']['1']['99']


	acc_cum_total_atype = float(acc_np1_atype + acc_np2_atype + 2*acc_both_atype + acc_other_atype)
	zero_cum_total_atype = float(zero_np1_atype + zero_np2_atype + 2*zero_both_atype + zero_other_atype)

	acc_total_atype = float(acc_np1_atype + acc_np2_atype + acc_both_atype + acc_other_atype)
	zero_total_atype = float(zero_np1_atype + zero_np2_atype + zero_both_atype + zero_other_atype)

	acc_cum_total_ztype = float(acc_np1_ztype + acc_np2_ztype + 2*acc_both_ztype + acc_other_ztype)
	zero_cum_total_ztype = float(zero_np1_ztype + zero_np2_ztype + 2*zero_both_ztype + zero_other_ztype)

	acc_total_ztype = float(acc_np1_ztype + acc_np2_ztype + acc_both_ztype + acc_other_ztype)
	zero_total_ztype = float(zero_np1_ztype + zero_np2_ztype + zero_both_ztype + zero_other_ztype)

	p_acc_np1_atype = acc_np1_atype/acc_total_atype*100
	p_acc_np2_atype = acc_np2_atype/acc_total_atype*100
	p_acc_both_atype = acc_both_atype/acc_total_atype*100
	p_acc_other_atype = acc_other_atype/acc_total_atype*100
	p_acc_np1_cum_atype = acc_np1_cum_atype/acc_cum_total_atype*100
	p_acc_np2_cum_atype = acc_np2_cum_atype/acc_cum_total_atype*100
	p_acc_other_cum_atype = acc_other_atype/acc_cum_total_atype*100

	p_zero_np1_atype = zero_np1_atype/zero_total_atype*100
	p_zero_np2_atype = zero_np2_atype/zero_total_atype*100
	p_zero_both_atype = zero_both_atype/zero_total_atype*100
	p_zero_other_atype = zero_other_atype/zero_total_atype*100
	p_zero_np1_cum_atype = zero_np1_cum_atype/zero_cum_total_atype*100
	p_zero_np2_cum_atype = zero_np2_cum_atype/zero_cum_total_atype*100
	p_zero_other_cum_atype = zero_other_atype/zero_cum_total_atype*100

	p_acc_np1_ztype = acc_np1_ztype/acc_total_ztype*100
	p_acc_np2_ztype = acc_np2_ztype/acc_total_ztype*100
	p_acc_both_ztype = acc_both_ztype/acc_total_ztype*100
	p_acc_other_ztype = acc_other_ztype/acc_total_ztype*100
	p_acc_np1_cum_ztype = acc_np1_cum_ztype/acc_cum_total_ztype*100
	p_acc_np2_cum_ztype = acc_np2_cum_ztype/acc_cum_total_ztype*100
	p_acc_other_cum_ztype = acc_other_ztype/acc_cum_total_ztype*100

	p_zero_np1_ztype = zero_np1_ztype/zero_total_ztype*100
	p_zero_np2_ztype = zero_np2_ztype/zero_total_ztype*100
	p_zero_both_ztype = zero_both_ztype/zero_total_ztype*100
	p_zero_other_ztype = zero_other_ztype/zero_total_ztype*100
	p_zero_np1_cum_ztype = zero_np1_cum_ztype/zero_cum_total_ztype*100
	p_zero_np2_cum_ztype = zero_np2_cum_ztype/zero_cum_total_ztype*100
	p_zero_other_cum_ztype = zero_other_ztype/zero_cum_total_ztype*100

	part_out_accum.append([part,str(p_acc_np1_atype),str(p_acc_np2_atype),str(p_acc_both_atype),str(p_acc_other_atype),str(p_acc_np1_cum_atype),str(p_acc_np2_cum_atype),str(p_acc_other_cum_atype),str(p_zero_np1_atype),str(p_zero_np2_atype),str(p_zero_both_atype),str(p_zero_other_atype),str(p_zero_np1_cum_atype),str(p_zero_np2_cum_atype),str(p_zero_other_cum_atype),str(acc_np1_atype),str(acc_np2_atype),str(acc_both_atype),str(acc_other_atype),str(zero_np1_atype),str(zero_np2_atype),str(zero_both_atype),str(zero_other_atype),str(p_acc_np1_ztype),str(p_acc_np2_ztype),str(p_acc_both_ztype),str(p_acc_other_ztype),str(p_acc_np1_cum_ztype),str(p_acc_np2_cum_ztype),str(p_acc_other_cum_ztype),str(p_zero_np1_ztype),str(p_zero_np2_ztype),str(p_zero_both_ztype),str(p_zero_other_ztype),str(p_zero_np1_cum_ztype),str(p_zero_np2_cum_ztype),str(p_zero_other_cum_ztype),str(acc_np1_ztype),str(acc_np2_ztype),str(acc_both_ztype),str(acc_other_ztype),str(zero_np1_ztype),str(zero_np2_ztype),str(zero_both_ztype),str(zero_other_ztype)])


part_out = Frame(['Pid','Acc-NP1%_AccType','Acc-NP2%_AccType','Acc-Both%_AccType','Acc-Other%_AccType','Acc-NP1-Cum%_AccType','Acc-NP2-Cum%_AccType','Acc-Other-Cum%_AccType','Zero-NP1%_AccType','Zero-NP2%_AccType','Zero-Both%_AccType','Zero-Other%_AccType','Zero-NP1-Cum%_AccType','Zero-NP2-Cum%_AccType','Zero-Other-Cum%_AccType','Acc-NP1-Freq_AccType','Acc-NP2-Freq_AccType','Acc-Both-Freq_AccType','Acc-Other-Freq_AccType','Zero-NP1-Freq_AccType','Zero-NP2-Freq_AccType','Zero-Both-Freq_AccType','Zero-Other-Freq_AccType','Acc-NP1%_ZeroType','Acc-NP2%_ZeroType','Acc-Both%_ZeroType','Acc-Other%_ZeroType','Acc-NP1-Cum%_ZeroType','Acc-NP2-Cum%_ZeroType','Acc-Other-Cum%_ZeroType','Zero-NP1%_ZeroType','Zero-NP2%_ZeroType','Zero-Both%_ZeroType','Zero-Other%_ZeroType','Zero-NP1-Cum%_ZeroType','Zero-NP2-Cum%_ZeroType','Zero-Other-Cum%_ZeroType','Acc-NP1-Freq_ZeroType','Acc-NP2-Freq_ZeroType','Acc-Both-Freq_ZeroType','Acc-Other-Freq_ZeroType','Zero-NP1-Freq_ZeroType','Zero-NP2-Freq_ZeroType','Zero-Both-Freq_ZeroType','Zero-Other-Freq_ZeroType'], part_out_accum)

part_out.printFrame('part-per-verb.csv')


# for case in [1,2]:
# 
# 	cframe = frame.filter(('case',str(case)),  ('response','1'))
# 
# 	print 'case ' + str(case) + ' NP1: ' + str(len(cframe.iterFrame()))
# 
# 	cframe = frame.filter(('case',str(case)), ('response','2'))
# 	print 'case ' + str(case) + ' NP2: ' + str(len(cframe.iterFrame()))
	

