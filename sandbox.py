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
	tool_bar = main_init.tool()
	# Ластик
	tool_bar.eraser().click()
	time.sleep(2)
	# Карандаш
	tool_bar.pencil().click()
	time.sleep(2)
	# Заливка
	tool_bar.fill().click()
	time.sleep(2)
	# Политра
	tool_bar.palette().click()
	time.sleep(2)

	# Изменить размер
	img_init = main_init.image()
	img_init.change_size().invoke()
	change_size = app_init.size_changing_dialog()
	# Высота в px
	change_size.height_px().click()
	# Без сохранения пропорций
	change_size.not_save().click()
	# По вертикали
	change_size.vertical_size().set_text("1080")
	# По горизонтали
	change_size.horizontal_size().set_text("1920")
	# Ok
	change_size.apply().click()

	# Треугольник
	delta = main_init.figure()
	delta.delta().invoke()
	# Выбор второго цвета
	color_init = main_init.color()
	color_init.color_two().click()
	# Цвет
	color_init.change_color().invoke()
	change_color = app_init.color_changing_dialog()
	# H
	change_color.shade().set_text("239")
	# S
	change_color.contrast().set_text("102")
	# V
	change_color.brightness().set_text("42")
	# R
	change_color.red().set_text("72")
	# G
	change_color.green().set_text("255")
	# B
	change_color.blue().set_text("10")
	# Ok
	change_color.apply().click()
	# Заливка
	delta.choice_fill().invoke()
	time.sleep(1)
	send_keys("{VK_DOWN}")
	send_keys("{ENTER}")
	main_init.grab()
	time.sleep(2)


if __name__ == "__main__":
	main()
