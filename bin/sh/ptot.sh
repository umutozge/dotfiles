#!/bin/bash

ROOT=`echo $1 | sed -ne 's/\([a-z\-]\+\).pdf/\1/gp'`
echo $ROOT
pdftotext -layout -nopgbrk $ROOT.pdf 

sed -i -e 's/ﬁ/fi/g' $ROOT.txt
sed -i -e 's/ﬂ/fl/g' $ROOT.txt

exit 0
