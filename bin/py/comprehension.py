#!/usr/bin/env python

from mypy.datatools import Frame, Csv
from mypy.utils import strToFloat, sdev, mean
import sys

frame = Frame(fromfile=sys.argv[1])

vframe = Frame(fromfile='verb-type-correspondence.csv')
verbs = {'simple' : vframe.filter(('Type','simple')).uniqField('Verb'),'complex': vframe.filter(('Type','complex')).uniqField('Verb')}


oframe = Frame(fromfile='comprehension-outliers.csv')

outliers= []

for d in oframe.iterFrame():
	if d['Reason']=='2':
		outliers.append(d['Pid'])

item_out_accum = []

for verb in verbs['simple'] + verbs['complex']:
	toverb = frame.filter(('Verb',verb))
	counts = {'1':{'1':0,'2':0}, '2':{'1':0,'2':0}} # 1 for Zero, 2 for Acc
	for d in toverb.iterFrame():
		if d['Pid'] in outliers:
			continue
		if int(d['Case']) < 3:
			counts[d['Case']][d['Response']] +=1
	acc_np1 =  counts['2']['1']
	acc_np2 = 	counts['2']['2']
	zero_np1 =  counts['1']['1']
	zero_np2 = counts['1']['2']
	
	

	acc_total = float(acc_np1 + acc_np2)
	zero_total = float(zero_np1 + zero_np2)

	p_acc_np1 = acc_np1/acc_total*100
	p_acc_np2 = acc_np2/acc_total*100

	acc_np1_bias = p_acc_np1-p_acc_np2 

	p_zero_np1 = zero_np1/zero_total*100
	p_zero_np2 = zero_np2/zero_total*100

	zero_np1_bias = p_zero_np1-p_zero_np2 

	item_out_accum.append([verb,str(p_acc_np2),str(p_acc_np2),str(p_zero_np1),str(p_zero_np2),str(acc_np1),str(acc_np2),str(zero_np1),str(zero_np2)])


item_out = Frame(['Verb','Acc-NP1%','Acc-NP2%','Zero-NP1%','Zero-NP2%','Acc-NP1-Freq','Acc-NP2-Freq','Zero-NP1-Freq','Zero-NP2-Freq'], item_out_accum)

item_out.printFrame('item.csv')

part_out_accum = []

parts = frame.uniqField('Pid') 

verb_types={'iade etti':'2','goturdu':'2','davet etti':'2','getirdi':'2','konuk etti':'2','aldi':'2','kabul etti':'1','dahil etti':'1','onerdi':'1','tanitti':'1','transfer etti':'1','atadi':'1'}

for part in  parts:
	if part in outliers:
		continue
	pf = frame.filter(('Pid',part))
	counts = {'1':{'1':{'1':0,'2':0}, '2':{'1':0,'2':0}}, '2':{'1':{'1':0,'2':0}, '2':{'1':0,'2':0}}} # 1 for Zero, 2 for Acc
		
	for d in pf.iterFrame():
		if int(d['Case']) < 3:
 			counts[verb_types[d['Verb']]][d['Case']][d['Response']] += 1

	acc_np1_at =  counts['2']['2']['1']
	acc_np2_at = 	counts['2']['2']['2']
	zero_np1_at =  counts['2']['1']['1']
	zero_np2_at = counts['2']['1']['2']
	acc_total_at = float(acc_np1_at + acc_np2_at)
	zero_total_at = float(zero_np1_at + zero_np2_at)
	p_acc_np1_at = acc_np1_at/acc_total_at*100
	p_acc_np2_at = acc_np2_at/acc_total_at*100
	p_zero_np1_at = zero_np1_at/zero_total_at*100
	p_zero_np2_at = zero_np2_at/zero_total_at*100

	acc_np1_zt =  counts['1']['2']['1']
	acc_np2_zt = 	counts['1']['2']['2']
	zero_np1_zt =  counts['1']['1']['1']
	zero_np2_zt = counts['1']['1']['2']
	acc_total_zt = float(acc_np1_zt + acc_np2_zt)
	zero_total_zt = float(zero_np1_zt + zero_np2_zt)
	p_acc_np1_zt = acc_np1_zt/acc_total_zt*100
	p_acc_np2_zt = acc_np2_zt/acc_total_zt*100
	p_zero_np1_zt = zero_np1_zt/zero_total_zt*100
	p_zero_np2_zt = zero_np2_zt/zero_total_zt*100

	part_out_accum.append([part,str(p_acc_np1_at),str(p_acc_np2_at),str(p_zero_np1_at),str(p_zero_np2_at),str(acc_np1_at),str(acc_np2_at),str(zero_np1_at),str(zero_np2_at),str(p_acc_np1_zt),str(p_acc_np2_zt),str(p_zero_np1_zt),str(p_zero_np2_zt),str(acc_np1_zt),str(acc_np2_zt),str(zero_np1_zt),str(zero_np2_zt)])

part_out = Frame(['Pid','Acc-NP1%_AccType','Acc-NP2%_AccType','Zero-NP1%_AccType','Zero-NP2%_AccType','Acc-NP1-Freq_AccType','Acc-NP2-Freq_AccType','Zero-NP1-Freq_AccType','Zero-NP2-Freq_AccType','Acc-NP1%_ZeroType','Acc-NP2%_ZeroType','Zero-NP1%_ZeroType','Zero-NP2%_ZeroType','Acc-NP1-Freq_ZeroType','Acc-NP2-Freq_ZeroType','Zero-NP1-Freq_ZeroType','Zero-NP2-Freq_ZeroType'], part_out_accum)


part_out.printFrame('part.csv')



# for case in [1,2]:
# 
# 	cframe = frame.filter(('case',str(case)),  ('response','1'))
# 
# 	print 'case ' + str(case) + ' NP1: ' + str(len(cframe.iterFrame()))
# 
# 	cframe = frame.filter(('case',str(case)), ('response','2'))
# 	print 'case ' + str(case) + ' NP2: ' + str(len(cframe.iterFrame()))
	

