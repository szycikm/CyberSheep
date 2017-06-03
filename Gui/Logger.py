from Gui.WidgetLogger import WidgetLogger


class Logger:

	__logger = None

	@staticmethod
	def init(widget):
		Logger.__logger = WidgetLogger(widget)

	@staticmethod
	def log(message):
		Logger.__logger.emit(message)
