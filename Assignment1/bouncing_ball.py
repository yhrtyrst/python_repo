"""
File: bouncing_ball.py
Name: Blair
-------------------------
TODO: This program simulates a bouncing ball at (START_X, START_Y)
      that has VX as x velocity and 0 as y velocity. Each bounce reduces
      y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
# 滑鼠點擊次數
counter = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(start)


def start(mouse):
    global ball
    global counter
    vy = 0
    if ball.x == START_X and ball.y == START_Y:  # 只有球在起點時可以開始運動
        counter += 1
        while counter <= 3:
            vy += GRAVITY
            ball.move(VX, vy)
            if ball.y + ball.height >= window.height:  # 碰到地板
                vy *= -REDUCE
                if vy > 0:
                    vy = -vy
            if ball.x + ball.width > window.width:  # 超出視窗外
                window.remove(ball)
                break
            pause(DELAY)
        ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)  # 重新建一個新球
        ball.filled = True
        window.add(ball)


if __name__ == "__main__":
    main()
