#!/bin/bash

fn=$1

echo Calculating fixations for $1...
fixation.py -o $1-SubjItemCondTw.csv accurate.csv
echo SubjItemCondTw Done!
fixation.py -f Subject,Condition -o $1-SubjCondTw.csv accurate.csv
echo SubjCondTw Done!
fixation.py -f Item,Condition -o $1-ItemCondTw.csv accurate.csv
echo ItemCondTw Done!

echo Now eliminating fields...

elimField.py -e Condition,TimePeriod -p Item -o $1-Item-ANOVA.csv $1-ItemCondTw.csv
elimField.py -e Condition,TimePeriod -p Subject -o $1-Subj-ANOVA.csv $1-SubjCondTw.csv

echo Collecting the results to an excel file...

procxl.py -r $1- $1-SubjItemCondTw.csv $1-SubjCondTw.csv $1-ItemCondTw.csv $1-Subj-ANOVA.csv $1-Item-ANOVA.csv 

echo Done!
