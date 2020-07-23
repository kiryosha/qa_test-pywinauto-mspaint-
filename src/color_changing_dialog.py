class ColorChangingDialog:
    __parent = None

    def __init__(self, parent):
        self.__parent = parent

    def __call__(self, *args, **kwargs):
        return self.__parent.child_window(title="Изменение палитры", control_type="Window")

    def apply(self):
        return self().child_window(title="ОК", auto_id="1", control_type="Button")

