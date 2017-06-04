"""THE GRID. A digital frontier. (...)"""
from tkinter import Canvas, HIDDEN, NORMAL

SCALE = 30
HALFSCALE = 15

class TheGrid(Canvas):

	def __init__(self, parent, w, h, buttontext):
		super().__init__(parent, width=(w+1)*SCALE, height=(h+1)*SCALE)
		self.__w = w
		self.__h = h
		self.__labels = []
		self.__buttons = []
		self.__recs = []
		self.__buttontext = buttontext
		for i in range(self.__w):
			self.__labels.append([])
			self.__buttons.append([])
			self.__recs.append([])
			for j in range(self.__h):
				self.__buttons[i].append(self.create_text((i+1)*SCALE, (j+1)*SCALE, text=self.__buttontext))
				self.__recs[i].append(self.create_rectangle((i+1)*SCALE+HALFSCALE, (j+1)*SCALE+HALFSCALE, (i+1)*SCALE-HALFSCALE, (j+1)*SCALE-HALFSCALE, outline=""))
				self.__labels[i].append(self.create_text((i+1)*SCALE, (j+1)*SCALE))

	def show(self, x, y, value, color):
		self.itemconfig(self.__labels[x][y], state=NORMAL, text=value)
		self.itemconfig(self.__recs[x][y], state=NORMAL, fill=color)

	def clear(self):
		for i in range(self.__w):
			for j in range(self.__h):
				self.itemconfig(self.__labels[i][j], state=HIDDEN)
				self.itemconfig(self.__recs[i][j], state=HIDDEN)
