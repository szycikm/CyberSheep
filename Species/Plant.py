from random import randint

from Names import Names
from Species.Organism import Organism


class Plant(Organism):
	def __init__(self, fromworld, x, y):
		super().__init__(fromworld, x, y)

	def action(self):
		"""1/4 chance to sew"""
		if randint(0, 3) == 0:
			for coords in self.randomizefields():
				if self._fromworld.getorganismbyposition(coords) is None:
					self._fromworld.addorganism(self.clone(self._fromworld, coords))
					return

	def introduce(self):
		return Names.getspeciesname(self._type)

	def tostring(self):
		return "%s;;" % (super().tostring())
