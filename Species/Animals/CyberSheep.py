import math
from Coordinates import Coordinates
from Species.Animal import Animal


class CyberSheep(Animal):

	def __init__(self, fromworld, x=None, y=None, age=0, strength=0, initiative=0, name=""):
		super().__init__(fromworld, x, y)
		self._age = age
		self.strength = strength if strength != 0 else 11
		self.initiative = initiative if initiative != 0 else 4
		if name != "":
			self._name = name
		self._type = 'C'

	def clone(self, fromworld, position):
		return CyberSheep(fromworld, position.x, position.y)

	def action(self):  # TODO test
		target = None
		nearestdistance = -1
		from Species.Plants.SosnowskysBorsch import SosnowskysBorsch
		for org in self._fromworld.getorganismsbytype(SosnowskysBorsch):
			dist = org.getdistanceto(self)
			if (target is not None and dist < nearestdistance) or nearestdistance == -1:
				target = org
				nearestdistance = dist
		if target is None:
			super().action()  # couldn't find any borschs - remain normal yet powerful sheep
		else:
			dx = target.getxy().x - self.getxy().x
			dy = target.getxy().y - self.getxy().y
			if math.fabs(dx) > math.fabs(dy):
				# move x
				self.move(Coordinates(self.getxy().x + (1 if dx < 0 else -1), self.getxy().y))
			else:
				# move y
				self.move(Coordinates(self.getxy().x, self.getxy().y + (1 if dy < 0 else -1)))
