from tkinter import *
from tkinter.ttk import Treeview

from Gui.InputDialog import InputDialog
from Gui.Logger import Logger

from Names import Names
from World import World

ANIMAL_START_MAX = 7
PLANT_START_MAX = 2

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
root.wm_title("Cyber Sheep")

for column in range(3):
	Grid.columnconfigure(root, column, weight=1)

Grid.rowconfigure(root, 1, weight=1)

nfolabel = Label(root, text="Programowanie Obiektowe projekt 3: Cyber Sheep. Marcin Szycik 165116")
nfolabel.grid(row=0, column=0, columnspan=3)

thegrid = Treeview(root, displaycolumns=None)
thegrid.grid(row=1, column=0, columnspan=3, sticky=W+E+N+S)

nextturnbtn = Button(root, text="Next turn")
nextturnbtn.grid(row=2, column=0, sticky=W+E)

upbtn = Button(root, text="\u2191")
upbtn.grid(row=2, column=1)

savebtn = Button(root, text="Save")
savebtn.grid(row=2, column=2, sticky=W+E)

leftbtn = Button(root, text="\u2190")
leftbtn.grid(row=3, column=0, sticky=E)

countlbl = Label(root, text="0")
countlbl.grid(row=3, column=1)

rightbtn = Button(root, text="\u2192")
rightbtn.grid(row=3, column=2, sticky=W)

specialbtn = Button(root, text="Special ability")
specialbtn.grid(row=4, column=0, sticky=W+E)

downbtn = Button(root, text="\u2193")
downbtn.grid(row=4, column=1)

loadbtn = Button(root, text="Load")
loadbtn.grid(row=4, column=2, sticky=W+E)

scrollbar = Scrollbar(root)
scrollbar.grid(row=0, column=4, rowspan=5, sticky=N+S)

log = Text(root, yscrollcommand=scrollbar.set)
log.grid(row=0, column=3, rowspan=5, sticky=N+S+E+W)

Logger.init(log)
Logger.log("Welcome to Cyber Sheep")

turn = 0
worldx = int(InputDialog(root, "Enter world x").show())
worldy = int(InputDialog(root, "Enter world y").show())

world = World(worldx, worldy)
Logger.log("Created world (%dx%d)" % (worldx, worldy))
root.mainloop()
