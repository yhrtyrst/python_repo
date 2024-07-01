"""
File: mouse_draw.py
Name: Blair
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousedragged
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the pen stroke
SIZE = 30

window = GWindow()


def main():
	onmousedragged(draw)
	onmouseclicked(draw)


def draw(mouse):
	pen_stroke = GOval(SIZE, SIZE)

	if mouse.x > window.width/2:
		color = 'red'
	else:
		color = 'gold'

	pen_stroke.filled = True
	pen_stroke.color = color
	pen_stroke.fill_color = color


	window.add(pen_stroke, x=mouse.x - SIZE/2, y=mouse.y - SIZE/2)



if __name__ == '__main__':
	main()
