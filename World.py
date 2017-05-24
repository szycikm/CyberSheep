class World:

	def __init__(self, maxxy):
		self.__maxxy = maxxy
		self.__organisms = []
		self.humanalive = False

	def getmaxxy(self):
		return self.__maxxy

	def getorganismcount(self):
		return len(self.__organisms)

	def getorganismbyposition(self, position):
		for org in self.__organisms:
			if org.isalive() and org.getxy().x == position.x and org.getxy().y == position.y:
				return org
		return None

	def gethuman(self):
		for org in self.__organisms:
			if isinstance(org, Human) and org.isalive():
				return org
		return None

	def doturn(self):
		self.__organisms.sort()
		cnt = self.getorganismcount()  # organism count can get bigger so it's important to keep it in separate variable
		for i in range(0, cnt):
			if self.__organisms[i].isalive():
				self.__organisms[i].action()

			if self.__organisms[i].isalive():  # again, because self organism might have just died
				self.__organisms[i].incrementAge()

		# clean dead __organisms
		for i in range(0, self.getorganismcount()):
			if not self.__organisms[i].isalive():
				self.__organisms.remove(self.__organisms[i])
				i -= 1  # because we just deleted i-th element

	def addorganism(self, o):
		if o.getxy().x >= self.__maxxy.x or o.getxy().y >= self.__maxxy.y or o.getor().x < 0 or o.getXY().y < 0:
			# coordinates outside of self world
			return False
		elif self.getorganismbyposition(o.getxy()) is None:
			# field already occupied
			return False
		else:
			self.__organisms.append(o)
			return True

	def tostring(self):
		everything = "%i\n%i" % (self.__maxxy.x, self.__maxxy.y)
		for org in self.__organisms:
			everything += "\n" + org.tostring()
		return everything
