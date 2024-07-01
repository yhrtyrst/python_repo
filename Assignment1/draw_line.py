"""
File: draw_line.py
Name: Blair
-------------------------
TODO: This program creates lines on an instance of GWindow class.
      There is a circle indicating the user’s first click. A line appears
      at the condition where the circle disappears as the user clicks
      on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
count = 0
start_x = 0
start_y = 0
window = GWindow(title='draw_line')
oval = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click_a_circle)


def click_a_circle(mouse):
    global count
    global start_x
    global start_y
    global oval
    count += 1  # 計算滑鼠點擊次數
    if count % 2 == 1:  # 點擊奇數次
        window.add(oval, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        start_x = oval.x  # 把圓的左上角座標存在 global variable 給直線當起點使用
        start_y = oval.y
    else:
        line = GLine(start_x + SIZE / 2, start_y + SIZE / 2, mouse.x, mouse.y)
        # oval = window.get_object_at(start_x + SIZE / 2, start_y + SIZE / 2)  # start_x,start_y為左上角座標，需指到圓內
        window.remove(oval)
        window.add(line)


if __name__ == "__main__":
    main()
