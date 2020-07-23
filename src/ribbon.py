class Ribbon:
	class ImageGroup:
		__parent = None

		def __init__(self, parent):
			self.__parent = parent

		def __call__(self, *args, **kwargs):
			return self.__parent.child_window(title="Изображение", control_type="ToolBar")

		def change_size(self):
			return self().child_window(title="Изменить размер", control_type="Button")

	class Colors:
		__parent = None

		def __init__(self, parent):
			self.__parent = parent

		def __call__(self, *args, **kwargs):
			return self.__parent.child_window(title="Цвета", control_type="ToolBar")

		def change_color(self):
			return self().child_window(title="Изменение цветов", control_type="Button")

		def color_two(self):
			return self().child_window(title="Цвет 2", control_type="Button")

	class Tools:
		__parent = None

		def __init__(self, parent):
			self.__parent = parent

		def __call__(self, *args, **kwargs):
			return self.__parent.child_window(title="Инструменты", control_type="ToolBar")

		def eraser(self):
			return self().child_window(title="Ластик", control_type="Button")

		def pencil(self):
			return self().child_window(title="Карандаш", control_type="Button")

		def fill(self):
			return self().child_window(title="Заливка цветом", control_type="Button")

		def palette(self):
			return self().child_window(title="Палитра", control_type="Button")

	class Figures:
		__parent = None

		def __init__(self, parent):
			self.__parent = parent

		def __call__(self, *args, **kwargs):
			return self.__parent.child_window(title="Фигуры", control_type="ToolBar")

		def delta(self):
			return self().child_window(title="Треугольник", control_type="ListItem")

		def choice_fill(self):
			return self().child_window(title="Заливка", control_type="SplitButton")

	__ppt = None

	def __init__(self, ppt):
		self.__ppt = ppt

	def __call__(self, *args, **kwargs):
		return self.__ppt.child_window(title="Главная", control_type="Custom")

	def image(self):
		return Ribbon.ImageGroup(self())

	def color(self):
		return Ribbon.Colors(self())

	def tool(self):
		return Ribbon.Tools(self())

	def figure(self):
		return Ribbon.Figures(self())

	def grab(self):
		return self.__ppt.drag_mouse_input(dst=(400, 400), src=(800, 650), button='left', pressed='', absolute=True)

