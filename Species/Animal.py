from Names import Names
from Species.Organism import Organism, ADULT_AGE
from Species.Plant import Plant


class Animal(Organism):

	def __init__(self, fromworld, x, y):
		self._name = Names.getrandomname()
		super().__init__(fromworld, x, y)

	def action(self):
		"""default animal behaviour"""
		self.move(self.randomizefield())

	def getname(self):
		return self._name

	def incrementage(self):
		super().incrementage()
		if self.getage() == ADULT_AGE:
			print("%s is all grown up now!" % (self.introduce()))  # TODO write this in UI

	def introduce(self):
		return "%s %s" % (Names.getspeciesname(self._type), self._name)

	def tostring(self):
		return super().tostring() + ";" + self._name

	def move(self, nextposition):
		if self.collision(self._fromworld.getorganismbyposition(nextposition)):
			self._position = nextposition
			print("%s moved to (%i,%i)" % (self.introduce(), self._position.x, self._position.y))  # TODO write this in UI

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
					print("D'awww. %s and %s are having a baby! And it's name is %s" % (self.introduce(), other.introduce(), child.getname()))  # TODO write this in UI
					return False

			# no place for the baby
			print("%s and %s wanted to have a baby, but the world decided otherwise" % (self.introduce(), other.introduce()))
			return False
		else:
			# stronger (or attacker) wins and takes looser's field
			if self.getstrength() >= other.getstrength():
				if other.tryresistattack(self):
					print("%s resisted %s's attack!" % (other.introduce(), self.introduce()))
					return False  # other organism reflected attarck -> don't move
				else:
					print("Yeah! %s ate %s!" % (self.introduce(), other.introduce()))
					other.die()  # how dramatic
					return True  # we just killed organism that standed there -> we now take it's place
			else:
				if isinstance(other, Plant):
					print("Oh no! %s ate %s and DIED!" % (self.introduce(), other.introduce()))  # we just ate a plant TODO write this in UI
				else:
					print("Oh no! %s ate %s!" % (other.introduce(), self.introduce()))

				self.die()
				return False
