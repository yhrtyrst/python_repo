"""
File: my_drawing.py
Name: Blair
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GArc
from campy.graphics.gwindow import GWindow

SIZE = 70
RECT_SIZE = 500
window = GWindow(title='A Birthday Card')


def main():
    """
    Title: A Birthday Card
    My friends' birthday is coming. I made a card to bless them.
    """
    rect = GRect(RECT_SIZE, RECT_SIZE)
    fill_color_and_add_to_window(rect, 'skyblue')
    label = GLabel('Happy Birthday to Aries!')
    label.font = 'courier-20-italic'
    label.color = 'teal'
    window.add(label, x=70, y=115)

    foot1 = GRect(10, 80, x=(window.width-SIZE)/2-50, y=(window.height-SIZE)/2+100)
    foot2 = GRect(10, 80, x=(window.width - SIZE) / 2 + 5, y=(window.height - SIZE) / 2 + 100)
    foot3 = GRect(10, 80, x=(window.width - SIZE) / 2 + 70, y=(window.height - SIZE) / 2 + 100)
    foot4 = GRect(10, 80, x=(window.width - SIZE) / 2 + 120, y=(window.height - SIZE) / 2 + 100)
    fill_color_and_add_to_window(foot1, 'black')
    fill_color_and_add_to_window(foot2, 'black')
    fill_color_and_add_to_window(foot3, 'black')
    fill_color_and_add_to_window(foot4, 'black')

    hoof1 = GOval(20, 10, x=(window.width - SIZE) / 2 - 60, y=(window.height - SIZE) / 2 + 170)
    hoof2 = GOval(20, 10, x=(window.width - SIZE) / 2 - 5, y=(window.height - SIZE) / 2 + 170)
    hoof3 = GOval(20, 10, x=(window.width - SIZE) / 2 + 60, y=(window.height - SIZE) / 2 + 170)
    hoof4 = GOval(20, 10, x=(window.width - SIZE) / 2 + 110, y=(window.height - SIZE) / 2 + 170)
    fill_color_and_add_to_window(hoof1, 'black')
    fill_color_and_add_to_window(hoof2, 'black')
    fill_color_and_add_to_window(hoof3, 'black')
    fill_color_and_add_to_window(hoof4, 'black')

    oval0 = GOval(SIZE, SIZE, x=(window.width-SIZE)/2-50, y=(window.height-SIZE)/2+10)
    oval1 = GOval(SIZE, SIZE, x=oval0.x, y=oval0.y+40)
    oval2 = GOval(SIZE, SIZE, x=oval0.x, y=oval0.y+65)
    oval3 = GOval(SIZE, SIZE, x=oval0.x - 35, y=oval0.y + 20)

    fill_color_and_add_to_window(oval0, 'white')
    fill_color_and_add_to_window(oval1, 'white')
    fill_color_and_add_to_window(oval2, 'white')
    fill_color_and_add_to_window(oval3, 'white')

    for i in range(1):
        oval3 = GOval(SIZE, SIZE, x=oval3.x, y=oval3.y + 25)
        fill_color_and_add_to_window(oval3, 'white')

    head = GOval(60, 80, x=oval3.x-30, y=oval3.y-25)
    fill_color_and_add_to_window(head, 'black')

    r_ear = GArc(250, 100, 10, 35)
    fill_color_and_add_to_window(r_ear, 'black')
    window.add(r_ear, x=head.x-30, y=head.y+5)

    l_ear = GArc(250, 100, 180, 35)
    fill_color_and_add_to_window(l_ear, 'black')
    window.add(l_ear, x=head.x - 35, y=head.y + 5)

    hair = GOval(25, 25, x=oval3.x - 30, y=oval3.y - 30)
    fill_color_and_add_to_window(hair, 'white')
    for i in range(3):
        hair = GOval(25, 25, x=hair.x+10, y=hair.y)
        fill_color_and_add_to_window(hair, 'white')
    hair = GOval(20, 20, x=oval3.x - 18, y=oval3.y - 40)
    fill_color_and_add_to_window(hair, 'white')
    hair = GOval(20, 20, x=oval3.x -5, y=oval3.y - 40)
    fill_color_and_add_to_window(hair, 'white')

    l_eye = GOval(21, 21, x=oval3.x-20, y=oval3.y+2)
    fill_color_and_add_to_window(l_eye, 'white')

    l_eye1 = GOval(10, 10, x=oval3.x - 16, y=oval3.y + 4)
    fill_color_and_add_to_window(l_eye1, 'black')

    r_eye = GOval(21, 21, x=oval3.x+1, y=oval3.y + 2)
    fill_color_and_add_to_window(r_eye, 'white')

    r_eye1 = GOval(10, 10, x=oval3.x + 6, y=oval3.y + 4)
    fill_color_and_add_to_window(r_eye1, 'black')


    for i in range(2):
        oval0 = GOval(SIZE, SIZE, x=oval0.x + 50, y=oval0.y)
        oval1 = GOval(SIZE, SIZE, x=oval0.x, y=oval0.y + 40)
        oval2 = GOval(SIZE, SIZE, x=oval0.x, y=oval0.y + 65)
        fill_color_and_add_to_window(oval0, 'white')
        fill_color_and_add_to_window(oval1, 'white')
        fill_color_and_add_to_window(oval2, 'white')

    oval4 = GOval(SIZE, SIZE, x=oval0.x + 30, y=oval3.y-25)
    fill_color_and_add_to_window(oval4, 'white')
    oval4 = GOval(SIZE, SIZE, x=oval4.x, y=oval3.y+10)
    fill_color_and_add_to_window(oval4, 'white')
    tail = GOval(30, 30, x=oval4.x+50, y=oval3.y+10)
    fill_color_and_add_to_window(tail, 'white')


def fill_color_and_add_to_window(obj, color):
    obj.filled = True
    obj.fill_color = color
    obj.color = color
    window.add(obj)


if __name__ == '__main__':
    main()
