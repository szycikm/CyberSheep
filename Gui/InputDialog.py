from tkinter import *

# based on https://stackoverflow.com/questions/28443749/how-do-i-return-a-result-from-a-dialog


class InputDialog(Toplevel):

	def __init__(self, parent, hint):
		Toplevel.__init__(self, parent)
		self.value = StringVar()
		self.label = Label(self, text=hint)
		self.entry = Entry(self, textvariable=self.value)
		self.ok_button = Button(self, text="OK", command=self.__ok_click)
		self.label.pack(fill=X)
		self.entry.pack(fill=X)
		self.ok_button.pack(fill=X)
		self.entry.bind("<Return>", self.__ok_click)
		self.grab_set()
		parent.lift()

	def __ok_click(self, event):
		self.destroy()
		self.grab_release()

	def show(self):
		self.wm_deiconify()
		self.entry.focus_force()
		self.wait_window()
		return self.value.get()
