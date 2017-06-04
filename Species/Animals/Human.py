from enum import Enum
from Coordinates import Coordinates
from Gui.Logger import Logger
from Species.Animal import Animal

SPECIAL_COUNTDOWN = 5
SPECIAL_STRENGTH = 10


class HumanTasks(Enum):
	DO_NOTHING = 0
	GO_UP = 1
	GO_DOWN = 2
	GO_LEFT = 3
	GO_RIGHT = 4
	DO_SPECIAL = 5


class Human(Animal):

	def __init__(self, fromworld, x=None, y=None, age=0, strength=0, initiative=0, name="", specialcountdown=0):
		super().__init__(fromworld, x, y)
		self._age = age
		self._strength = strength if strength != 0 else 5
		self._initiative = initiative if initiative != 0 else 4
		if name != "":
			self._name = name
		self._type = 'H'
		self.__specialcountdown = specialcountdown
		self.__nexttask = HumanTasks.DO_NOTHING
		self._fromworld.humanalive = True

	def clone(self, fromworld, position):
		return Human(fromworld, position.x, position.y)

	def action(self):
		if self.__specialcountdown > 0:
			self.__specialcountdown -= 1
			self._strength -= 1
			Logger.log("%s's strength is dropping! %i turns till normal" % (self.introduce(), self.__specialcountdown))
		if self.__nexttask == HumanTasks.GO_UP:
			self.move(Coordinates(self._position.x, self._position.y - 1))
		elif self.__nexttask == HumanTasks.GO_DOWN:
			self.move(Coordinates(self._position.x, self._position.y + 1))
		elif self.__nexttask == HumanTasks.GO_LEFT:
			self.move(Coordinates(self._position.x - 1, self._position.y))
		elif self.__nexttask == HumanTasks.GO_RIGHT:
			self.move(Coordinates(self._position.x + 1, self._position.y))
		elif self.__nexttask == HumanTasks.DO_SPECIAL:
			self.__specialcountdown = SPECIAL_COUNTDOWN
			self._strength = SPECIAL_STRENGTH
			Logger.log("%s used their special ability!" % (self.introduce()))
		else:
			Logger.log("%s had nothing to do this turn" % (self.introduce()))
		self.__nexttask = HumanTasks.DO_NOTHING

	def istasklegal(self, task):
		if task == HumanTasks.GO_UP:
			return self._position.y - 1 >= 0
		elif task == HumanTasks.GO_DOWN:
			return self._position.y + 1 < self._fromworld.getmaxxy().y
		elif task == HumanTasks.GO_LEFT:
			return self._position.x - 1 >= 0
		elif task == HumanTasks.GO_RIGHT:
			return self._position.x + 1 < self._fromworld.getmaxxy().x
		elif task == HumanTasks.DO_SPECIAL:
			return self.__specialcountdown <= 0
		else:
			return False

	def setnexttask(self, task):
		self.__nexttask = task

	def die(self):
		super().die()
		self._fromworld.humanalive = False

	def tostring(self):
		return "%s%i" % (super().tostring(), self.__specialcountdown)
