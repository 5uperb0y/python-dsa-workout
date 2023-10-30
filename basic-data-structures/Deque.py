"""
Design a Deque class in Python, capturing the essence of the queue data structure.
- Deque(): creates an empty deque with no input and returns an initialized empty deque as output.
- is_empty(): checks the deque's emptiness, returning a boolean value (True if empty, False otherwise).
- size(): counts the number of items within the deque, returning the total count as an integer.
- add_rear(): takes an item as input and adds it to the deque's rear without returning any output.
- add_front(): takes an item as input and adds it to the deque's front without returning any output.
- remove_rear(): removes and returns the deque's rear item, handling errors if the deque is empty.
- remove_front(): removes and returns the deque's front item, handling errors if the deque is empty.
"""
class Deque():
	def __init__(self):
		self.items = []
	def add_front(self, item):
		self.items.append(item)
	def add_rear(self, item):
		self.items.insert(0, item)
	def is_empty(self):
		return self.items == []
	def size(self):
		return len(self.items)
	def remove_front(self):
		return self.items.pop()
	def remove_rear(self):
		return self.items.pop(0)

