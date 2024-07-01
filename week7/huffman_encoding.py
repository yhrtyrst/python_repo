"""
File: huffman_encoding_ANS.py
Name:
-----------------------------------
This program demonstrates the idea of zipping/unzipping
through the algorithm of Huffman Encoding.
We will be using all of the important concepts
we learned today to complete this hugh project.
"""

from ds import Tree, PriorityQueue

# The string to be zipped/unzipped
TARGET = 'stancode sc001 sc101'


def main():
    d = build_dict()
    print('----------1----------')
    print(d)
    ############################
    priority_queue = put_key_val_to_pq(d)
    print('----------2----------')
    priority_queue.traversal_tree_elements()
    ############################
    tree = encoding_tree(priority_queue)
    print('----------3----------')
    bfs(tree)
    zipped = encoding(tree)
    print(f'{TARGET} (bits: {len(TARGET)*8}) \nEncoded: {zipped} (bits: {len(zipped)})')
    decoding(tree, zipped)


def build_dict():
    """
    :return: dict, a Python dictionary containing ch as key,
                    the number of ch occurrence as value
    """
    pass


def put_key_val_to_pq(d):
    """
    :param d : Dict[str: int], key is character and the value is its occurance
    :return : PriorityQueue, with Tuple(Tree, count) as its elements
    --------------------------------
    This function constructs a priority queue based on the chatacter occurance in d.
    """
    pass


def encoding_tree(pq):
    """
    :param pq: PriorityQueue, containing all the ch we need to encode
    :return: Tree, a binary tree that has all the ch encoded
    """
    pass


def encoding(tree):
    """
    :param tree: Tree, Huffman Tree containing the Huffman codes for characters in TARGET
    :return: str, the zipped string of TARGET
    """
    encoding_d = {}
    dfs(tree, encoding_d, '')
    print('----------4----------')
    print(encoding_d)
    
    ###############################################
    # TODO: get all the coding as a single string!
    ans = ''
    ###############################################
    return ans


def dfs(cur, encoding_d, cur_encoding):
    """
    :param cur : Tree, the pointer of current position
    :param encoding_d: Dict[str, str], holding each character as key and its Huffman code as value
    :param cur_encoding: str, the current path encoding ('0' goes left ; '1' goes right)
    """
    pass


def decoding(tree, zipped_words):
    """
    :param tree: Tree, the binary tree that contains all the ch encoded
    :param zipped_words: str, the mystery compressed binary digits to be unzipped
    """
    ans_lst = []
    add_to_ans_lst(tree, zipped_words, ans_lst, tree)
    print('--------------decoding...-----------------')
    print(''.join(ans_lst))


def add_to_ans_lst(tree, zipped_words, ans_lst, cur):
    """
    This function trace all the binaries in zipped_words down to leaves
    and add the character to ans_lst
    -------------------------------------------------
    :param tree: Tree, the binary tree that contains all the ch encoded
    :param zipped_words: str, binaries that were zipped from TARGET
    :param ans_lst: List[str], containing characters that are in leaf node
    :param cur: Tree, pointer of where the current node is
    """
    pass


#################### DO NOT EDIT THE CODES BELOW THIS LINE ####################


def bfs(tree):
    """
    :param tree: Tree, class defined in ds.py in which constructor creates objects with 
                 one value and two pointers.
    -----------------------------------------------
    This function traverses the tree and prints all elements out
    """
    queue = [tree]
    while len(queue) != 0:
        ele = queue.pop(0)
        print(ele.val, end=' | ')
        if ele.left is not None:
            queue.append(ele.left)
        if ele.right is not None:
            queue.append(ele.right)
    print('')


if __name__ == '__main__':
    main()
