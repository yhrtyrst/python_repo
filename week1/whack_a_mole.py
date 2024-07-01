"""
File: whack_a_mole.py
Name: 
---------------------------
This program plays a game called
"whack a mole" in which players 
clicking the popping moles 
on screen to gain scores 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 550

# Constant controls the pause time of the animation
DELAY = 700

# Global variables
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title='Whack_a_mole')
score = 0
label = GLabel('Score: ' + str(score))


def main():
    label.font = '-30'
    window.add(label, x=0, y=label.height+10)
    onmouseclicked(remove)
    while True:  # 一秒可以執行幾億次，所以要延遲
        img = GImage('mole.png')
        random.x = random.randint(0, window.width - img.width)
        random.y = random.randint(0, window.height - img.height)
        window.add(img, x=random.x, y=random.y)
        pause(DELAY)


def remove(event):
    global score
    maybe_mole = window.get_object_at(event.x, event.y)
    if maybe_mole is not None and maybe_mole is not label:
        window.remove(maybe_mole)
        score += 1
    label.text = 'Score: ' + str(score)


if __name__ == '__main__':
    main()
