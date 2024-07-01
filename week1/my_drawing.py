"""
File: my_drawing.py
Name: Blair
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(width=800, height=500, title='myFace')
    face = GOval(200, 250, x=350, y=200)
    face.filled = True
    face.fill_color = 'gold'
    face.color = 'dodgerblue'
    r_eye = GOval(50, 50, x=390, y=250)
    r_eye.filled = True
    r_eye.fill_color = 'black'
    l_eye = GOval(50, 50, x=460, y=250)
    l_eye.filled = True
    l_eye.fill_color = 'black'
    mouth = GRect(50, 10, x=430, y=400)
    mouth.filled = True
    mouth.fill_color = 'red'
    label = GLabel('Hello World!', x=350, y=180)
    label.font = '-40'
    trangle = GPolygon()


    window.add(label)
    window.add(face)
    window.add(r_eye)
    window.add(l_eye)
    window.add(mouth)


if __name__ == '__main__':
    main()
