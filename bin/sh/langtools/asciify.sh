#!/bin/bash

if [ -p /dev/stdin ];
then
	read input
	stdin=1
else
	stdin=0
	input=$1
fi


declare -A chars

chars[Ç]=C
chars[İ]=I
chars[Ğ]=G
chars[Ö]=O
chars[Ş]=S
chars[Ü]=U
chars[ç]=c
chars[ı]=i
chars[ğ]=g
chars[ö]=o
chars[ş]=s
chars[ü]=u

sedcmd="sed -r 's/a/a/"

for c in ${!chars[@]}
do
	#hextr=`echo -n $c | hexdump -x | sed -nr 's/0+ +([^ ]+) .*/\1/gp' |sed -nr 's/(..)(..)/\\\\x\1\\\\x\2/gp'`
	#hexen=`echo -n ${chars[$c]} | hexdump -x | sed -nr 's/0+ +([^ ]+) .*/\1/gp' |sed -nr 's/(..)(..)/\\\\x\1\\\\x\2/gp'`
	#sedcmd=`echo -n $sedcmd "; s/$hextr/$hexen/"`
	sedcmd=`echo $sedcmd "; s/$c/${chars[$c]}/g"`
done

sedcmd=`echo $sedcmd "'"`


if [ $stdin -eq 1 ];
then
	echo "echo $input | $sedcmd" | sh
else
	echo -e "$sedcmd $input" | sh
fi
