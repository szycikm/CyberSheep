from Species.Animal import Animal


class Wolf(Animal):

	def __init__(self, fromworld, x=None, y=None, age=0, strength=0, initiative=0, name=""):
		super().__init__(fromworld, x, y)
		self._age = age
		self.strength = strength if strength != 0 else 9
		self.initiative = initiative if initiative != 0 else 5
		self._name = name
		self._type = 'W'

	def clone(self, fromworld, position):
		return Wolf(fromworld, position.x, position.y)
