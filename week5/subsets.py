"""
File: subsets.py
Name:
-------------------------
This file prints all the sub-lists on Console
by calling a recursive function - list_sub_lists(lst).
subsets.py is a famous LeetCode Medium problem
"""


def main():
    """
    LeetCode Medium Problem
    """
    list_sub_lists([1, 2, 3, 4])


def list_sub_lists(lst):
    """
    :param lst: list[str], containing a number of characters
    """
    helper(lst, [])


def helper(lst, current_lst):
    # base case
    if len(lst) == 0:
        print(current_lst)
    else:
        # choose
        ele = lst.pop()

        # explore without the ele
        helper(lst, current_lst)

        # explore with the ele
        current_lst.append(ele)
        helper(lst, current_lst)

        # un-choose
        current_lst.pop()
        lst.append(ele)


if __name__ == '__main__':
    main()
