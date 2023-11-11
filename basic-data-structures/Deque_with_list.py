"""
Implement a Deque using linked lists
"""
from UnorderedList import UnorderedList
class Deque():
	def __init__(self):
		self.items = UnorderedList()
	def add_front(self, item):
		self.items.append(item)
	def add_rear(self, item):
		self.items.add(item)
	def is_empty(self)
		return self.items.is_empty()
	def size(self):
		return self.items.size()
	def remove_front(self):
		return self.items.pop()
	def remove_rear(self):
		return self.items.pop(0)
