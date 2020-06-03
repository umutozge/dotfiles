#!/bin/bash

args=("$@")

for ((i=0;i<$#;i++)){
	ROOT=`echo ${args[$i]} | sed -e 's/\([^.][^.]*\).jpg/\1/'`
	convert ${args[$i]} $ROOT.pdf
}
echo 'Done!\n'
exit 0
