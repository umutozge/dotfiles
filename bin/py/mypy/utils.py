import math
import sys
import xlwt

def isString(text):
	return str(type(text)) == "<type 'str'>"

def isInt(text):
	return str(type(text)) == "<type 'int'>"

def isFloat(text):
	return str(type(text)) == "<type 'float'>"

def isFile(text):
	return str(type(text)) == "<type 'file'>"


def trunc2(number,dec_places):
	if isinstance(number,float):
		number = str(number)
	try:
		newnumber = None
		dec_ind = number.find('.')
		rnd_ind = dec_ind+int(dec_places)
# 		penult = number[rnd_ind+1]
# 		if int(penult) >= 5:
# 			newnumber = number[:rnd_ind] + str(int(number[rnd_ind])+1)
# 		else:
		newnumber = number[:rnd_ind+1]
		return newnumber
	except IndexError:
		return number	
	

def strToInt(string):
	if string=="":
		return 0
	else:
		return int(string)

def strToFloat(string):
	if string=="":
		return 0
	else:
		return float(string)
def listToStr(list):
	accum=""
	for i in list:
		accum +=  str(i)
	return accum

def sumList(list):
	sum= 0
	for i in list:
		sum = sum+i
	return sum 

def mean(list):
	if isinstance(list[0],int):
		sum = 0.0
		for l in list:
			sum = sum + float(l)
		return sum/float(len(list))
	elif isinstance(list[0],str):
		sum = 0.0
		for l in list:
			sum = sum + strToFloat(l)
		return sum/float(len(list))
	elif isinstance(list[0],float):
		sum = 0.0
		for l in list:
			sum = sum + l
		return sum/float(len(list))

def sdev(lst):
	if len(lst) <= 1:
		return 0.0
	mn = mean(lst)
	n = len(lst) - 1
	sum = 0
	for l in lst:
		sum = sum + (l-mn)**2
	return math.sqrt(sum/n)
	
def writeXLsheet(workbook,sheetname,rows):
		ws = workbook.add_sheet(sheetname)
		for ri, row in enumerate(rows):
			for ci, val in enumerate(row):
				ws.write(ri,ci,val)

def xproduct(list1,list2,cross=lambda x,y:str(x)+'-'+str(y)):
	newlist = []
	for x in list1:
		for y in list2:
			newlist.append(cross(x,y))
	return newlist

