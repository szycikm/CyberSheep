from Gui.Logger import Logger
from Species.Plant import Plant

BONUS_STRENGTH = 3


class Guarana(Plant):

	def __init__(self, fromworld, x=None, y=None, age=0, strength=0, initiative=0):
		super().__init__(fromworld, x, y)
		self._age = age
		self._strength = strength if strength != 0 else 0
		self._initiative = initiative if initiative != 0 else 0
		self._type = 'U'

	def clone(self, fromworld, position):
		return Guarana(fromworld, position.x, position.y)

	def tryresistattack(self, attacker):
		attacker.setstrength(attacker.getstrength() + BONUS_STRENGTH)
		Logger.log("%s ate %s and is FEELING STRONGER" % (attacker.introduce(), self.introduce()))
		return False
