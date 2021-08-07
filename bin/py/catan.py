#!/usr/bin/python3

import random
import sys
import os

random.seed()

def roll ():
	return random.randint(1,6),random.randint(1,6)

name_dict = {1:'Oktay',3:'Tubiş',2:'Umiş'}

first_player = random.randint(1,3)

print(name_dict[first_player],' is the first player')

input('Press enter to continue')

report = dict()
count = first_player - 1 
turn_count = 1
while(True):
	inp = input()
	os.system('clear')
	print('Turn: ',turn_count)
	print()
	turn_count += 1
	if not inp=='q':
		result = roll()
		s = result[0] + result[1]
		if report.get(s):
			report[s] += 1
		else:
			report[s] = 1
		sys.stderr.write(name_dict[(count % 3) + 1] +'  %i : %i\t\t%i\n' % (max(result),min(result),s))
		total = sum(report.values())
		count += 1
		print()
		print('Next player: ', name_dict[(count % 3) + 1])
		print()
		report_list = list(sorted(report.items(), key=lambda x: x[1]))
		report_list.reverse()
		for x,y in report_list:
			print(str(x)+'\t'+str(y)+'\t'+str(int(y/total*100))+'%')
	else:
		break
