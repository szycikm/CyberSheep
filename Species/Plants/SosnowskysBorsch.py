from Gui.Logger import Logger
from Species.Animal import Animal
from Species.Plant import Plant


class SosnowskysBorsch(Plant):

	def __init__(self, fromworld, x=None, y=None, age=0, strength=0, initiative=0):
		super().__init__(fromworld, x, y)
		self._age = age
		self._strength = strength if strength != 0 else 10
		self._initiative = initiative if initiative != 0 else 0
		self._type = 'O'

	def clone(self, fromworld, position):
		return SosnowskysBorsch(fromworld, position.x, position.y)

	def action(self):
		"""destroy them with lazers"""
		for coords in self.randomizefields():
			victim = self._fromworld.getorganismbyposition(coords)
			from Species.Animals.CyberSheep import CyberSheep
			if victim is not None and isinstance(victim, Animal) and not isinstance(victim, CyberSheep):
				Logger.log("%s got too close to %s and DIED" % (victim.introduce(), self.introduce()))
				victim.die()
		super().action()  # and after it kills everything, it tries to reproduce
