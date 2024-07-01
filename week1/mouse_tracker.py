"""
File: mouse_tracker.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved, onmouseclicked, onmousedragged

# This constant controls the size of the GRect
SIZE = 100
rect = GRect(SIZE, SIZE)
window = GWindow()
COLOR = 'blue'


def main():
	rect.filled = True
	rect.fill_color = COLOR
	rect.color = COLOR
	window.add(rect)
	onmouseclicked(draw)
	onmousedragged(draw)
	onmousemoved(reset_position)


def draw(mouse):
	rect_click = GRect(SIZE, SIZE)
	rect_click.filled = True
	rect_click.color = COLOR
	rect_click.fill_color = COLOR
	window.add(rect_click, mouse.x - SIZE/2, mouse.y - SIZE/2)


def reset_position(mouse):
	# rect.x = mouse.x - SIZE/2
	# rect.y = mouse.y - SIZE/2
	window.add(rect, mouse.x - SIZE/2, mouse.y - SIZE/2)


if __name__ == '__main__':
	main()
