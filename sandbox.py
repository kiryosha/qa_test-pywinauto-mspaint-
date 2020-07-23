# TODO: реализовать...
#  * возможность выбора ластика, карандаша, заливки и пипетыча
#  * возможность изменять ширину и высоту полотна в px без сохранения пропорций
#  * возможность выбирать для рисования равносторонний треугольник
#  * возможность указать сплошной цвет заливки
#  * возможность указать цвет в фортах RGB и HSV (через диалог изменения цветов)

from pywinauto.keyboard import send_keys
from src.paint import Paint
import time


def main():
	app_init = Paint()
	main_init = app_init.ribbon()
	choice_tool = main_init.tool()()
	# Ластик
	choice_tool.child_window(title="Ластик", control_type="Button").click()
	time.sleep(2)
	# Карандаш
	choice_tool.child_window(title="Карандаш", control_type="Button").click()
	time.sleep(2)
	# Заливка
	choice_tool.child_window(title="Заливка цветом", control_type="Button").click()
	time.sleep(2)
	# Политра
	choice_tool.child_window(title="Палитра", control_type="Button").click()
	time.sleep(2)

	# Изменить размер
	img_init = main_init.image()
	img_init.change_size().invoke()
	change_init = app_init.size_changing_dialog()
	change_window = change_init()
	# Высота в px
	change_window.child_window(title="пиксели", auto_id="1102", control_type="RadioButton").click()
	# Без сохранения пропорций
	change_window.child_window(title="Сохранить пропорции", auto_id="1100", control_type="CheckBox").click()
	# По вертикали
	change_window.child_window(title="Изменить размер по вертикали", auto_id="1020", control_type="Edit").set_text("1080")
	# По горизонтали
	change_window.child_window(title="Изменить размер по горизонтали", auto_id="1019", control_type="Edit").set_text("1920")
	# Ok
	(change_init.apply()).click()

	# Треугольник
	choice_figure = main_init.figure()()
	choice_figure.child_window(title="Треугольник", control_type="ListItem").invoke()
	# Выбор второго цвета
	color_init = main_init.color()
	app_init().child_window(title="Цвет 2", control_type="Button").click()
	# Цвет
	color_init.change_color().invoke()
	change_color = app_init.color_changing_dialog()
	color_window = change_color()
	# H
	color_window.child_window(title="Оттенок:", auto_id="703", control_type="Edit").set_text("239")
	# S
	color_window.child_window(title="Контраст:", auto_id="704", control_type="Edit").set_text("102")
	# V
	color_window.child_window(title="Яркость:", auto_id="705", control_type="Edit").set_text("42")
	# R
	color_window.child_window(title="Красный:", auto_id="706", control_type="Edit").set_text("72")
	# G
	color_window.child_window(title="Зеленый:", auto_id="707", control_type="Edit").set_text("255")
	# B
	color_window.child_window(title="Синий:", auto_id="708", control_type="Edit").set_text("10")
	# Ok
	(change_color.apply()).click()
	# Заливка
	main_init.fill()()
	time.sleep(1)
	send_keys("{VK_DOWN}")
	send_keys("{ENTER}")
	app_init().drag_mouse_input(dst=(400, 400), src=(800, 650), button='left', pressed='', absolute=True)
	time.sleep(2)


if __name__ == "__main__":
	main()
