"""
File: student_info_dict.py
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info
"""


# The file name of our target text file
FILE = 'romeojuliet.txt'

# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'


def main():
	word_count = {}
	with open(FILE, 'r') as f:
		for line in f:
			tokens_list = line.split()
			for token in tokens_list:
				# case-insensitive
				# remove punctuation
				token = string_manipulation(token)
				if token not in word_count:
					word_count[token] = 1
				else:
					word_count[token] += 1
	print_out_d(word_count)


def print_out_d(d):
	"""
	: param d: (dict) key of type str is a word
					value of type int is the word occurrence
	---------------------------------------------------------------
	This method prints out all the info in d
	"""
	for key, value in sorted(d.items(), key=lambda ele: ele[1]):  # value sorted
						#[('romeo',57),('the',75),...]
		print(key, '->', value)


def string_manipulation(string_line):
	string_line = string_line.lower()
	ans = ''
	for ch in string_line:
		if ch.isalpha() or ch.isdigit():
			ans += ch
	return ans


if __name__ == '__main__':
	main()
