from random import randint
from tkinter import *
from tkinter.ttk import Treeview
from Gui.InputDialog import InputDialog
from Gui.Logger import Logger
from Names import Names
from Species.Animals.Antelope import Antelope
from Species.Animals.CyberSheep import CyberSheep
from Species.Animals.Fox import Fox
from Species.Animals.Human import Human
from Species.Animals.Sheep import Sheep
from Species.Animals.Turtle import Turtle
from Species.Animals.Wolf import Wolf
from Species.Plants.Dairy import Dairy
from Species.Plants.Grass import Grass
from Species.Plants.Guarana import Guarana
from Species.Plants.SosnowskysBorsch import SosnowskysBorsch
from Species.Plants.WolfBerries import WolfBerries
from World import World

# initial spawn proportions
ANIMAL_START_DIVIDER = 40
PLANT_START_DIVIDER = 60


class App:

	def __init__(self, parent):
		self.root = parent
		self.root.wm_title("Cyber Sheep")
		Grid.columnconfigure(self.root, 0, weight=1)
		Grid.columnconfigure(self.root, 1, weight=1)
		Grid.columnconfigure(self.root, 2, weight=0)
		Grid.rowconfigure(self.root, 1, weight=1)
		nfolabel = Label(self.root, text="Programowanie Obiektowe projekt 3: Cyber Sheep. Marcin Szycik 165116")
		nfolabel.grid(row=0, column=0, columnspan=2)

		thegrid = Treeview(self.root, displaycolumns=None)
		thegrid.grid(row=1, column=0, columnspan=2, sticky=N + E + W + S)

		nextturnbtn = Button(self.root, text="Next turn")
		nextturnbtn.grid(row=2, column=0, sticky=W + E)
		nextturnbtn.bind("<Button-1>", self.doturn)

		specialbtn = Button(self.root, text="Special ability")
		specialbtn.grid(row=2, column=1, sticky=W + E)

		savebtn = Button(self.root, text="Save")
		savebtn.grid(row=3, column=0, sticky=W + E)

		loadbtn = Button(self.root, text="Load")
		loadbtn.grid(row=3, column=1, sticky=W + E)

		countlbl = Label(self.root, text="Turn 0")
		countlbl.grid(row=4, column=0, columnspan=2, sticky=W + E)

		scrollbar = Scrollbar(self.root)
		scrollbar.grid(row=0, column=3, rowspan=5, sticky=N + S)

		log = Text(self.root, yscrollcommand=scrollbar.set)
		log.grid(row=0, column=2, rowspan=5, sticky=N + E + W + S)

		Logger.init(log)
		Logger.log("Welcome to Cyber Sheep")

		# set names
		Names.setspeciesnames({
			'W': "Wolf",
			'S': "Sheep",
			'F': "Fox",
			'T': "Turtle",
			'A': "Antelope",
			'H': "Human",
			'C': "Cyber Sheep",
			'G': "Grass",
			'D': "Dairy",
			'U': "Guarana",
			'B': "Wolf Berries",
			'O': "Sosnowsky's Borsch"
		})
		Names.setnames([
			"Jake",
			"Winston",
			"Harry",
			"Larry",
			"Lenny",
			"Johnny",
			"Spencer",
			"Fred",
			"Joey",
			"Steve",
			"Bob",
			"Mascara",
			"Mooriela",
			"Vicky",
			"Christina",
			"Vicky",
			"Daisy",
			"Elizabeth",
			"Dolores",
			"Esmeralda",
			"Matilda",
			"Jenny"
		])

		self.turn = 0
		worldx = int(InputDialog(self.root, "Enter world x", 20).show())
		worldy = int(InputDialog(self.root, "Enter world y", 20).show())

		animalstartmax = int((worldx * worldy) / ANIMAL_START_DIVIDER)
		plantstartmax = int((worldx * worldy) / PLANT_START_DIVIDER)

		# create world
		self.world = World(worldx, worldy)
		Logger.log("Created world (%dx%d)" % (worldx, worldy))

		self.world.addorganism(Human(self.world))  # HUMAN AFTER ALL (actually add him first)
		self.world.humanalive = True  # yep, he sure seems alive

		# add healthy amount of other organisms

		for i in range(0, randint(0, animalstartmax)):
			self.world.addorganism(Wolf(self.world))

		for i in range(0, randint(0, animalstartmax)):
			self.world.addorganism(Sheep(self.world))

		for i in range(0, randint(0, animalstartmax)):
			self.world.addorganism(Fox(self.world))

		for i in range(0, randint(0, animalstartmax)):
			self.world.addorganism(Turtle(self.world))

		for i in range(0, randint(0, animalstartmax)):
			self.world.addorganism(Antelope(self.world))

		for i in range(0, randint(0, animalstartmax)):
			self.world.addorganism(CyberSheep(self.world))

		for i in range(0, randint(0, plantstartmax)):
			self.world.addorganism(Grass(self.world))

		for i in range(0, randint(0, plantstartmax)):
			self.world.addorganism(Dairy(self.world))

		for i in range(0, randint(0, plantstartmax)):
			self.world.addorganism(Guarana(self.world))

		for i in range(0, randint(0, plantstartmax)):
			self.world.addorganism(WolfBerries(self.world))

		for i in range(0, randint(0, plantstartmax)):
			self.world.addorganism(SosnowskysBorsch(self.world))

	def doturn(self, event):
		self.turn += 1

		Logger.log("======= Round %d =======" % self.turn)
		Logger.log("Population: %d" % self.world.getorganismcount())
		self.world.doturn()
		self.drawworld()
		Logger.log("++++ Round %d ended ++++" % self.turn)

	def drawworld(self):
		Logger.log("TODO")  # TODO

if __name__ == '__main__':
	root = Tk()
	App(root)
	root.mainloop()
