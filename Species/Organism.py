from abc import abstractmethod
from random import randint, shuffle
from Coordinates import Coordinates

ADULT_AGE = 5


class Organism:

	def __init__(self, fromworld, x, y):
		if x is None or y is None:
			x = randint(0, fromworld.getmaxxy().x)
			y = randint(0, fromworld.getmaxxy().y)
		self._fromworld = fromworld
		self._position = Coordinates(x, y)
		self._type = None
		self._strength = None
		self._initiative = None
		self.__age = 0
		self.__alive = True

	def __lt__(self, other):
		if self.getinitiative() == other.getinitiative():
			return self.getage() > other.getage()
		else:
			return self.getinitiative() > other.getinitiative()

	@abstractmethod
	def clone(self, fromworld, position):
		pass

	@abstractmethod
	def action(self):
		pass

	@abstractmethod
	def introduce(self):
		pass

	def tryresistattack(self, attacker):
		return False

	def gettype(self):
		return self._type

	def draw(self):
		"""if organism is below ADULT_AGE turns draw it small. Just for fun."""
		return self._type.lower() if self.__age < ADULT_AGE else self._type

	def getxy(self):
		return self._position

	def getage(self):
		return self.__age

	def getstrength(self):
		return self._strength

	def setstrength(self, strength):
		self._strength = strength

	def getinitiative(self):
		return self._initiative

	def incrementage(self):
		self.__age += 1

	def isalive(self):
		return self.__alive

	def die(self):
		"""fly, fly, PIZZA DIE!"""
		self.__alive = False  # don't actually die, just mark organism as dead

	def tostring(self):
		return "%s;%i;%i%i%i%i" % (self._type, self.__age, self._strength, self._initiative, self._position.x, self._position.y)

	def randomizefields(self):
		"""randomizes 2 to 4 new coordinates respecting the world limits"""
		randomized = []
		if self._position.x + 1 < self._fromworld.getmaxxy().x:
			randomized.append(Coordinates(self._position.x + 1, self._position.y))
		if self._position.x > 0:
			randomized.append(Coordinates(self._position.x - 1, self._position.y))
		if self._position.y + 1 < self._fromworld.getmaxxy().y:
			randomized.append(Coordinates(self._position.x, self._position.y + 1))
		if self._position.y > 0:
			randomized.append(Coordinates(self._position.x, self._position.y - 1))
		shuffle(randomized)
		return randomized
