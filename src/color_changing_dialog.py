class ColorChangingDialog:
    __parent = None

    def __init__(self, parent):
        self.__parent = parent

    def __call__(self, *args, **kwargs):
        return self.__parent.child_window(title="Изменение палитры", control_type="Window")

    def apply(self):
        return self().child_window(title="ОК", auto_id="1", control_type="Button")

    def shade(self):
        return self().child_window(title="Оттенок:", auto_id="703", control_type="Edit")

    def contrast(self):
        return self().child_window(title="Контраст:", auto_id="704", control_type="Edit")

    def brightness(self):
        return self().child_window(title="Яркость:", auto_id="705", control_type="Edit")

    def red(self):
        return self().child_window(title="Красный:", auto_id="706", control_type="Edit")

    def green(self):
        return self().child_window(title="Зеленый:", auto_id="707", control_type="Edit")

    def blue(self):
        return self().child_window(title="Синий:", auto_id="708", control_type="Edit")

