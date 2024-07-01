"""
File: anagram.py
Name: Blair
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

dict_lst = []  # a dictionary


def main():
    """
    TODO:
    """
    start = time.time()
    ####################
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')

    while True:
        word = input('Find anagrams for: ')
        if word == EXIT:
            break
        else:
            find_anagrams(word)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    global dict_lst
    with open(FILE, 'r') as f:
        for line in f:
            dict_lst.append(line.strip())


def find_anagrams(s):
    """
    :param s: string to find anagrams
    :return:
    """
    read_dictionary()
    s_len = len(s)
    empty_s = ''
    output = []
    index_lst = []
    print('Searching...')
    find_anagrams_helper(s, empty_s, s_len, output, index_lst)
    print(f'{len(output)} anagrams: {output}')


def find_anagrams_helper(s, current_s, s_len, output, index_lst):
    global dict_lst
    if len(current_s) == len(s):
        if current_s in dict_lst:
            if current_s in output:
                pass
            else:
                print(f'Found: {current_s}')
                print('Searching...')
                output.append(current_s)
                return
    else:
        for i in range(s_len):
            if s[i] in current_s and i in index_lst:
                pass
            else:
                current_s += s[i]
                index_lst.append(i)
                if has_prefix(current_s):
                    find_anagrams_helper(s, current_s, s_len, output, index_lst)
                    current_s = current_s[:-1]
                    index_lst.pop()
                else:
                    current_s = current_s[:-1]
                    index_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: string
    :return: boolean
    """
    global dict_lst
    # start = sub_s[:1]
    for word in dict_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
