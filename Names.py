import random


class Names:

	__speciesnames = {}
	__speciescolors = {}
	__names = []

	@staticmethod
	def setspeciesnames(speciesnames):
		Names.__speciesnames = speciesnames

	@staticmethod
	def setspeciescolors(speciescolors):
		Names.__speciescolors = speciescolors

	@staticmethod
	def setnames(names):
		Names.__names = names

	@staticmethod
	def getspeciesname(letter):
		if letter in Names.__speciesnames:
			return Names.__speciesnames[letter]
		return "Undefined"

	@staticmethod
	def getspeciescolor(letter):
		if letter in Names.__speciescolors:
			return Names.__speciescolors[letter]
		return "black"

	@staticmethod
	def getrandomname():
		if any(Names.__names):
			return random.choice(Names.__names)
		return "Undefined"
