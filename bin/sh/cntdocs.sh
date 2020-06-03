#!/bin/bash
xmllint --format $1|grep -c '<d>' 
