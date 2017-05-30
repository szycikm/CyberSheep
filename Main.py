from Names import Names
from tkinter import *

ANIMAL_START_MAX = 7
PLANT_START_MAX = 2

turn = 0
worldx = 0
worldy = 0

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

root = Tk()
label = Label(root, text="je sa")
label.pack()
root.mainloop()
