#!/usr/bin/env python
"""
A module for trimming and analzing eye-tracking data.
"""

import sys
import os
import re
import exceptions
import copy
import xlrd, xlwt 
from optparse import OptionParser
from mypy.datatools import * 
from mypy import utils
from datetime import datetime

class Experiment(object):
	"""An experiment with a number of sessions."""
	def __init__(self,raw_path='raw/',conditions=None, validity='2', aoicats="dist,target,topic", other="Other", timewindow_info=None,required_info="Participant,Group,AgeGroup,Session,TrialId,Item,Condition,RTTime,TimePeriod,TimePeriodSpa,AOICat,AOIStimulus,ClickAcc,ValidityLeftEye,ValidityRightEye",trim_inaccurate=False,root_dir='.',spa_plot=None,images=None,item_filter=lambda x:True, level=3, trial_onset_label=None, trial_offset_label=None):
		"""Initialize an Experiment instance.
			
			Keyword args:

			raw_path -- path to look for raw data files.
			conditions -- manipulated conditions.
			validity -- 2: both eye need be 0; 1: at least one eye need be 0
			aoicats -- comma separated names of Area of Interest categories of the experiment
			timewindow_info -- a csv file with the info; 'insert': calculate from log data (text files) and insert; None: do nothing, it is already in the gazedata 
			required_info -- comma separated column names that needs to be kept from the original data 
			spa_plot -- if None no spa plot is needed; otherwise provide the interval length for the plot
			trim_inaccurate -- whether you need to get rid of inaccurate responses; they will be counted in the error analysis in any case
			images -- name of the image categories (UpLeftImage, LowCenterImage etc.); these are used to construct item names 
			item_filter -- a boolean function to decide whether to include an item 
			level -- the level of loop where the critical trial info is in e-prime txt files

		"""
		
		self._Conditions = conditions.split(',')
		self._Sessions = []
		self._Participants = []
		self._Groups = []
		self._RawPath = raw_path
		self._Validity = int(validity)
		self._Level = level
		self._AOICats = aoicats.split(',')+[other]
		self._NumOfAOIs = len(self._AOICats) - 1 #subtract the other cat
		self._TrimInaccurate = trim_inaccurate
		self._RequiredInfo = required_info.split(',') # required fields in the data, the rest is removed 
		for i in range(self._NumOfAOIs):
			self._RequiredInfo.append('AOI'+str(i+1))
		for i in range(self._NumOfAOIs):
			self._RequiredInfo.append('AOI'+str(i+1)+'Cat')
		self._RequiredInfo.append('AOI')
		self._AnalDate = str(datetime.today().date())
		self._AnalTime = str(datetime.today()).split(' ')[1]
		self._AnalTime = self._AnalTime[:self._AnalTime.index('.')]
		self._SpaInterval = spa_plot	
		self._Images = images.split(',')
		self._ItemFilter = item_filter
		self.TrialOnsetLabel=trial_onset_label
		self.TrialOffsetLabel=trial_offset_label

		"""Check whether you need to generate csv files from gazedata."""
		self._data_clean = filter(lambda x: x.endswith('.csv'), os.listdir(self.RawPath)) != []

		"""Initialize a frame to collect inaccurate responses"""
		self.Inaccurates = Frame(['Participant','Condition','Item']) 

		"""Decide what to do about time windows"""
		if timewindow_info is None:
			self.TWInfo = None
		elif timewindow_info.endswith('csv') :
			self.TWInfo = self._compile_item_info(timewindow_info)
		elif timewindow_info == 'insert':
			#TODO: read time window info from session files and bind it to self.TWInfo
			pass

		"""Collect sessions"""
		for f in  filter(lambda x: x.endswith('.text'), os.listdir(self.RawPath)):
			self.Sessions.append(Session(self,f))

		"""Find the groups in the experiment"""
		groups = set()
		for s in self.Sessions:
			groups.add(s.Group)
		self.Groups = list(groups)
		



		"""Collect data into a single frame"""
		sys.stderr.write('\n\nMerging raw data and writing to disk...')
		self.NumOfTrials = 0 
		self.Data = self.collect_data()
			
		self.Data.printFrame('exp_data_for_debug.csv') # it is useful to have this written down for debugging purposes
		sys.stderr.write('\t[OK]\n')

		"""Get the name of the experiment from the first Session file's prefix until '-' and remove the group letter from the name"""
# 		pat = re.compile('^([^-]*)-([^-]*)')
# 		m = pat.search(self._Sessions[0].ID)
# 		self._Name = '-'.join([m.group(1)[:-1],m.group(2)])
 		pat = re.compile('^([^-]*)--.*')
 		m = pat.search(self._Sessions[0].ID)
 		self._Name = m.group(1)

		"""Check or create the output location"""
		self.curDir = os.getcwd()
		self.outPath = self._AnalDate+'-'+self._Name+'-TrimmedData'
		os.chdir(root_dir)
		if not os.access(self.outPath,os.F_OK):
			os.makedirs(self.outPath)
		
		"""Prepare for logging and output"""
		os.chdir(self.outPath)
		self.logFile = open(self._Name+'-exp-info-'+self._AnalDate+'.txt','w')
		self._write_log()


		"""The major operations performed in a row"""	
		self.trim_data()
		self.report_fixation(['Participant','Item','Condition'],['Participant','Condition'],['Item','Condition'])
		SpaPlot(self)
		
	
	def _exit(self):
		os.chdir(self.curDir)
		sys.exit()

	def _write_log(self):
		"""Write log information"""
		self.logFile.write('***START LOG***')
		self.logFile.write('\nDate of analysis:\t'+self._AnalDate)
		self.logFile.write('\nTime of analysis:\t'+self._AnalTime)
		self.logFile.write('\n\nExperiment:\t'+self._Name)
		self.logFile.write('\nGroups:\t'+','.join(self.Groups))
		self.logFile.write('\nNumber of sessions:\t'+ str(len(self._Sessions)))
		validity_map = lambda x: {0:'neither eye',1:'at least one eye',2:'both eyes'}[x]
		self.logFile.write('\nValidity requirement:\t'+validity_map(self._Validity) )	
		inacc_map = lambda x: {True: 'only accurate responses included',False:'all responses included'}[x]
		self.logFile.write('\nAccuracy requirement:\t' + inacc_map(self._TrimInaccurate))	


		"""Extract info re items and groups"""
		for g in self._Groups:
			self.logFile.write('\n\nItems of group '+g+'\n')	

			for s in self._Sessions:
				if s.Group == g:
					item_bag = set()
					for t in s.Trials:
						if self._ItemFilter(t.Item):
							item_bag.add((t.Condition,t.Item))
					for i in item_bag:
						self.logFile.write('\n%s -- %s'%i)
					break

		self.logFile.write('\n\nSessions of the experiment:\n')
		slist = []
		for s in self._Sessions:
			slist.append('\n'+s.ID+'\t['+str(len(s.Trials))+ ' trials]')

		for s in sorted(slist):
			self.logFile.write(s)

		self.logFile.write('\n***END LOG***')

	def trim_data(self,trim_noncrit=True,trim_invalid=True):
		"""Trim the data of the experiment, write a report"""

		sys.stderr.write('\nTrimming data...')

		fields = ['Condition','Participant','Item']
		values = {}
		for f in fields:
			values[f] = self.Data.uniqField(f)

		total_looks = len(self.Data.data)
		total_trials = self.NumOfTrials 
	
		counts = {'Invalid':{'Participant':{},'Condition':{},'Item':{}}, 'Inaccurate':{'Participant':{},'Condition':{},'Item':{}}}

		newdata = Frame(self.Data.header)
		for d in self.Data:#do NOT use removeData in this loop: it is time costly and mutates the iterator
			remove = False
			"""Remove invalid gazes"""
			if not self._check_validity(d):
				self._update_counts(counts['Invalid'],d)			
				if trim_invalid:
					remove = True
			if trim_noncrit:
				"""Remove and skip non-critical conditions"""
				if not self._check_critical(d):
					remove = True
			if not remove:
				newdata.addData(d)	
		
		del self.Data
		self.Data = newdata
		print self.Data.printFrame();sys.exit(0)	

		"""Write the info to an excel workbook"""
		wb = xlwt.Workbook() 
		fname = self.Name+'-error-analyses-'+str(datetime.today().date())+'.xls'
		f = lambda x:int(x)*' (removed)'	
		label_inv = '#Invalid'+f(trim_invalid)
		label_inacc = '#Inaccurate'+f(self._TrimInaccurate)
		label_perc_inv = '%Invalid looks in total of '+str(total_looks)
		label_perc_inacc = '%Inaccurate trials in total of '+ str(total_trials)

		"""Report invalid looks"""
		resthead= [label_inv,label_perc_inv]
		for f in fields:
			header = [f]+resthead
			frame = Frame(header)
			for x in values[f]:
				d = dict()
				d[f] = x	
				try:
					d[label_inv] = counts['Invalid'][f][x] 
				except KeyError:
					d[label_inv] = 0
				d[label_perc_inv] = d[label_inv]/float(total_looks)*100 
				frame.addData(d) 
			invtot = sum(frame.getField(label_inv))
			frame.addData({f:'Total',label_inv:invtot,label_perc_inv:invtot/float(total_looks)*100})
			frame.printFrame(wb,'InvldLooks-per-'+f,fname)

		"""Report inaccurate trials"""

		for d in self.Inaccurates:
			for f in fields:
				try:
					counts['Inaccurate'][f][d[f]] +=1
				except KeyError:
					counts['Inaccurate'][f][d[f]] =1

		resthead= [label_inacc,label_perc_inacc]
		for f in fields:
			header = [f]+resthead
			frame = Frame(header)
			for x in values[f]:
				d = dict()
				d[f] = x	
				try:
					d[label_inacc] = counts['Inaccurate'][f][x] 
				except KeyError:
					d[label_inacc] = 0
				d[label_perc_inacc] = d[label_inacc]/float(total_trials)*100 
				frame.addData(d) 
			inacctot = sum(frame.getField(label_inacc))
			frame.addData({f:'Total',label_inacc:inacctot,label_perc_inacc:inacctot/float(total_trials)*100})
			frame.printFrame(wb,'InaccTrials-per-'+f,fname)

		self.Inaccurates.printFrame(wb,'ListOfInaccTrials'+f,fname)
		sys.stderr.write('\t[OK]')

	def _update_counts(self,dic,data):
		for x in ['Participant','Condition','Item']:
			try:
				dic[x][data[x]] += 1
			except KeyError:
				dic[x][data[x]] = 1

	def _check_validity(self,data):
		left, right = (int(data['ValidityLeftEye']),int(data['ValidityRightEye']))
		if self.Validity == 2:
			return left == 0 and right == 0
		elif self.Validity == 1:
			return left == 0 or right == 0 
		elif self.Validity == 0:
			return True
		else:
			raise UnrecognizedValue('Validity',str(self.Exp.Validity))

	def _check_critical(self,data):
		return data['Condition'] in self.Conditions and self._ItemFilter(data['Item'])

	def _compile_item_info(self,infofile):
		"""Compile item onset, offset, duration info into a hierarchical dict from a csv file
		
			The structure of the dict is item_name/cond/tw_name/{onset,offset,duration}
		"""
		inp = Frame(fromfile=infofile)
		"""fix item names, TODO: this will go when we have consistent naming"""
		for d in inp:
			d['Item Name'] = '-'.join(sorted(d['Item Name'].split('-')))

		items = inp.uniqField('Item Name')
		conds = self.Conditions
		tws = filter(lambda x: x.endswith('Onset'),inp.header)
		tws = ['TW'+str(i+1)+'_'+re.sub('Onset','',x) for i, x in enumerate(tws)]
		self.TWs = tws
		retval ={}
		
		for i in items:
			print i
			f = inp.filter(('Item Name',i))
			cdict = dict()
			for c in conds:
				d = f.getData('Condition',c)
				twdict = dict()
				for tw in tws:
					tdict = dict()	
					for k in ['Onset','Offset']:
						tdict[k]=d[tw[tw.index('_')+1:]+k]
					twdict[tw]=tdict
				cdict[c]=twdict	
			retval[i] = cdict 
		return retval

	def collect_data(self):
		"""Collect the data of the Experiment into a single frame and keep it in self.Data"""
		"""Also collect here count infomation re accuracy"""
		data_accum = Frame()
		for s in self.Sessions:
			trials = s.Trials	
			for trial in trials:
				print trial.Item,trial.Session.ID,len(trial.Data.data),trial.Accurate
				self.NumOfTrials +=1
				if not trial.Accurate:
					d = dict()
					data = trial.Data.data[0]
					for x in ['Participant','Condition','Item']:
						d[x]=data[x]
					self.Inaccurates.addData(d)
					if not self._TrimInaccurate:
						data_accum.append(trial.get_data())#take a copy of the Trial data
				else:
					data_accum.append(trial.get_data()) #take a copy of the Trial data
  				del trial.Data #delete the original to free some memory
		return data_accum				

	@property
	def Conditions(self):
		"""Critical conditions of the experiment"""
		return self._Conditions

	@property
	def NumOfAOIs(self):
		"""Number of area of interests in the experiment"""
		return self._NumOfAOIs
	@NumOfAOIs.setter
	def NumOfAOIs(self,value):
		self._NumOfAOIs = value

	@property
	def Sessions(self):
		"""List of Session instances in the experiment"""
		return self._Sessions
	@Sessions.setter
	def Sessions(self,value):
		self._Sessions = value

	@property
	def RawPath(self):
		"""path to look for raw data files"""
		return self._RawPath

	@property
	def Groups(self):
		"""Experimental groups in the experiment"""
		return self._Groups
	@Groups.setter
	def Groups(self,value):
		self._Groups = value

	@property
	def Validity(self):
		"""Validity requirement for fixations: 2 means both eyes must be 0, 1 means only one eye."""
		return self._Validity
	@Validity.setter
	def Validity(self,value):
		self._Validity = value

	@property
	def AOICats(self):
		"""Names of Area of Interest categories of the experiment"""
		return self._AOICats
	@AOICats.setter
	def AOICats(self,value):
		self._AOICats = value

	@property
	def RequiredInfo(self):
		"""List of columns representing the information that needs to be retained (or computed) from the original data"""
		return self._RequiredInfo
	@RequiredInfo.setter
	def RequiredInfo(self,value):
		self._RequiredInfo = value

	@property
	def Name(self):
		"""Name of the experiment as extracted from session names"""
		return self._Name
	@Name.setter
	def Name(self,value):
		self._Name = value

	@property
	def Participants(self):
		"""Participants of the experiment"""
		return self._Participants
	@Participants.setter
	def Participants(self,value):
		self._Participants = value

	def get_session(self,sessionid):
		"""Return the Session instance with the id sessionid"""
		for s in self.Sessions:
			if s.ID == sessionid:
				return s

	def report_items(self,write):
		"""Collect and report info on item durations. 
		TODO: this will be depracated when we start to require to have the item timing information as time_info_file parameter of the Experiment class"""
		sample_sessions=[]
		for g in self.Groups:
			for s in self.Sessions:
				if s.Group == g:
					sample_sessions.append(s)	
					break
		item_frame_header = ['Item','Condition','NP1Onset','NP2Onset','AuxOnset','VerbOnset','NP2Offset']
		item_frame = Frame(item_frame_header) 
		for s in sample_sessions:
			for t in s.Trials:
				data = {'Item':t.Item.ID}	
				for h in item_frame_header[1:]:
					data[h]=eval('t.Item.'+h)
				item_frame.addData(data)
	
		"""Compute means for each condition and write the output for each condition to an excel workbook"""
		wb = xlwt.Workbook()	
		for cond in self.Conditions:
			condframe = item_frame.filter(('Condition',cond))
			data = {'Item':'Means'}
			for f in condframe.header[2:]:
				data[f] = utils.mean(condframe.getField(f))
			condframe.addData(data)
			condframe.printFrame(wb,cond,self.Name+'-item-durations.xls')
		

	def report_fixation(self,*keyss):
		sys.stderr.write('\n\nCalculating and reporting fixation information...')
		wb = xlwt.Workbook()
		for keys in keyss:	
			self._report_fixation(wb,keys)
		filename = self.Name+'-fixation-data-'+str(datetime.today().date())+'.xls'
		wb.save(filename)
		sys.stderr.write('\t[OK]\n')

	def _report_fixation(self,wb,keys):
		fix = self.compute_fixations(self.Data,keys) #compute and get the fixation data
		header = keys + ['TimePeriod'] + [x+ 'PercFix' for x in self.AOICats] #construct the header for the output Frame instance
		sheetname = '-'.join(keys)
		rows = self._tabulize(fix,keys+['TimePeriod'])

		
		utils.writeXLsheet(wb,sheetname,[header]+rows)
		if len(keys) == 2:
			frame = Frame(header,rows)
			elimframe = frame.elim_fields(keys[0],[keys[1]]+['TimePeriod'])
			head = elimframe.header
			head = map(lambda x: re.sub('Nominative','Nom',re.sub('Accusative','Acc',x)),head)#ACCUSATIVE
			rows = elimframe.printFrame()
			pframe = self._compute_preference(elimframe)
			phead = pframe.header
			phead = map(lambda x: re.sub('Nominative','Nom',re.sub('Accusative','Acc',x)),phead)#ACCUSATIVE
			prows = pframe.printFrame()
			utils.writeXLsheet(wb,sheetname+'-ANOVA',[head]+rows[1:])
			utils.writeXLsheet(wb,sheetname+'-Prefs',[phead]+prows[1:])

	def _compute_preference(self,inframe):
		keys = []	
		for k in inframe.header[1:]:
			if k.endswith('ThemePercFix'):
				keys.append(k.split('-')[0]+'-'+k.split('-')[1])
		
		newheader = [x+'-ThemePref' for x in keys]
		retframe = Frame([inframe.header[0]]+newheader)
		
		pivot = inframe.header[0] 

		for d  in inframe:
			nd = {}	
			nd[pivot] = d[pivot]
			for k in newheader:
				s = k.split('-') 
				prefix = '-'.join(s[:-1])
				nd[k] = float(d[prefix+'-ThemePercFix']) - float(d[prefix+'-GoalPercFix'])

			retframe.addData(nd)	

		return retframe
		

	def _tabulize(self,tree,colnames):	
		retval = []	
		if colnames != []:
			colname = colnames[0]
			for key in tree.keys():
				rest = self._tabulize(tree[key],colnames[1:])	
				if not isinstance(rest[0],list):
					retval.append([key]+rest)
				else:
					for i in rest:
						retval.append([key]+i)
			return retval
		else:
			for k in self.AOICats:
				try:
					val = tree[k]/float(tree['Total'])*100
				except ZeroDivisionError:
					val = 0.00
				retval.append(val)	
			return retval	

	def compute_fixations(self,frame,keys):
		retdict = dict()
		if keys == []:
			for t in self.Data.uniqField('TimePeriod'):
				if not t or t in ['Fixation','Ignore']:
					continue
				f = frame.filter(('TimePeriod',t))
				ddict = dict()
				for a in self.AOICats:
					ddict[a] = 0
				ddict['Total'] = 0
				for d in f:
					print d
					ddict[d['AOICat']] += 1	
					ddict['Total'] += 1	
				retdict[t] = ddict
			return retdict
		else:
			key = keys[0]	
			vals = self.Data.uniqField(key)
			for val in vals:
				f = frame.filter((key,val))
				retdict[val] = self.compute_fixations(f,keys[1:])
			return retdict
		
class Session():
	"""A session of the experiment."""
	def __init__(self, experiment,session_file_name):
		"""Initialize a Session instance.
		
			Args:
			experiment -- the owner Experiment instance.
			session_file_name -- name of the session file.
		
		"""
		self._ID = session_file_name[:session_file_name.index('.')]
 		sys.stderr.write('\nReading session '+self.ID+'...')	
		self._Exp = experiment
		self._Group = ""
		self._Participant = ""
		self._Trials = []
		"""Perform various operations on gazedata if needed. Need is checked by whether there are already csv files in the RawPath"""
		if not self.Exp._data_clean:
			self._proc_gazedata()

		self._DataFile = self.Exp.RawPath+self.ID + '.csv'  

		self._parse_info_file(session_file_name,self._Exp._Level)

# 		sys.stderr.write('\t[OK]') # with '+str(len(self.Trials))+' trials\n')	
 		sys.stderr.write('\t[OK] with '+str(len(self.Trials))+' trials\n')	

	@property	
	def ID(self):
		"""ID of the session as appears on the output file (.gazedata and .txt)"""
		return self._ID
	@ID.setter
	def ID(self,value):
		self._ID = value
	
	@property	
	def Exp(self):
		"""The owner Experiment instance for this session"""
		return self._Exp
	@Exp.setter
	def Exp(self,value):
		self._Exp = value

	@property	
	def Group(self):
		"""Group of the session"""
		return self._Group
	@Group.setter
	def Group(self,value):
		self._Group = value

	@property	
	def Participant(self):
		"""The participant ID for the session"""
		return self._Participant
	@Participant.setter
	def Participant(self,value):
		self._Participant = value

	@property	
	def Trials(self):
		"""The list of Trial instances of the session"""
		return self._Trials
	@Trials.setter
	def Trials(self,value):
		self._Trials = value

	@property	
	def DataFile(self):
		"""The data of the Session kept as a .csv file"""
		return self._DataFile
	@DataFile.setter
	def DataFile(self,value):
		self._DataFile = value

	def _parse_info_file(self,file_name,lev):
		"""Parse the session file with '.text' extension and set certain class attributes."""	
		lines = open(self.Exp.RawPath+file_name,'r').readlines()	

		factors = {'Condition':'', self.Exp.TrialOnsetLabel:0,self.Exp.TrialOffsetLabel:0}
		for i in self.Exp._Images:
			factors[i]=''

		pattern= re.compile('(.*): (.*)')

		line = lines.pop(0)
		while line.find('Header End') ==-1:
			m = pattern.match(line.strip())
			if m:
				key = m.group(1)
				if key == 'Experiment':
					self.Group=m.group(2).split('-')[0][-1:] #TODO: This needs to be standardized
				elif key == 'Subject':
					self.Participant=m.group(2)
			line = lines.pop(0)

		level=0

		while True:
			try:
				line = lines.pop(0)
				if line.find('LogFrame Start') !=-1 and level==lev:
					factors = {'Condition':'', self.Exp.TrialOnsetLabel:0,self.Exp.TrialOffsetLabel:0}
					for i in self.Exp._Images:
						factors[i]=''
				m = pattern.match(line.strip())

				if m:
					key = m.group(1)
					if key in factors.keys():
						try:
							factors[key] = int(m.group(2).replace('.',''))
						except:
							factors[key] = m.group(2).replace('.','')
					elif key=='Level':
						level=int(m.group(2))

				if line.find('LogFrame End') >-1 and level == lev:
					self.Trials.append(Trial(factors,self))	
			except 	IndexError:
				break					

	def _proc_gazedata(self):	
		"""
		Perform the following operations on gazedata:
		
		-construct a Frame from gazedata
		-insert Item and Group fields and set them
		-correct various errors TODO: will be removed in future versions 	
		-write the data to a csv file ignoring non-required information (which is determined by the RequiredInfo attribute of the owner Experiment instance).
		"""
		sys.stderr.write('fixing gazedata errors...')
		"""Read .gazedata and construct a Frame instance from it"""
		gazedatafile = open(self.Exp.RawPath+self.ID+'.gazedata','r') 
		rows = [x.strip().split('\t') for x in gazedatafile] # construct a list of rows from the lines of the (tab separated) .gazedata file 
		header = map(lambda x:re.sub('Subject','Participant',x),rows[0])
		dataframe = Frame(header,rows=rows[1:])

		"""Insert 'Item', 'Group', 'TimePeriodSpa' and 'AgeGroup' fields to dataframe """
		dataframe.header.insert(dataframe.header.index('Condition'),'Item')
		dataframe.header.insert(dataframe.header.index('TrialId'),'Group')
		dataframe.header.insert(dataframe.header.index('TrialId'),'Session')
		dataframe.header.insert(dataframe.header.index('Group'),'AgeGroup')
		dataframe.header.insert(dataframe.header.index('TimePeriod'),'TimePeriodSpa')


		for d in dataframe:
			"""Set group information"""
			d['Group'] = self.Group
			"""Set session information"""
			d['Session'] = self.ID
			"""Fix some errors and inconsistencies"""
			self._fix_errors(d)
			"""Set the 'Item' field"""
			aoinames = ['AOI'+str(x) for x in range(1,self.Exp.NumOfAOIs+1)]
			if 'abl' in self._Exp._Conditions:
				d['Item'] = '-'.join(sorted([d[x][5:-6].replace('2','') for x in aoinames]))
			else:
				d['Item'] = '-'.join(sorted([d[x][:-4].replace('2','') for x in aoinames]))

		"""Write the data to a .csv file, but only the required information"""
		dataframe.header = self.Exp.RequiredInfo
		dataframe.printFrame(self.Exp.RawPath+self.ID+'.csv')

	def _fix_errors(self,data):
		"""Fix some errors and inconsistencies in gazedata."""

		"""Set AOICat to 'Other' when AOIStimulus is 'Other'"""
		if data['AOIStimulus'] == 'other' or data['AOIStimulus'] == 'Other':
			data['AOICat'] = 'Other'

		#Change AOICat from Targ, Comp, Dist to Agent, Patient, Topic
		if data['AOICat'] in ['Dist','dist']:
			data['AOICat'] = 'Topic'
		if data['Condition'] == 'Accusative':
			if data['AOICat'] in ['Targ','targ']:
				data['AOICat'] = 'Agent'
			elif data['AOICat'] in ['Comp','comp']:
				data['AOICat'] = 'Patient'
		elif data['Condition'] == 'Nominative':
			if data['AOICat'] in ['Targ','targ']:
				data['AOICat'] = 'Patient'
			elif data['AOICat'] in ['Comp','comp']:
				data['AOICat'] = 'Agent'
		#ACCUSATIVE
			
		"""Change AOICat from target, dist, topic to Theme, Goal, Topic
		if data['AOICat'] == 'topic':
			data['AOICat'] = 'Topic'
		if data['Condition'] == 'Accusative':
			if data['AOICat'] == 'target':
				data['AOICat'] = 'Goal'
			elif data['AOICat'] == 'dist':
				data['AOICat'] = 'Theme'
		elif data['Condition'] == 'Dative':
			if data['AOICat'] == 'target':
				data['AOICat'] = 'Theme'
			elif data['AOICat'] == 'dist':
				data['AOICat'] = 'Goal'
		""" #DATIVE

		"""Change AOICat from targ, to Targ
		if data['AOICat']=='targ':
			data['AOICat']='Targ'
		""" #ACCUSATIVE
		
		"""Correct inconsistencies in item names
		aoinames = ['AOI'+str(x) for x in range(1,self.Exp.NumOfAOIs+1)]
		aois = [data['AOI'+str(x)] for x in range(1,self.Exp.NumOfAOIs+1)]
		for name in aoinames:
			if data[name]=='oyuncak.bmp' and 'adam.bmp' in aois:
				data[name]='oyuncakayi.bmp'
				if data['AOIStimulus']=='oyuncak.bmp':
					data['AOIStimulus'] ='oyuncakayi.bmp'
			elif data[name]=='oyuncak.bmp' and 'kiz.bmp' in aois:
				data[name]='oyuncakbebek.bmp'
				if data['AOIStimulus']=='oyuncak.bmp':
					data['AOIStimulus'] ='oyuncakbebek.bmp'
			elif data[name]=='cocuk2.bmp':
				data[name]='cocuk.bmp'
				if data['AOIStimulus']=='cocuk2.bmp':
					data['AOIStimulus'] ='cocuk.bmp'
			elif data[name]=='kadin2.bmp':
				data[name]='kadin.bmp'
				if data['AOIStimulus']=='kadin2.bmp':
					data['AOIStimulus'] ='kadin.bmp'
			elif data[name]=='bebek.bmp' and 'kiz.bmp' in aois:
				data[name]='oyuncakbebek.bmp'
				if data['AOIStimulus']=='bebek.bmp':
					data['AOIStimulus'] ='oyuncakbebek.bmp'
			if data[name+'Cat']=='targ':
				data[name+'Cat']='Targ'
			"""#ACCUSATIVE

class Trial(object):
	"""Trial in a session."""
	def __init__(self,factors, session):
		"""Initialize a Trial instance
		
			Args:

			factors -- a dictionary containing the info 'Condition',TrialOnsetLabel,TrialOffsetLabel
			session -- the owner Session instance
		"""
		
		

		attrlist=['Condition',session.Exp.TrialOnsetLabel,session.Exp.TrialOffsetLabel]
		for attr in attrlist:
			try:
				exec("self."+attr.replace('.','')+'="'+factors[attr]+'"')
			except TypeError:
				exec("self."+attr.replace('.','')+'= int('+ str(factors[attr]) +')')



		self.Session = session 
		
		if 'abl' in self.Session._Exp._Conditions:
			self.Item = "-".join(sorted([factors[x][5:-5] for x in self.Session.Exp._Images]))
		else:
			self.Item = "-".join(sorted([factors[x][:-3] for x in self.Session.Exp._Images]))
	 	"""The following block is needed to fix some inconsistencies in image names, and will be deleted in the future
"""
		self.Item=self.Item.replace('2','')
		"""
		if self.Item == 'adam-cocuk-oyuncak':
			self.Item = 'adam-cocuk-oyuncakayi'
		elif self.Item == 'bebek-kadin-kiz':
			self.Item = 'kadin-kiz-oyuncakbebek'
		elif self.Item == 'kadin-kiz-oyuncak':
			self.Item = 'kadin-kiz-oyuncakbebek'
		"""
		
		self.Condition = factors['Condition']
		self.TimeWindows = []
		self.Onset = int(factors[self.Session.Exp.TrialOnsetLabel])
		self.Offset = int(factors[self.Session.Exp.TrialOffsetLabel])
		self.Length = self.Offset - self.Onset
		print "Onset: ",self.Onset," | Offset: ",self.Offset," | Duration: ",self.Length	
		print self.Session.ID+' -- '+self.Item + ' now reading...'
		self._Data = Frame(fromfile=self.Session.DataFile).filter(('Item',self.Item))
		print str(len(self._Data.data)) + ' read\n'
		self.Condition = self._Data.data[0]['Condition']#this is a patch for the dom experiment, where conditions are wrong in the e-prime text files
		item_map ={'agac-kurbaga-kus':'GenPoss', 'ari-bocek-inek':'GenORel', 'balik-zebra-zurafa':'GenPoss', 'canta-ogretmen-ordek':'GenORel', 'esek-kuzu-mantar':'GenORel', 'balon-cocuk-makas':'GenPoss', 'bocek-gemi-polis':'GenORel', 'buz-kemik-penguen':'GenPoss', 'ciftci-kadin-yumurta':'GenORel', 'hemsire-hirsiz-mum':'GenPoss'}
		for data in self._Data:
			if data['Item'] in item_map.keys():
				data['Condition'] = item_map[data['Item']]

		self.Accurate = bool(int(self._Data.data[0]['ClickAcc']))

		"""Put time window information as needed"""
 		if self.isCritical():
 			if self.Session.Exp.TWInfo:
 				self._insert_tws()
 			if self.Session.Exp._SpaInterval:
 				self._insert_tw_series(self.Session.Exp._SpaInterval)


	@property
	def Data(self):
		"""Data of the trial (Frame)"""
		return self._Data
	@Data.setter
	def Data(self,value):
		self._Data = value
	@Data.deleter
	def Data(self):
		del self._Data

	def _insert_tws(self):
		"""Insert time window information into the data of the Trial""" 
		item_info = self.Session.Exp.TWInfo
		newdata = Frame(self.Data.header) #constructing a new frame and accumulating data into that is less time-costly than removing unnecessary data from the original data -- so do not revise this code
		for d in self.Data:
			rttime = int(d['RTTime'])
			if rttime < self.Onset:
				continue
			elif rttime > self.Offset:
				break
			time_info = item_info[d['Item']][d['Condition']]
			d['TimePeriod'] = self._get_tw(rttime,time_info)
			newdata.addData(d)
		del self.Data
		self.Data = newdata
		print str(len(self.Data.data)) + ' after tw insertion'

	def _get_tw(self,time,timeinfo):
		for k in timeinfo.keys():		
			os = self.Onset + int(timeinfo[k]['Onset'])
			ofs = self.Onset + int(timeinfo[k]['Offset'])
			if time >= os and time <= ofs:
				return k
		
	def _insert_tw_series(self,interval):
		"""
		Add a series of time windows to the trial
		
		Args:
		interval -- step length of tw series
		"""
				
		num_of_tws = self.Length/interval + 1
		newdata = Frame(self.Data.header) #constructing a new frame and accumulating data into that is less time-costly than removing unnecessary data from the original data -- so do not revise this code
		for d in self.Data:
			rttime = int(d['RTTime'])
			if rttime < self.Onset:
				continue
			else:
				tw = (rttime - self.Onset)/100 + 1
				if tw <= num_of_tws:
					d['TimePeriodSpa'] = str(tw)
					newdata.addData(d)
				else:
					break

		del self.Data
		self.Data = newdata

	def isCritical(self):
		"""Whether the trial is of a critical item"""
		return self.Condition in self.Session.Exp.Conditions# and self.Session.Exp._ItemFilter(self.Item)
	
	def get_data(self):
		"""Return a copy of the data of the trial as a Frame instance"""
		return copy.deepcopy(self.Data) #as we have a deep copy, altering the data of the trial does not alter the session data

class SpaPlot():
	"""Spaghetti plot for an eye-tracking experiment"""
	
	def __init__(self,experiment,foreach=None):
		sys.stderr.write('\nCalculating spaghetti plots...')
		self.Exp = experiment
		data = self.Exp.Data
		self.Sessions = self.Exp.Sessions 
		self.Conditions = self.Exp.Conditions 
		tr = None
	

		"""Split the data per condition and store in a dict of frames"""
		self.Data = {}
		for cond in self.Conditions:
			self.Data[cond] = data.filter(('Condition',cond))

		del data #free some memory
		
		"""Generate reports:
			-general
			-per item
			-per participant
		"""

		wb_gen = xlwt.Workbook()
		wb_item = xlwt.Workbook()
		wb_part = xlwt.Workbook()

		# General
		gen_rows = []
		for cond in self.Conditions:
			gen_rows.extend([[''],[cond],['']])
			gen_frame = self._compute_fixations(self.Data[cond]).get_prop()
			gen_rows.extend(gen_frame.get_rows())

		utils.writeXLsheet(wb_gen,'All',gen_rows)
		wb_gen.save(self.Exp.Name+'-spaghetti-all.xls')
		wb_gen = None

		# per item	
		for item in self.Data[cond].uniqField('Item'):
			item_rows = []
			for cond in self.Conditions:
				item_rows.extend([[''],[cond],['']])		
				item_frame = self._compute_fixations(self.Data[cond].filter(('Item',item))).get_prop()
				item_rows.extend(item_frame.get_rows())
		
			utils.writeXLsheet(wb_item,item,item_rows)

		wb_item.save(self.Exp.Name+'-spaghetti-per-item.xls')
		wb_item = None

		# per participant
	
		for part in self.Data[cond].uniqField('Participant'):
			part_rows = []
			for cond in self.Conditions:
				part_rows.extend([[''],[cond],['']])
				part_frame = self._compute_fixations(self.Data[cond].filter(('Participant',part))).get_prop()
				part_rows.extend(part_frame.get_rows())
			
			utils.writeXLsheet(wb_part,part,part_rows)

		wb_part.save(self.Exp.Name+'-spaghetti-per-participant.xls')

		sys.stderr.write('\t[OK]\n\n')

	def _compute_fixations(self,dataframe):
		"""Return fixation information for the dataframe"""
		retval =  Frame(['AOICat']+[str(i) for i in range(1,250)])
	
		for a in self.Exp.AOICats:
			data = {'AOICat':a}
			for tw in [str(i) for i in range(1,250)]:
				data[tw]=0
			retval.addData(data)	

		for d in dataframe:
			if int(d['TimePeriodSpa']) < 250:
				retval.getData('AOICat',d['AOICat'])[d['TimePeriodSpa']] += 1
			else:
				break

		return retval



# 	def _collect_data(self):
# 		"""Insert tw series of the step length self.Interval to the trials of the session.
# 		Collect  and return the resulting data"""
# 		data_accum = Frame()
# 		for s in self.Exp.Sessions:
# 			trials = s.Trials	
# 			for trial in trials:
# 				"""add tw series to the trial and put it in the accumulator"""
# 				data_accum.append(trial.add_tw_series(100,self.NumTWs))
# 		return data_accum				

class UnrecognizedValue(exceptions.Exception):
	def __init__(self,param,value):
		self.param = param
		self.value = value
	
	def __str__(self): 
		print "\t'%s' is not recognized as a value for parameter '%s'."%(self.value,self.param)
