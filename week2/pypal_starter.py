import pypal


def bank():
    jerry_a = pypal.Pypal('YangHung', money=1000, withdraw_limit=700)
    jerry_a.set_name('bj')
    jerry_a._n = 'change again'
    #print(jerry_a.name, 'test')  #  另外寫getter 才可以print出來
    print(jerry_a._n,'test') #  可以印出來
    jerry_a.withdraw(1000)
    jerry_a.withdraw(500)
    jerry_a.withdraw(600)
    bob_a = pypal.Pypal('Robert', money=10000, withdraw_limit=7000)
    print(bob_a.get_money())
    bob_a.withdraw(5000)

    print(jerry_a)


if __name__ == '__main__':
    bank()  # 可以改變執行的第一個function
