#!/usr/bin/env python
from fixpy import *
import sys
import os
from datetime import datetime

## ITEM FILTERS ##
# for low relatedness use this
low_rel = lambda x: x in 'civciv-kurt-misir,aslan-maymun-muz,kadin-kiz-oyuncakbebek,at-cocuk-top,findik-kurt-sincap'.split(',')
# for high relatedness use this
high_rel = lambda x: x in 'havuc-tavsan-tilki,adam-cocuk-oyuncakayi,avci-ayi-bal,bebek-dondurma-kopek,fare-kedi-peynir'.split(',')
# for very high  relatedness use this
very_high_rel = lambda x: x in 'havuc-tavsan-tilki,fare-kedi-peynir'.split(',')

date = str(datetime.today().date())
# root_dir = os.environ['HOME']+'/kc/'+date+'-KU-TrimmedData'
root_dir = '.'
experiment = Experiment(\
#experiment = Experiment(timewindow_info=sys.argv[1],\
conditions = 'Accusative,Nominative',\
root_dir=root_dir,\
spa_plot=100,\
aoicats="comp,dist,targ",\
level=2,\
trial_onset_label="QuadSlide.OnsetTime",\
trial_offset_label="AnimSlide.OnsetTime",\
# item_filter = very_high_rel,\
images='UpLeftImage,UpRightImage,LowCenterImage')


