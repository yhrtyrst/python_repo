"""
File: hole_puncher.py
Name: Blair
------------------------
This file shows how to use campy
mouse event to punch holes (GOval)
on GWindow
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.mouse import onmousemoved

# This constant controls the size of the hole
SIZE = 30

# Global Variable
window = GWindow()
hole_x = 0
hole_y = 0


def main():
	onmouseclicked(create_hole)
	# onmousemoved(create_hole)


def create_hole(mouse):
	global hole_y
	global hole_x
	black = GOval(SIZE, SIZE, x=mouse.x - SIZE/2, y=mouse.y - SIZE/2)
	# black = GOval(SIZE, SIZE, x=mouse.x + SIZE / 2, y=mouse.y + SIZE / 2)
	hole_x = black.x
	hole_y = black.y
	print(black)
	print(hole_x, hole_y)
	black.filled = True
	red = GOval(SIZE, SIZE, x=mouse.x, y=mouse.y)
	red.filled = True
	red.fill_color = 'red'
	window.add(black)
	window.add(red)
	test = window.get_object_at(hole_x, hole_y)
	print(test)
	test1 = window.get_object_at(hole_x + SIZE/2, hole_y + SIZE/2)
	print(hole_x + SIZE/2)
	print(test1)

if __name__ == '__main__':
	main()
