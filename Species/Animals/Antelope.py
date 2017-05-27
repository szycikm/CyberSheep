from Species.Animal import Animal


class Antelope(Animal):

	def __init__(self, fromworld, x=None, y=None, age=0, strength=0, initiative=0, name=""):
		super().__init__(fromworld, x, y)
		if age != 0:
			self._age = age
		self.strength = strength if strength != 0 else 4
		self.initiative = initiative if initiative != 0 else 4
		if name != "":
			self._name = name
		self._type = 'A';

	def clone(self, fromworld, position):
		return Antelope(fromworld, position.x, position.y)

	def action(self):
		for i in range(0, 1):
			if self.isalive():
				self.move(self.randomizefield())

	def tryresistattack(self, attacker):
		for coords in self.randomizefields():
			if self._fromworld.getorganismbyposition(coords) is None:
				self.move(coords)
				print("%s got away from %s" % (self.introduce(), attacker.introduce()))  # TODO write this in UI
				return True
		print("%s tried to run, but you can't hide from %s" % (self.introduce(), attacker.introduce()))  # TODO write this in UI
		return False

	def tostring(self):
		return "%s;" % (super().tostring())
