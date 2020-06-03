#!/bin/bash

filename=`echo $1 | sed  's|.*/\([^/]\+\)|\1|'`
scp -q -c blowfish  oezge@141.58.164.102:~/$1 $filename 

