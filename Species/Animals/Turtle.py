from random import randint

from Gui.Logger import Logger
from Species.Animal import Animal

TURTLE_RESIST_STRENGTH = 5


class Turtle(Animal):

	def __init__(self, fromworld, x=None, y=None, age=0, strength=0, initiative=0, name=""):
		super().__init__(fromworld, x, y)
		self._age = age
		self.strength = strength if strength != 0 else 2
		self.initiative = initiative if initiative != 0 else 1
		if name != "":
			self._name = name
		self._type = 'T'

	def clone(self, fromworld, position):
		return Turtle(fromworld, position.x, position.y)

	def tryresistattack(self, attacker):
		return attacker.getstrength() < TURTLE_RESIST_STRENGTH

	def action(self):
		"""lazy turtle moves with 25% chance"""
		if randint(0, 3) == 0:
			super().action()
		else:
			Logger.log("%s decided not to move" % (self.introduce()))
