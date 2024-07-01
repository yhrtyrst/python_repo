"""
File: number_of_words.py
Name:
-------------------------------
This file calculates the number of words in
romeojuliet.txt by using word.split() and
basic Python list operations
"""

FILE = 'romeojuliet.txt'


def main():
    total = 0
    with open(FILE, 'r') as f:
        for line in f:
            # 一行行 string
            token_lst = line.split()

            total += len(token_lst)
    print('Total', total)


if __name__ == '__main__':
    main()

