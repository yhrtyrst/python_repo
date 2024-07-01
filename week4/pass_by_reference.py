"""
File: pass_by_reference.py
Name: Jerry Liao
-------------------------------
This program demonstrates the concept of 
pass-by-reference by showing the color change 
of a GRect
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow

window = GWindow()


def main():
	rect = GRect(100, 100) # rect 存的是位址 記憶體位址 不是一個rect
	rect.filled = True # . 前往記憶體位址找到filled那一層
	rect.fill_color = 'green'
	window.add(rect, 0, 0)
	change_color(rect)


def change_color(rect):
	rect.fill_color = 'magenta'


if __name__ == '__main__':
	main()
