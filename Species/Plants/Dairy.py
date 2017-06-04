from Species.Plant import Plant


class Dairy(Plant):

	def __init__(self, fromworld, x=None, y=None, age=0, strength=0, initiative=0):
		super().__init__(fromworld, x, y)
		self._age = age
		self._strength = strength if strength != 0 else 0
		self._initiative = initiative if initiative != 0 else 0
		self._type = 'D'

	def clone(self, fromworld, position):
		return Dairy(fromworld, position.x, position.y)

	def action(self):
		for i in range(0, 2):
			super().action()
