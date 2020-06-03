#!/usr/bin/env python
from fixpy import *
import sys
import os
from datetime import datetime

## ITEM FILTERS ##
# for low relatedness use this
#low_rel = lambda x: x in 'civciv-kurt-misir,aslan-maymun-muz,kadin-kiz-oyuncakbebek,at-cocuk-top,findik-kurt-sincap'.split(',')
# for high relatedness use this
#high_rel = lambda x: x in 'havuc-tavsan-tilki,adam-cocuk-oyuncakayi,avci-ayi-bal,bebek-dondurma-kopek,fare-kedi-peynir'.split(',')
# for very high  relatedness use this
#very_high_rel = lambda x: x in 'havuc-tavsan-tilki,fare-kedi-peynir'.split(',')


# one human

onehuman = lambda x: x in 'havuc-sihirbaz-tavsan,ciftci-inek-ot,fare-palyaco-peynir,fotografci-kus-simit,kemik-kopek-veteriner,kedi-ressam-sut'.split(',')

# two human

twohuman = lambda x: x in 'disci-elbise-kiz,bebek-hemsire-mama,kiz-ogretmen-oyuncakbebek,doktor-hasta-ilac,araba-cocuk-mudur,berber-cocuk-kazak'.split(',')


date = str(datetime.today().date())
# root_dir = os.environ['HOME']+'/kc/'+date+'-KU-TrimmedData'
root_dir = '.'
experiment = Experiment(\
#experiment = Experiment(timewindow_info=sys.argv[1],\
conditions = 'Accusative,Dative',\
root_dir=root_dir,\
aoicats="Topic,Goal,Theme,Other",\
spa_plot=100,\
item_filter = onehuman,\
images='UpLeftImage,UpRightImage,LowCenterImage')
