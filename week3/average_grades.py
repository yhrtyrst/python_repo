"""
File: average_grades.py
Name: Blair
-------------------------
This file stores all the scores
in a python list and calculates the
average of all elements in it
"""

# Constant
EXIT = -1  # Controls when to break the loop of score input


def main():
	"""
	This program asks inputs from users 
	"""
	print(f"This program averages the input(s), or {EXIT} to exit")
	
	lst = []

	while True:
		score = int(input('Score: '))
		if score == EXIT:
			break
		lst.append(score)
	
	print('The average:', average_by_index(lst))
	print('The average:', average_by_for_each(lst))


def average_by_index(scores):  # 適用於有 index 的data type
	"""
	:param scores: (list) Containing all the scores input by user
	:return : (float) The average of the elements in scores
	----------------------------------------------
	This function uses indices in for loop to calculate
	the average of scores
	"""
	l_l = len(scores)
	total = 0
	for i in range(l_l):
		total += scores[i]
	return total/l_l


def average_by_for_each(scores):
	"""
	:param scores: (list) Containing all the scores input by user
	:return : (float) The average of the elements in scores7
	----------------------------------------------
	This function uses for each loop to calculate
	the average of scores
	"""
	total = 0
	for score in scores:
		total += score
	return total/len(scores)


if __name__ == '__main__':
	main()
