import vim

def shortex(tokenList):
	return ["\shortex{" + str(len(tokenList)) + "}{" + " & ".join(tokenList) + "}", "{" + "&".join([" " for i in range(len(tokenList))]) + "}","{`'}"]  

currentBuffer = vim.current.buffer
currentLine = vim.current.line
currentLineNumber = vim.current.window.cursor[0]

currentBuffer.append(shortex(currentLine.split()),currentLineNumber)
del currentBuffer[currentLineNumber-1]


def amper(tokenList):
	"""Takes a list and returns latex tabular raw with &s
	"""
	if len(tokenList) == 1:
		return str(tokenList[0])
	else:
		return str(tokenList[0]) + " & " + amper(tokenList[1:]) 	




