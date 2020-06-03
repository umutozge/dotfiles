#!/bin/bash

args=("$@")

for ((i=0;i < $#;i++)){
	convert -quality 75 ${args[$i]} dummy.jpg
	mv dummy.jpg ${args[$i]}
}
