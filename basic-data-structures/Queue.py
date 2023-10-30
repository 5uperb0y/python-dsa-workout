"""
Design a Queue class in Python, capturing the essence of the queue data structure.
- Queue(): creates an empty queue with no input and returns an initialized empty queue as output.
- is_empty(): checks the queue's emptiness, returning a boolean value (True if empty, False otherwise).
- size(): counts the number of items within the queue, returning the total count as an integer.
- enqueue(): takes an item as input and adds it to the queue's rear without returning any output.
- dequeue(): removes and returns the queue's front item, handling errors if the queue is empty.
"""
class Queue():
	def __init__(self):
		self.items = []
	def is_empty(self):
		return self.items == []
	def size(self):
		return len(self.items)
	def enqueue(self, item):
		return self.items.insert(0, item)
	def dequeue(self):
		return self.items.pop()