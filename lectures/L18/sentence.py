class Sentence(object):
	def __init__(self, text):
		self.text = text
		self.index = 0
		self.words = text.split()

	def __iter__(self):
		word =  self.words[self.index]
		self.index += 1
		return word

	def __next__(self):
		pass
