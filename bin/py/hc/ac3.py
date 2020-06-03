#!/usr/bin/python3

#Arc consistency for 3D Scene analysis
#Please see Steedman (1995) for the problem.

# Umut Ozge
# tumuum@gmail.com
# May 19, 2016


"""
How to represent input figures:

We need a general description of a  2-D line drawing.

Junction: <I,T,L>, where I is the index of the junction, a unique identifier.
						 T is the type of the junction --
						 a string from {'a'rrow, 'e'll, 'y', 't'ee}
						 N is a tuple that keeps the indices of neighbors,
						 according to the convention of ex. 5.3 from Steedman;
						 namely when the arms of a junction is labeled starting
						 from 1 according to that convention, the tuple tells
						 which junction (by index of it) stands on the other end
						 of the arm.

Figure: a set of junctions.

	Example 1:

		1----2
		|	/
		|  /
	    | /
		3

	[1, 'e', (2,3)]
	
	[2, 'e', (3,1)]

	[3, 'e', (1,2)]


	Example 2 -- Figure 5.10:

			1
		   /|\
		  / | \
	     /  |  \
		/   |   \
	   /    |    \
	 4 \    |    / 2
	    \   |   /
	     \  |  /
	      \ | /
	       \|/
			3	

	[[1,'a',(2,3,4)],	
	 [2,,'e',(3,1)],
	 [3,'a',(4,1,2)],
	 [4,'e',(1,3)]]


This is how the input is represented. The class Figure defined below adds the
label information to this representation.


"""   

import sys

class Figure:

	def __init__(self, junctionset):

		#keep the junctions of a figure in dict for easy access
		#the dict self.junctions will look like
		# {1: <some_junction_instance>, 2: <some_junction_instance>...}
		#
		self.junctions = {} 
		for j in junctionset:
			#
			#create Junction and add it to the junction list
			#Junction requires three pieces of info to get initialized
			#	1. index of the junction
			#	2. type of the junction
			#   3. connectivity of the junction, list of neighbouring junction indeces
			#
			self.junctions[j[0]] = Junction(j[0],j[1],j[2])

	def get_junction(self,index):
		try:
			return self.junctions[index]
		except KeyError:
			sys.stderr.write('No junction with index '+str(index))	
			sys.exit(1)

	def get_arcs(self):
		#extract a queue of arcs from the connectivity of junctions
		arc_list = []
		for j in self.junctions.values():
			for i in j.neighbors:
				arc_list.append((j.index,i))
		arc_list.sort()
		return arc_list
	

	def check_consistency(self,arc):
		ind1, ind2 = arc
		junc1, junc2 = self.get_junction(ind1), self.get_junction(ind2)

		# keep track of if you removed something
		sth_removed = False
		
		# put a stopper at the end of the label list -- for loop is not good as
		# you may remove things from the label list

		junc1.labelset.append('STOP')
		current_label = junc1.labelset.pop(0)

		while current_label != 'STOP':
			consistent = False
			for label2 in junc2.labelset:
				a, b = label2[ind1], current_label[ind2] 
				if a == b and len(a) + len(b) == 2:
					consistent = True
					break
				elif len(a) + len(b) == 5:
					consistent = True
					break

			if consistent:
				#if current label is consistent put it back
				junc1.labelset.append(current_label)	
			else:
				sth_removed = True
			current_label = junc1.labelset.pop(0)		

		return sth_removed


	def filter(self):
		#form the arc queue
		arq = self.get_arcs()
		#loop untill no arc left on the queue
		while arq:
			#get current arc
			ca  = arq.pop(0)
			removed = self.check_consistency(ca)
			if removed:
				for a in self.get_arcs():
					if a[1] == ca[0] and a not in arq:
						arq.append(a)

class Junction:
	
	#the label types on p. 181
	A1 = ('A1',('out','+','in'))
	A2 = ('A2',('+','-','+'))
	A3 = ('A3',('-','+','-'))

	L1 = ('L1',('out','in'))
	L2 = ('L2',('in','out'))
	L3 = ('L3',('in','+'))
	L4 = ('L4',('+','out'))
	L5 = ('L5',('-','in'))
	L6 = ('L6',('out','-'))

	T1 = ('T1',('out','in','+'))
	T2 = ('T2',('out','in','-'))
	T3 = ('T3',('out','in','out'))
	T4 = ('T4',('out','in','in'))

	Y1 = ('Y1',('in','out','-'))
	Y2 = ('Y2',('out','-','in'))
	Y3 = ('Y3',('-','in','out'))
	Y4 = ('Y4',('-','-','-'))
	Y5 = ('Y5',('+','+','+'))

	LABELS = {'A' : [A1,A2,A3],\
			  'L' : [L1,L2,L3,L4,L5,L6],\
			  'T' : [T1,T2,T3,T4],\
			  'Y' : [Y1,Y2,Y3,Y4,Y5]\
			 }

	def __init__(self, ind, typ, neig):
		#info brings the information encoded in the input (see above)
		self.index = ind
		self.neighbors = neig
		self.labelset = []
		labels = self.LABELS[typ]
		for label in labels:
			#initialize a dict
			adict = {'Name':label[0]}
			for i in range(len(self.neighbors)):
				adict[self.neighbors[i]] = label[1][i]
			self.labelset.append(adict)
		

	def prn(self):
		print("Junction "+str(self.index))
		for l in self.labelset:
			print(l)
		print('\n')

if __name__=='__main__':
	#form a figure (here we take the pyramid)
	# Uncomment the following  for Pyramid
# 	fig = Figure([\
# 	[1,'A',(2,3,4)],\
# 	[2,'L',(3,1)],\
# 	[3,'A',(4,1,2)],\
# 	[4,'L',(1,3)]])

	# The following is big T, comment it and uncomment the above for Pyramid
	fig = Figure([\
	[1,'L',(2,11)],\
	[2,'T',(3,12,1)],\
	[3,'A',(4,13,2)],\
	[4,'L',(5,3)],\
	[5,'A',(6,13,4)],\
	[6,'L',(7,5)],\
	[7,'A',(8,13,6)],\
	[8,'L',(9,7)],\
	[9,'T',(12,8,10)],\
	[10,'L',(11,9)],\
	[11,'A',(1,12,10)],\
	[12,'T',(2,9,11)],\
	[13,'Y',(5,7,3)]])

	fig.filter()
	for j in fig.junctions.values():
		j.prn()
