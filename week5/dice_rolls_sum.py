"""
File: dice_rolls_sum.py
Name: Blair
-----------------------------
This program finds all the dice rolls permutations
that sum up to a constant TOTAL. Students will find
early stopping a good strategy of decreasing the number
of recursive calls
"""

# This constant controls the sum of dice of our interest
TOTAL = 8


def main():
    dice_sum(TOTAL)


def dice_sum(target_sum):
    counter = []  # 存在heap 不受 stack frame影響 如果是 int 存在stack 會受stack frame影響
    dice_sum_helper(target_sum, [], counter)
    print(sum(counter))


def dice_sum_helper(target_sum, current_lst, counter):
    counter.append(1)
    if sum(current_lst) <= target_sum:
        if sum(current_lst) == target_sum:
            print(current_lst)
        else:
            for die in [1, 2, 3, 4, 5, 6]:
                if die + sum(current_lst) > target_sum:  # early stopping
                    break
                else:
                    # choose
                    current_lst.append(die)
                    # explore
                    dice_sum_helper(target_sum, current_lst, counter)
                    # un-choose
                    current_lst.pop()





if __name__ == '__main__':
    main()
