from subprocess import Popen, PIPE
import sys


class Flookup():

	def __init__(self, direction='up', machine=None):

		# set the transducer machine
		if not machine:
			sys.stderr.write("\nFlookup requires a machine path as string: Flookup(machine='my_machine.fst')")
			sys.stderr.write("\nExiting...\n")
			sys.exit()
		else:
			self.machine = machine

		# start and set the flookup process
		self.process = self._start(direction,machine)
	
	def _start(self,direction,machine):
		if direction == 'up':
			dir = []
		elif direction == 'down':
			dir = ['-i']
		else:
			sys.stderr.write("\nFlookup: unrecognized direction specification %s' % direction")
			sys.stderr.write("\nExiting...\n")
			sys.exit()

		proc = Popen(['flookup'] + dir + ['-b','-w',""">>>
""",machine], stdin=PIPE, stdout=PIPE)
		sys.stderr.write('\nFlookup: process successfully started.\n')
		return proc

	def stop(self):
		self.process.stdin.close()
		self.process.stdout.close()
		self.process.wait()
		sys.stderr.write("\nflookup finished with return code %d\n" % self.process.returncode)

	def parse(self, word):
		word = bytes(word.strip()+'\n', "utf-8")
		self.process.stdin.write(word)
		self.process.stdin.flush()
		acc = []
		while True:
			line = self.process.stdout.readline().decode('utf-8')
			if line.startswith('>>>'):
				break
			elif line.endswith('+?\n'):
				self.process.stdout.readline()
				return []
			acc.append(line.strip().split('\t')[1])
		
		return acc			

	def tokenize(self,sentence):
		sentence = bytes(sentence.strip()+'\n', "utf-8")
		self.process.stdin.write(sentence)
		self.process.stdin.flush()
		output = self.process.stdout.readline().decode('utf-8').strip()
		self.process.stdout.readline()
		self.process.stdout.readline()
		return output.split('\t')[1].split(' ')

if __name__ == '__main__':
	#	parser = Flookup(machine='/home/umut/bin/fst/trmorph.fst')
	tokenizer = Flookup(machine='/home/umut/bin/fst/tokenize.fst')
#	print(parser.parse('araba'))
#	print(parser.parse('asparserdad'))
#	print(parser.parse('ev'))

	print(tokenizer.tokenize("ali eve gitti mi?"))
	print(tokenizer.tokenize("ali arbaya gitti mi?"))
	print(tokenizer.tokenize("ali eve/arbaya gitti mi?"))
	#parser.stop()
	tokenizer.stop()

