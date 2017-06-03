import logging
from tkinter import DISABLED, END, NORMAL

# from https://stackoverflow.com/questions/13318742/python-logging-to-tkinter-text-widget


class WidgetLogger(logging.Handler):
	def __init__(self, widget):
		logging.Handler.__init__(self)
		self.setLevel(logging.INFO)
		self.widget = widget
		self.widget.config(state=DISABLED)

	def emit(self, record):
		self.widget.config(state=NORMAL)
		self.widget.insert(END, '\n' + record)  # append
		self.widget.see(END)  # scroll to the bottom
		self.widget.config(state=DISABLED)
