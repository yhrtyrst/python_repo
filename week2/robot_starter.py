# user
from robot import Robot, Robot2, Robot3
from campy.graphics.gwindow import GWindow


def main():
    #window = GWindow()
    # robot3 = Robot3(180, 50, 'gold', color3='red', count3=6)
    # robot3.say_hi()
    # ball = robot3.give_me_a_ball(50)
    # rect = robot3.give_me_a_rect(80)
    # robot3.start_count()
    #
    # window.add(rect)
    # window.add(ball)
    # robot2 = Robot2(183, 80, color2='red', count2=5)
    # robot2.start_count()
    # robot2.say_hi()
    # big_ball = robot2.give_me_a_ball(900)
    # window.add(big_ball)

    Robot.say_hi()
    r1 = Robot(color='blue', weight=70, height=183)  # 只要輸入keyword 就可以不依照順序輸入參數
    ball1 = r1.give_me_a_ball(80)
    r1.self_introduce()
    r1.bmi()
    r1.say_hi()
    # window.add(ball1)
    #
    # r3 = Robot(183, 70, color='gold')
    # ball3 = r3.give_me_a_ball(80)
    # r3.self_introduce()
    # r3.bmi()
    #
    # r2 = Robot(170, 80)
    # ball2 = r2.give_me_a_ball(10)
    # r2.say_hi()
    #
    # window.add(ball1)
    # window.add(ball2)
    # window.add(ball3, x=100, y=100)


if __name__ == '__main__':
    print('robot_starter.py(__name__):', __name__)
    main()
