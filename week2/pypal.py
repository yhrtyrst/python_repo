
WITHDRAW_LIMIT = 1000
MONEY = 0


class Pypal:
    def __init__(self, name, money=MONEY, withdraw_limit=WITHDRAW_LIMIT):
        self._n = name
        self.__m = money
        self._w_l = withdraw_limit

    def set_name(self, new_name):
        print(f'Successfully updated! from {self._n} to {new_name}')
        self._n = new_name

    def get_money(self):
        return self.__m

    def withdraw(self, amount):
        if amount > self._w_l:
            print('Exceed Limit')
        elif amount > self.__m:
            print('Illegal')
        else:
            self.__m -= amount
            print(f'{self._n} remains: {self.__m}')

    def __str__(self):  # str的名稱是指展示的字串是什麼 可以客製化print出來的資訊 而非記憶體位址
        return f'name: {self._n} / money: {self.__m} / limit: {self._w_l}'


# def bank():  也可以在coder端執行
#     jerry_a = Pypal('YangHung', money=1000, withdraw_limit=700)
#     jerry_a.withdraw(1000)
#     jerry_a.withdraw(500)
#     jerry_a.withdraw(600)
#     bob_a = Pypal('Robert', money=10000, withdraw_limit=7000)
#     bob_a.withdraw(5000)

#
# if __name__ == '__main__':
#     bank()
