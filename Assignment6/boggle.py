"""
File: boggle.py
Name: Blair
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    TODO:
    """
    start = time.time()
    ####################
    word_lst = []
    for i in range(1, 5):
        row = input(f' {i} row of letters: ')
        if check_row(row):
            word_lst.append(row.lower().split(' '))
        else:
            print('Illegal input')
            break
    find_word(word_lst)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(word_lst):
    dict_lst = read_dictionary()
    ans = []
    m, n = len(word_lst), len(word_lst[0])
    for i in range(m):
        for j in range(n):
            start_point = word_lst[i][j]
            path = [(i, j)]
            find_helper(word_lst, i, j, path, start_point, ans, dict_lst)
    print(f'There are {len(ans)} words in total.')


def find_helper(word_lst, cur_i, cur_j, path, word, ans, dict_lst):
    if len(word) >= 4:
        if word in dict_lst and word not in ans:
            ans.append(word)
            print(f'Found {word}')
    for i in range(-1, 2):
        for j in range(-1, 2):
            next_i = cur_i + i
            next_j = cur_j + j
            if len(word_lst[0]) > next_i >= 0 and len(word_lst[0]) > next_j >= 0:
                if (next_i, next_j) not in path:
                    word += word_lst[next_i][next_j]
                    path.append((next_i, next_j))
                    if has_prefix(word, dict_lst):
                        find_helper(word_lst, next_i, next_j, path, word, ans, dict_lst)
                    path.pop()
                    word = word[:-1]
    """
    (i-1, j-1)   (i, j-1)    (i+1, j-1)
    (i-1, j)     (i, j)
    (i-1, j+1)
    
    """


def check_row(s: str) -> bool:
    if s[-1].isspace():
        return False
    for i in range(len(s)):
        if i % 2 == 0:
            if not s[i].isalpha():
                return False
        else:
            if not s[i].isspace():
                return False
    return True


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    :return: (list) vocabulary List
    """
    dict_lst = []
    with open(FILE, 'r') as f:
        for line in f:
            dict_lst.append(line.strip())
    return dict_lst


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :param dictionary: (list) vocabulary List
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
