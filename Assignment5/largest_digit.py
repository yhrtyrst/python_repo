"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int to fin largest digit
	:return: int, largest_digit
	"""
	find_max = 0
	result = find_largest_digit_helper(n, find_max)
	return result


def find_largest_digit_helper(n, find_max):
	if n < 0:
		n = -n
	if n % 10 == 0:
		return find_max
	else:
		a = n % 10
		if a > find_max:
			find_max = a
		return find_largest_digit_helper((n - a) // 10, find_max)


if __name__ == '__main__':
	main()
