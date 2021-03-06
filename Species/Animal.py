from Gui.Logger import Logger
from Names import Names
from Species.Organism import Organism, ADULT_AGE
from Species.Plant import Plant


class Animal(Organism):

	def __init__(self, fromworld, x, y):
		super().__init__(fromworld, x, y)
		self._name = Names.getrandomname()

	def action(self):
		"""default animal behaviour"""
		self.move(self.randomizefield())

	def getname(self):
		return self._name

	def incrementage(self):
		super().incrementage()
		if self.getage() == ADULT_AGE:
			Logger.log("%s is all grown up now!" % (self.introduce()))

	def introduce(self):
		return "%s %s" % (Names.getspeciesname(self._type), self._name)

	def tostring(self):
		return "%s;%s;" % (super().tostring(), self._name)

	def move(self, nextposition):
		if self.collision(self._fromworld.getorganismbyposition(nextposition)):
			self._position = nextposition
			Logger.log("%s moved to (%d,%d)" % (self.introduce(), self._position.x, self._position.y))

	def randomizefield(self):
		"""just grab the first random field"""
		return self.randomizefields()[0]

	def collision(self, other):
		"""default animal collision logic. return value = if animal should be moved or not"""
		if other is None:
			return True  # nothing stands here so we might as well go there
		elif self.gettype() == other.gettype():
			# animal of the	same type stands here -> just have sex and don't go there

			# pick a place for the baby
			for coords in self.randomizefields():
				child = self.clone(self._fromworld, coords)
				if self._fromworld.addorganism(child):
					Logger.log("D'awww. %s and %s are having a baby! And it's name is %s" % (self.introduce(), other.introduce(), child.getname()))
					return False

			# no place for the baby
			Logger.log("%s and %s wanted to have a baby, but the world decided otherwise" % (self.introduce(), other.introduce()))
			return False
		else:
			# stronger (or attacker) wins and takes looser's field
			if self.getstrength() >= other.getstrength():
				if other.tryresistattack(self):
					Logger.log("%s resisted %s's attack!" % (other.introduce(), self.introduce()))
					return False  # other organism reflected attarck -> don't move
				else:
					Logger.log("Yeah! %s ate %s!" % (self.introduce(), other.introduce()))
					other.die()  # how dramatic
					return True  # we just killed organism that standed there -> we now take it's place
			else:
				if isinstance(other, Plant):
					Logger.log("Oh no! %s ate %s and DIED!" % (self.introduce(), other.introduce()))  # we just ate a plant
				else:
					Logger.log("Oh no! %s ate %s!" % (other.introduce(), self.introduce()))

				self.die()
				return False
