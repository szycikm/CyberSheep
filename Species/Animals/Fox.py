from Gui.Logger import Logger
from Species.Animal import Animal


class Fox(Animal):

	def __init__(self, fromworld, x=None, y=None, age=0, strength=0, initiative=0, name=""):
		super().__init__(fromworld, x, y)
		self._age = age
		self._strength = strength if strength != 0 else 3
		self._initiative = initiative if initiative != 0 else 7
		if name != "":
			self._name = name
		self._type = 'F'

	def clone(self, fromworld, position):
		return Fox(fromworld, position.x, position.y)

	def action(self):
		"""sneaky fox checks all directions and decides where to move (if at all)"""
		for coords in self.randomizefields():
			collider = self._fromworld.getorganismbyposition(coords)
			# move to empty field, or attack weaker organism. sneaky
			if collider is None or (collider is not None and collider.getstrength() <= self.getstrength()):
				self.move(coords)
				return
		Logger.log("%s decided to stay in place" % (self.introduce()))
