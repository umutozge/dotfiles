#!/bin/bash

grades=$(egrep '; >' $1 | cut -d ' ' -f 3)

sum=0
for x in $grades;
do
	sum=$(echo "$sum + $x" | bc -l)
done

sed_str="s/$2(.*)\.lisp/\1/p"

tmp=$(echo $1 | sed -nr $sed_str)

echo -e "$tmp\t$sum"
