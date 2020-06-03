"""A module for the course
	COGS 502 -- Programming and Logic
	
	Cognitive Science
	Informatics Institute
	Middle East Technical Unviersity

	version 1.0 -- Dec 2015	
	"""
import sys

_interpreter_version = sys.version_info[0]

def read_str(prompt='A string please: '):
	"""Prompts the user to enter a string and returns the value entered. 
	Provide a string argument to read_str for a custom prompt message.

	Example:

	>>> import cogs502
	>>> name = cogs502.read_str()
	A string please: Pythagoras
	>>> name
	'Pythagoras'
	>>> name = cogs502.read_str('Please enter your name: ')
	Please enter your name: Pythagoras
	>>> name
	'Pythagoras'
	>>>
	"""
	if _interpreter_version == 2:
		from_user = raw_input(prompt)
	elif _interpreter_version == 3:
		from_user = input(prompt)
	else:
		from_user = None
	return from_user
		
def read_int(prompt='An integer please: '):
	"""Prompts the user to enter an integer and returns the value entered. 
	Provide a string argument to read_str for a custom prompt message.

	Example:

	>>> import cogs502
	>>> age = cogs502.read_int()
	An integer please: 21 
	>>> age
	21
	>>> age = cogs502.read_int('Please enter your age: ')
	Please enter your age: 21 
	>>> age
 	21	
	>>>
	"""
	try:
		return int(input(prompt))
	except:
		print('Ooops, I think that was not an integer. Let\'s try again.')
		return read_int(prompt)  

def read_float(prompt='A float please: '):
	"""Prompts the user to enter a floating point number and returns the value entered. 
	Provide a string argument to read_str for a custom prompt message.

	Example:

	>>> import cogs502
	>>> height = cogs502.read_float()
	An float please: 1.75 
	>>> height
	1.75
	>>> height = cogs502.read_float('Please enter your height: ')
	Please enter your height: 1.75 
	>>> height
 	1.75	
	>>>
	"""
	try:
		return float(input(prompt))
	except:
		print('Ooops, I think that was not a float. Let\'s try again.')
		return read_float(prompt)

def read_list(prompt='A list please: '):
	"""Prompts the user to enter a list and returns the value entered. 
	Provide a string argument to read_list for a custom prompt message.

	The list can be arbitrarily complex; and you can use any delimiter other 
	than brackets, dot and numbers for strings in the list.

	Example:

	import cogs502
	>>> mylist = cogs502.read_list(
	A list please: ['abra',[3,'cad'],[[4],4]]
	>>> mylist
	['abra', [3, 'cad'], [[4], 4]]
	>>> mylist = cogs502.read_list('Give me a list of names: ')
	Give me a list of names: ['jill','jane',/mary/,-jack-]
	>>> mylist
	['jill', 'jane', 'mary', 'jack']
	>>>)

	"""
	if _interpreter_version==2:
		from_user = raw_input(prompt)
	elif _interpreter_version==3:
		from_user = input(prompt)
	else:
		from_user = None
	try:
		if from_user[0]!='[': raise
		return _read_list(from_user, [],'','')
	except:
		print('Ooops, I think that was not a valid list. Let\'s try again.')
		return read_list(prompt)

def _read_list(input_tape,stack,string_store,number_store):
	try:
		current_symbol =  input_tape[0]
	except:
		if len(stack) !=1 :
			raise
		else:
			return stack[0]#when the input_tape finishes you will have the first and only element on your stack as the list you are trying to construct, so return it. 
	#
	# Now we will handle all the possible types of symbols we read on the input_tape
	#
	# Let's start with the opening bracket.
	# When we encounter it we push it to the stack.
	# Stack is the right kind of structure for capturing nested dependencies. 
	#  
	#
	#Now the code for handling strings in the list
	#
	#First, how to start reading a string:
	#The first non-number and non-bracket and non-dot and non-comma thing you read when the string_store is empty
	#will be taken as the string delimiter"""
	#
	if not string_store:#if string_store is empty 
		#if you encounter a digit or a point, store them in number_store
		if current_symbol == '[':
			stack.append('[')
		elif current_symbol.isdigit() or current_symbol == '.':
			number_store += current_symbol
		#if it turns out that the current symbol is not a digit or comma, then 
		#there are two cases we need to distinguish. The current_symbol might be a 
		#start of a string, *unless* it's a bracket or a comma. In the following condition we
		#capture such a case. We store the symbol in string_store, we treat it as the delimiter of
		#a string.
		#
		elif not current_symbol in ['[',']',',']:
			string_store += current_symbol
		#When you read a comma, all you need to care about are numbers.
		#List type elements and string type elements are delimited by
		#their special delimiters, but numbers do not come by delimiters -- so we
		#use comma as marking the end of a number. This corresponds to the state when 
		#the number_store is non-empty and the current_symbol is the comma.
		#
		elif current_symbol == ',' and number_store:
			#if your number has a point somewhere in it, you need
			#to have it as float, otherwise as integer. The following
			#code does this in a logically reverse order.
			if number_store.find('.') == -1:
				stack.append(int(number_store))
			else:
				stack.append(float(number_store))
			#don't forget to reset your number_store
			number_store = ''
		#
		#
		#Now let's decide what to do upon encountering a closing bracket ']'
		#
		#When you see this you form a list including all the elements
		#you encountered since you last saw an opening bracket '['
		#
		#But before forming this list and pushing it to your stack,
		#you should check whether there has been any number reading
		#going on. Remember that numbers do not have delimiters, 
		#but they are always immediately followd by a comma or a closing bracket.
		#
		elif current_symbol == ']':
			#Actually it would have been nicer to have this number reading buisiness
			#as a function, in order not to repeat it here -- you can do it as an exercise.
			if number_store:
				if number_store.find('.') == -1:
					stack.append(int(number_store))
				else:
					stack.append(float(number_store))
				number_store=''
			#
			#After reading any possible number, now it is time to 
			#form a list upto the last encountered openning bracket.
			#The following code does this.
			#
			accumulator = [] 
			top = stack.pop()
			while top != '[':
				accumulator = [top] + accumulator
				top = stack.pop()
			#
			#you've gathered your list, now push it to the stack
			#
			stack.append(accumulator)
	#
	# Now let us code what to do when the string_store is non-empty.
	# which means we had started to read a string. 
	#
	elif string_store:#if string_store is non-empty
		#First test whether you have reached the 
		#end of the string you've been reading.
		#You can do it by comparing the current_symbol
		#to the initial symbol of the string_store
		if current_symbol == string_store[0]:
			#if that's the case than push the string you've read
			#to the main stack -- but you should not be taking the
			#very first symbol on the string_store, since that's the
			#delimeter.
			stack.append(string_store[1:])
			#As you are finished with the current string, it's time to reset
			#your string_store
			string_store = ''
		else:
			#if you are here, then it means you read a symbol that is part
			#of the string, so just append it to string_store
			string_store+= current_symbol
	#You have done whatever you can do with the current_symbol,
	#it's time to go on with the rest.
	return _read_list(input_tape[1:],stack,string_store,number_store)
