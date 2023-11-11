"""
Implement a stack using linked lists
"""
from UnorderedList import UnorderedList
class Stack():
	def __init__(self):
		self.items = UnorderedList()
	def is_empty(self):
		return self.items.is_empty()
	def size(self):
		return self.items.size()
	def push(self, item):
		self.items.add(item)
	def pop(self):
		return self.items.pop(0)
	def peek(self):
		if self.is_empty():
			raise Exception("the stack is empty")
		else:
			return self.items.head.data