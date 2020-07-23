from pywinauto.application import Application
from subprocess import Popen

from src.ribbon import Ribbon
from src.size_changing_dialog import SizeChangingDialog
from src.color_changing_dialog import ColorChangingDialog


class Paint:
	__paint_process = None
	_paint = None

	def __init__(self):
		self.__paint_process = Popen(["mspaint"])
		self._paint = Application(backend="uia").connect(process=self.__paint_process.pid)
		self._paint = self._paint.window()

	def __del__(self):
		self.__paint_process.terminate()

	def __call__(self, *args, **kwargs):
		return self._paint

	def ribbon(self):
		return Ribbon(self())

	def size_changing_dialog(self):
		return SizeChangingDialog(self())

	def color_changing_dialog(self):
		return ColorChangingDialog(self())
