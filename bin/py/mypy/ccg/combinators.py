#!/usr/bin/env python

from curses.textpad  import * 
from curses import wrapper
import locale
import sys

A = lambda x: lambda y: x(y)
T = lambda x: lambda f: f(x)
B = lambda f: lambda g: lambda x: f(g(x))


#lexicon

mary = "m'"
john = "j'"
loves = lambda x: lambda y: "loves'"+x+y

def stop():
	stdscr.clear()
	stdscr.refresh()
	curses.nocbreak()
	curses.echo()
	curses.endwin()


def start(stdscr):
	curses.echo()
	stdscr.addstr(10,0,'Enter a term to resolve, or "q" for quit',curses.A_BOLD)
	resp = stdscr.getstr(11,0)
	stdscr.refresh()
	stdscr.addstr(12,0,resp)
	stdscr.refresh()


if __name__ == "__main__":

	locale.setlocale(locale.LC_ALL,"")

	wrapper(start)	



#	stdscr = curses.initscr()
#	stdscr.keypad(1)
#	curses.noecho()
	#curses.cbreak()
	
# 	try:	
# 		stdscr.addstr(0,20,'Enter a term to resolve, or "q" for quit',curses.A_BOLD)
# #		inwin = curses.newwin(30, 30, 0, 20)
# 		#rectangle(inwin, 0, 30, 0, 20)
# 	
# 		#tb = Textbox(inwin)
# 		#instr = tb.edit()
# 
# 		#stdscr.addstr(0,50,instr)	
# 
# 	except AttributeError as ae:
# 		stop()
# 		print str(ae)
# 	except:
# 		stop()
# 		print 'Unknown error'

#	if stdscr.getch() == ord('q'):

