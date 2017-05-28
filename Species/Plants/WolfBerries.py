from Species.Plant import Plant


class WolfBerries(Plant):

	def __init__(self, fromworld, x=None, y=None, age=0, strength=0, initiative=0):
		super().__init__(fromworld, x, y)
		self._age = age
		self.strength = strength if strength != 0 else 99
		self.initiative = initiative if initiative != 0 else 0
		self._type = 'B'

	def clone(self, fromworld, position):
		return WolfBerries(fromworld, position.x, position.y)
