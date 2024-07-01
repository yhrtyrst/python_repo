from campy.gui.events.timer import pause
from zonegraphics import ZoneGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    This program plays a Python game 'zone'
    A ball will be bouncing around the GWindow
    Players must defend the zone indicated by black
    line at the middle of the GWindow by clicking on
    the bouncing ball
    """
    graphics = ZoneGraphics()
    lives = NUM_LIVES
    while True:
        if graphics.ball_in_zone():
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            else:
                break
        # update
        graphics.ball.move(graphics.dx, graphics.dy)
        # check
        if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
            # bounce
            graphics.dx *= -1
        elif graphics.ball.y <= 0 or graphics.ball.y+graphics.ball.height >= graphics.window.height:
            # bounce
            graphics.dy *= -1
        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
