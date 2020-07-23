class SizeChangingDialog:
	__parent = None

	def __init__(self, parent):
		self.__parent = parent

	def __call__(self, *args, **kwargs):
		return self.__parent.child_window(title="Изменение размеров и наклона", control_type="Window")

	def apply(self):
		return self().child_window(title="ОК", auto_id="1", control_type="Button")

	def height_px(self):
		return self().child_window(title="пиксели", auto_id="1102", control_type="RadioButton")

	def not_save(self):
		return self().child_window(title="Сохранить пропорции", auto_id="1100", control_type="CheckBox")

	def vertical_size(self):
		return self().child_window(title="Изменить размер по вертикали", auto_id="1020", control_type="Edit")

	def horizontal_size(self):
		return self().child_window(title="Изменить размер по горизонтали", auto_id="1019", control_type="Edit")
