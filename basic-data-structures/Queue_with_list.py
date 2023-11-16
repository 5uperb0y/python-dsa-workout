"""
Implement a Queue using linked lists.
"""
from UnorderedList import UnorderedList
class Queue():
	def __init__(self):
		self.items = UnorderedList()
	def is_empty(self):
		return self.is_empty()
	def size(self):
		return self.items.size()
	def enqueue(self, item):
		self.items.add(item)
	def dequeue(self):
		return self.items.pop()