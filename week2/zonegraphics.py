from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
ZONE_WIDTH = 100
ZONE_HEIGHT = 100
BALL_RADIUS = 15
MAX_SPEED = 6
MIN_Y_SPEED = 2


class ZoneGraphics:

    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 zone_width=ZONE_WIDTH, zone_height=ZONE_HEIGHT, ball_radius=BALL_RADIUS):
        # Create window
        self.window = GWindow(width=window_width, height=window_height, title='ZoneGame')

        # Create zone
        self.zone = GRect(zone_width, zone_height, x=(window_width-zone_width)/2, y=(window_height-zone_height)/2)
        self.zone.color = 'blue'
        self.window.add(self.zone)

        # Create ball and initialize velocity/position
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'green'
        self.ball.color = 'green'
        self.window.add(self.ball)

        self.dx = 0
        self.dy = 0
        self.reset_ball()

        # Initialize mouse listeners
        onmouseclicked(self.handle_click)

    def handle_click(self, mouse):
        obj = self.window.get_object_at(mouse.x, mouse.y)
        if obj == self.ball:
            self.reset_ball()

    def reset_ball(self):
        self.set_ball_position()
        while self.ball_in_zone():
            self.set_ball_position()
        self.set_ball_velocity()
        self.window.add(self.ball)

    def set_ball_velocity(self):
        self.dx = random.randint(0, MAX_SPEED)
        self.dy = random.randint(MIN_Y_SPEED, MAX_SPEED)
        if random.random() > 0.5:
            self.dx = -self.dx
        if random.random() > 0.5:
            self.dy = -self.dy

    def set_ball_position(self):
        self.ball.x = random.randint(0, self.window.width - self.ball.width)
        self.ball.y = random.randint(0, self.window.height - self.ball.height)

    def ball_in_zone(self):
        zone_left_side = self.zone.x
        zone_right_side = self.zone.x + self.zone.width
        is_ball_x_in_zone = zone_left_side <= self.ball.x <= zone_right_side - self.ball.width

        zone_top = self.zone.y
        zone_bottom = self.zone.y + self.zone.height
        is_ball_y_in_zone = zone_top <= self.ball.y <= zone_bottom

        return is_ball_x_in_zone and is_ball_y_in_zone
