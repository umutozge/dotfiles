#!/usr/bin/python

from mypy.datatools import Frame, Csv
import subprocess
import re








IDS={ "3-studi-sd":("Single room","Double room for single use","Studentenhotel","56.00"), "5-munchner":("Single room","Single room","Muenchnerhof","55.00"), "2-studi-sp":("Single room","Single room with private bath","Studentenhotel","49.00"), "1-studi-ss":("Single room (shared bath.)","Single room (shared bath.)","Studentenhotel","35.50"), "6-sauter":("Single room","Single room","Sautter","90.00"), "7-astoria":("Single room","Single room","Astoria","44.00"), "4-studi-d":("Double room","Double room","Studentenhotel","63.00")}


def getHotel(shortname):
	return IDS[shortname][2]
def getDesc(shortname):
	return IDS[shortname][0]
def getLongDesc(shortname):
	return IDS[shortname][1]
def getPrice(shortname):
	return IDS[shortname][3]


bs = Csv("bookings-final.csv").getRows()
bookings=Frame(bs[0],bs[1:])


for b in bookings.iterFrame():
	key = b["Room"]
	hotel = getHotel(key)
	desc = getDesc(key)
	longdesc = getLongDesc(key)
	price = getPrice(key)
	name = b["Name"]
	surname= b["Surname"]
	checkin= b["Checkin"]
	checkout= b["Checkout"]
	notes = b["Notes"]
	email= b["Email"]
	try:
		f = open(hotel+".csv",'r')
		f.close()
	except IOError:
		w = open(hotel+".csv",'a')
		w.write("Surname,Name,Email,Room,Check-in,Check-out,Notes\n")
		w.close()
	w = open(hotel+".csv","a")
	w.write("%s,%s,%s,%s,%s.05.12,%s.05.12,%s\n"%(surname,name,email,longdesc,checkin,checkout,notes))	
	w.close()

# 	subject="WAFL 8: Hotel booking confirmation"
# 	body="Dear %s %s,\n\nWe would like to confirm your reservation:\n\n%s in %s at %s Euro from %s to %s May.\n\nWe are looking forward to seeing you in Stuttgart.\n\nRegards,\nThe OC\n\nPS: 10 Euro student discount is possible upon producing a valid student ID."% (name,surname,desc,hotel,price,checkin,checkout)
# 	args = ["mutt"]
# 	out=open("body","w")
# 	out.write(body)	
# 	out.close()
# 	args.extend(["-s"+subject,"-ibody"]+["--",email])	
#  	subprocess.call(args)
# 
