#!/bin/bash

tar -zcvf ti`date +%F`.tgz `echo $1'[[:digit:]].csv'`
