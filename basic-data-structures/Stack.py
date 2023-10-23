"""
Design a Stack class in Python, capturing the essence of the stack data structure.
- Stack(): creates an empty stack with no input and returns an initialized empty stack as output.
- push(item): takes an item as input and adds it to the stack's top without returning any output.
- pop(): removes and returns the stack's topmost item, handling errors if the stack is empty.
- peek(): provides the stack's top item without removal, returning a message if the stack is empty.
- is_empty(): checks the stack's emptiness, returning a boolean value (True if empty, False otherwise).
- size(): counts the number of items within the stack, returning the total count as an integer.
"""
class Stack():
	def __init__(self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		try:
			return self.items.pop()
		except IndexError:
			print("pop from empty stack")
	def peek(self):
		try:
			return self.items[-1]
		except IndexError:
			print("the stack is empty")
	def is_empty(self):
		return self.items == []
	def size(self):
		return len(self.items)