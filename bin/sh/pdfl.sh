#!/bin/bash

pdflatex $1

ROOT=`echo $1 | sed -e 's/\(\w\w*\).tex/\1/g'`
pdftotext -layout -nopgbrk $ROOT.pdf 

TOS=$ROOT.txt

sed -i -e 's/ﬁ/fi/g' $TOS
sed -i -e 's/ﬂ/fl/g' $TOS


w3m +$2 $TOS
exit 0
