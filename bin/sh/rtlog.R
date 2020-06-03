#!/usr/bin/Rscript

#library(dplyr)

args = commandArgs(trailingOnly=T)

if (!is.na(args[1])) {
	threshold <- as.integer(args[1])
}else {
	threshold = 0
}

data <- read.table("~/res/log", header=T)

print("Average daily work time:")
mean(data$Time)/60
