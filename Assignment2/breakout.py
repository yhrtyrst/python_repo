"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    ball = graphics.ball
    paddle = graphics.paddle
    total_bricks = graphics.get_brick_cols() * graphics.get_brick_rows()
    lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        if lives == 0:  # 剩 0 命遊戲終止
            break
        if total_bricks == 0:  # bricks 全部消除遊戲終止
            break
        ball.move(graphics.get_ball_dx(), graphics.get_ball_dy())

        # 開始偵測球的四個點
        maybe_obj = graphics.window.get_object_at(ball.x, ball.y)
        if maybe_obj is None:
            maybe_obj = graphics.window.get_object_at(ball.x + ball.width, ball.y)
            if maybe_obj is None:
                maybe_obj = graphics.window.get_object_at(ball.x + ball.width, ball.y + ball.height)
                if maybe_obj is None:
                    maybe_obj = graphics.window.get_object_at(ball.x, ball.y + ball.height)

        ball_dx = graphics.get_ball_dx()
        ball_dy = graphics.get_ball_dy()

        if maybe_obj is not None:
            if maybe_obj is paddle:  # 遇到 paddle 反彈
                graphics.set_ball_dy(-ball_dy)
            else:                    # 遇到 brick 反彈和消除
                graphics.set_ball_dx(-ball_dx)
                graphics.set_ball_dy(-ball_dy)
                graphics.window.remove(maybe_obj)
                total_bricks -= 1

        if ball.x + ball.width >= graphics.window.width or ball.x <= 0:  # 撞到視窗左右
            graphics.set_ball_dx(-ball_dx)
        if ball.y <= 0:  # 撞到視窗頂部
            graphics.set_ball_dy(-ball_dy)
        if ball.y + ball.height >= graphics.window.height:  # 掉出視窗下方
            graphics.window.remove(ball)
            lives -= 1
            if lives > 0:
                ball = graphics.ball
                graphics.window.add(ball, x=(graphics.window.width - ball.width) / 2,
                                    y=(graphics.window.height - ball.width) / 2)
                graphics.set_ball_dx(0)
                graphics.set_ball_dy(0)
        pause(FRAME_RATE)
    graphics.show_the_end()


if __name__ == '__main__':
    main()
