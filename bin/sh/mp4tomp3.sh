#!/bin/bash

args=("$@")

for ((i=0;i<$#;i++)){
	ROOT=`echo ${args[$i]} | sed -e 's/\([^.][^.]*\).mp4/\1/'`
	 avconv -i ${args[$i]} -vn -f mp3 $ROOT.mp3
}
echo 'Done!\n'
exit 0
