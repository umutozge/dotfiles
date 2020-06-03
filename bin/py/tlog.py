#!/usr/bin/env python

import sys
import os
from datetime import date, datetime, timedelta, time
import re
import exceptions

class tlog():
	
	PATH = os.environ['HOME']+'/lib/tlog/'

	def __init__(self,mode,task=''):

		if task=='':
			if mode=='status':
				logs = os.listdir(self.PATH)
				for log in logs:
					tlog('status',log)
				sys.exit(0)
			else:
				sys.stderr.write(mode+' what?\n')
				sys.exit(0)

		self.task = task			

		#When?
		self.today = datetime.today().date()
		self.now = datetime.now()
		#Where?
		self.path = tlog.PATH + task
		try:
			self.db = open(self.path,'r')
		except IOError:
			self.db = open(self.path,'w')
			self.db.close()
			self.db = open(self.path,'r')


		date_pattern = re.compile('(\d\d\d\d)-(\d\d)-(\d\d)')
		lines = self.db.readlines()
		lastdate = None 
		for l in reversed(lines):
			m = date_pattern.search(l)	
			if m:
				lastdate = date(int(m.group(1)),int(m.group(2)),int(m.group(3)))
				break

		#if it was the first time the task is being logged... 
		if not lastdate:
			lastdate = self.today - timedelta(days=1)
		self.db.close()

		self.db = open(self.path,'a')
		#increment the lastdate and then fill in the unlogged days if there are any.
		lastdate = lastdate + timedelta(days=1)
		while self.today >= lastdate:
			self.db.write(lastdate.isoformat()+'\n')
			lastdate = lastdate + timedelta(days=1)

		#read the current status from the last line of the database.	
		try:
			status = lines[-1].strip()	
		except IndexError:
			status = '.'

		if mode == 'log':
			if status == '.' or date_pattern.search(status):
				self.db.write(self.now.time().strftime('%H:%M:%S')+'\n')
				sys.stderr.write('*- %s\n'%(self.task))
			elif re.search('\d\d:\d\d',status):
				self.db.write(self.now.time().strftime('%H:%M:%S')+'\n.\n')
				sys.stderr.write('-- %s\n'%(self.task))
			else:
				raise DatabaseError(self)
		elif mode == 'status':
			sys.stderr.write(self._get_stat(status))
		elif mode == 'report':
			self.db.close()
			self._print_report(self._report())


	def _report(self):
		db = open(self.path,'r') 
		report = {} 
		lines = list(reversed(db.readlines()))

		duration = timedelta() 
		first = True
		date = self.today
		while lines:
			l = lines.pop(0)
			if l.strip() == '.':
				#read a time block
				end = eval('datetime('+','.join(map(self._rem_zero,[x.split('.')[0] for x in date.isoformat().split('-') + lines.pop(0).split(':')]))+')')
				start = eval('datetime('+','.join(map(self._rem_zero,[x.split('.')[0] for x in date.isoformat().split('-') + lines.pop(0).split(':')]))+')')
				duration += end - start
				first = False
				continue
			elif l.strip().find(':') != -1 and first:
				start = eval('datetime('+','.join(map(self._rem_zero,[x.split('.')[0] for x in date.isoformat().split('-') + l.split(':')]))+')')
				end = self.now
				duration += end -start 
				first = False
				continue
			elif l.strip().find(':') != -1 and not first:
				raise DatabaseError(self)

			m = re.search('\d\d\d\d-\d\d-\d\d',l)	

			if not m:
				raise DatabaseError(self)

			report[m.group(0)] = duration.seconds

			duration = timedelta()

		return report

	def _print_report(self,report):
		keys = sorted(report.keys())

		for key in keys:
			print key+'\t'+self._sec2hour(report[key])

	def _sec2hour(self,seconds):
		mins = seconds/60
		hrs = mins/60
		mins = mins%60
		return str(hrs)+'h'+str(mins)+'m'

	def _get_stat(self,status):
		if status == '.' or status.find('-') != -1:
			return '-- %s\n'%(self.task)
		else:
			return '*- %s\n'%(self.task)

	def _rem_zero(self,input):
		if input[0]=='0':
			return input[1:]
		else:
			return input
		
	def _exit(self,code=0):
		self.db.close()	
		sys.exit(code)

class DatabaseError(exceptions.Exception):
	
	def __init__(self,owner):
		self.owner = owner	

	def __str__(self): 
		print '\n\n\tDatabase in %s is broken, please check for errors.'%(self.owner.path)

