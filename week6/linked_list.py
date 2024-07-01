"""
File: linked_list.py
Name: 
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""


class ListNode:
	def __init__(self, data, pointer):
		self.val = data
		self.next = pointer # 8 byte


def main():
	# node3 = ListNode(('C',7), None)
	# node2 = ListNode(('B', 5), node3)
	# node1 = ListNode(('A', 3), node2) #obj存address
	# linked_list = node1

	node1 = ListNode(('A', 3), None)
	node2 = ListNode(('B', 3), None)
	node3 = ListNode(('C', 7), None)
	node1.next = node2
	node2.next = node3
	priority_queue = node1  # linked_list
	print(f"node1:{node1}, node2:{node2}, node3:{node3}")
	print('--------------------------------')
	traversal(priority_queue)


def traversal(priority_queue):
	"""
	:param priority_queue: ListNode, holding the first ListNode object
						   as the start of priority queue
	--------------------------
	This function prints out each val of a linked list
	"""
	cur = priority_queue
	# while cur.next is not None:
	# 	print(cur.val)
	# 	cur = cur.next
	# print(cur.val)
	while cur is not None:
		print(cur.val)
		cur = cur.next


if __name__ == '__main__':
	main()
