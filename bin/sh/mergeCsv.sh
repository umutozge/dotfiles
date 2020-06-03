#!/bin/bash

function func_zip {
	zip `echo $1 | sed 's/^.*$/&\.zip/g'`  $1
}
function func_bzip2 {
	bzip2 $1
}
function func_bunzip2 {
	bunzip2 $1
}
function func_tar {
	tar -zcvf `echo $1 | sed 's/^.*$/&\.tgz/g'`  $1
}


args=("$@")
len=${#args[@]}

head -n 1 ${args[1]} > ${args[0]}

for ((i=1;i<$len;i++))
do 
	tail -q -n +2 ${args[$i]} >> ${args[0]}	
done

