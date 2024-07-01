# coder
from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow


class Robot:
    def __init__(self, height, weight, color='green'):
        self.h = height
        self.w = weight
        self.c = color

    # instance method * 3
    def give_me_a_ball(self, size):
        window = GWindow()
        ball = GOval(size, size)
        #ball._width = 500
        print(ball.width,'test')
        ball.filled = True
        ball.fill_color = self.c
        ball.color = self.c
        window.add(ball)
        return window

    def self_introduce(self):
        print(f'h={self.h}/w={self.w}')

    def bmi(self):
        h_in_m = self.h/100
        bmi = self.w/(h_in_m**2)
        print('bmi:', bmi)

    # static method 不會用到 self
    @staticmethod
    def say_hi():
        print('\\Hi!')


class Robot2(Robot):  # 承襲Robot
    def __init__(self, height2, weight2, color2='green', count2=3):
        super().__init__(height2, weight2, color=color2)
        # 啟動super class 'Robot' constructor, 不加self是因為現在在class Robot2裡面, self已經不共用了

        self.count = count2

    def start_count(self):
        for i in range(self.count):
            print(i+1, end='')
        print('')


class Robot3(Robot2):
    def __init__(self, height3, weight3, rect_color3, color3='green', count3=3):
        # print('robot.py(__name__):', __name__)
        super().__init__(height3, weight3, color2=color3, count2=count3)
        self.r_c = rect_color3

    def give_me_a_rect(self, size):
        rect = GRect(size, size)
        rect.filled = True
        rect.fill_color = self.r_c
        return rect


# print('robot.py(__name__):', __name__) python不嚴謹 這行可以被執行


if __name__ == '__main__':
    print('robot.py(__name__):', __name__)
