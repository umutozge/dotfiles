#!/usr/bin/env python
from fixpy import *
import sys
import os
from datetime import datetime


date = str(datetime.today().date())
root_dir = os.environ['HOME']+'/dom/'+date+'-DOM-TrimmedData'
experiment = Experiment(root_dir='.',\
conditions = ['Acc1','Acc2','Zero1','Zero2'],\
num_aois=2,\
timewindow_info='twi_dom.csv',\
aoicats='NP1,NP2,Other',\
spa_plot=100,\
images='UpLeftImage,LowCenterImage',\
)
