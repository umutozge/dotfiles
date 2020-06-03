#!/bin/bash

size=(`pdfinfo $1|grep 'Page size'| sed -e 's/.*: \+\([0-9]\+\) x \([0-9]\+\).*/\1 \2/'`)
width=`echo "${size[0]} * 0.0138" | bc` 
height=`echo "${size[1]} * 0.0138" | bc` 
pdftops -level3 $1 - | psbook | psnup -2 -W${width}in -H${height}in | ps2pdf - kitapcik-$1
