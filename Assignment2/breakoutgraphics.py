"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 6        # Maximum initial horizontal speed for the ball
BALL_COLOR = 'olive'   # Color of the ball
PADDLE_COLOR = 'olive' # Color of the paddle


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self._window_height = window_height
        self._window_width = window_width
        self.__brick_rows = brick_rows
        self.__brick_cols = brick_cols

        # Create a paddle
        paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width) / 2, y=window_height - paddle_offset)
        self.paddle = paddle
        self._paddle_offset = paddle_offset
        self.fill_color_and_add_to_window(paddle, PADDLE_COLOR)

        # Center a filled ball in the graphical window
        ball = GOval(ball_radius*2, ball_radius*2, x=(window_width-ball_radius*2)/2, y=(window_height-ball_radius*2)/2)
        self.ball = ball
        self._start_x = ball.x
        self._start_y = ball.y
        self.fill_color_and_add_to_window(ball, BALL_COLOR)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_velocity)
        onmousemoved(self.move_paddle)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height, x=j*(brick_width+brick_spacing),
                              y=brick_offset + i*(brick_height+brick_spacing))
                if i == 0 or i == 1:
                    self.fill_color_and_add_to_window(brick, 'moredarkgreen')
                elif i == 2 or i == 3:
                    self.fill_color_and_add_to_window(brick, 'darkgreen')
                elif i == 4 or i == 5:
                    self.fill_color_and_add_to_window(brick, 'forestgreen')
                elif i == 6 or i == 7:
                    self.fill_color_and_add_to_window(brick, 'limegreen')
                elif i == 8 or i == 9:
                    self.fill_color_and_add_to_window(brick, 'lightgreen')

    def show_the_end(self):
        end_background = GRect(self._window_width, self._window_height)
        self.fill_color_and_add_to_window(end_background, 'teal')
        text = GLabel("The End")
        text.font = 'courier-40-italic'
        self.window.add(text, x=(self._window_width - text.width)/2, y=(self._window_height - text.height)/2)

    def fill_color_and_add_to_window(self, obj, color):
        obj.filled = True
        obj.fill_color = color
        obj.color = color
        self.window.add(obj)

    def move_paddle(self, mouse):
        paddle_middle_x = mouse.x - self.paddle.width/2  # 滑鼠置於 paddle 中間
        self.window.add(self.paddle, x=paddle_middle_x, y=self._window_height - self._paddle_offset)

        if self.paddle.x <= 0:  # 超出視窗左邊
            self.window.add(self.paddle, x=0, y=self._window_height - self._paddle_offset)
        elif self.paddle.x + self.paddle.width >= self._window_width:  # 超出視窗右邊
            self.window.add(self.paddle, x=self._window_width-self.paddle.width,
                            y=self._window_height - self._paddle_offset)

    def set_ball_velocity(self, mouse):
        if self.ball.x == self._start_x and self._start_y == self._start_y:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED + 1)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def get_ball_dx(self):
        return self.__dx

    def set_ball_dx(self, dx):
        self.__dx = dx

    def get_ball_dy(self):
        return self.__dy

    def set_ball_dy(self, dy):
        self.__dy = dy

    def get_brick_rows(self):
        return self.__brick_rows

    def get_brick_cols(self):
        return self.__brick_cols


