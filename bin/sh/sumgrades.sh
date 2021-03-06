#!/bin/bash

grades=$(egrep '; >' $1 | cut -d ' ' -f 3)

sum=0
for x in $grades;
do
	sum=$(echo "$sum + $x" | bc -l)
done

tmp=$(echo $1 | sed -nr 's/mt-01-(.*)\.lisp/\1/p')

echo -e "$tmp\t$sum"
