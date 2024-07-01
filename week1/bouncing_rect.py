"""
File: bouncing_rect.py
Name: 
------------------------
This file shows how to make a simple 
animation by campy library
"""
from campy.graphics.gobjects import GRect
from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause

# This controls the width and height of the rect
SIZE = 30

# This controls the pause time (in millisecond) for the animation
DELAY = 10


def main():
	window = GWindow()
	rect = set_up_rect()
	vx = 5
	window.add(rect, x=(window.width - SIZE) / 2, y=(window.height - SIZE) / 2)
	while True:
		rect.move(vx, 0)
		if rect.x + rect.width >= window.width or rect.x <= 0:
			vx = -vx
		pause(DELAY)


def set_up_rect():
	rect = GRect(SIZE, SIZE, x=430, y=400)
	rect.filled = True
	rect.fill_color = 'red'
	return rect
			

if __name__ == '__main__':
	main()
