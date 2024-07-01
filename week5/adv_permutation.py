"""
File: adv_permutation.py
Name: Blair
------------------------------
This program finds all the permutations [1, 2, 3].
To complete this task, you will need backtracking
-- choose, explore, and un-choose
"""


def main():
	permutation([1, 2, 3])


def permutation(lst):
	length = len(lst)
	lst_empty = []
	return permutation_helper(lst, lst_empty, length)


def permutation_helper(lst, current_lst, ans_len):
	if len(current_lst) == ans_len:
		print(current_lst)
	else:
		for num in lst:
			if num in current_lst:
				pass
			else:
				# choose
				current_lst.append(num)
				# explore
				permutation_helper(lst, current_lst, len(lst))
				# un-choose stack
				current_lst.pop()




if __name__ == '__main__':
	main()