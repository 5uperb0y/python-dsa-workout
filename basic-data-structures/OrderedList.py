"""
Design an Ordered List class in Python, capturing the essence of the list data structure.
- List(): creates an empty list. No parameters needed. Returns the empty list.
- is_empty(): checks whether the list is empty and returns a boolean.
- add(item): adds a new and unique item to the list making sure that the order is preserved. It needs the item and returns nothing. Assume the item is not already in the list.
- search(item): searches for the item in the list and returns a boolean.
- size(): counts the number of items within the queue, returning the total count as an integer.
- remove(item): removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
- pop(): removes and returns the last item in the list. It needs nothing and returns an item.  Assume the list has at least one item.
"""
class Node():
	def __init__(self, init_data):
		self.data = init_data
		self.next = None
class OrderedList():
	def __init__(self):
		self.head = None
	def is_empty(self):
		return self.head is None
	def size(self):
		current = self.head
		count = 0
		while current:
			current = current.next
			count = count + 1
		return count
	def remove(self, item):
		current = self.head
		previous = None
		while current:
			if current.data == item:
				if previous is None:
					self.head = current.next
				else:
					previous.next = current.next
				return
			else:
				previous = current
				current = current.next
	def search(self, item):
		current = self.head
		while current:
			if current.data == item:
				return True
			elif current.data > item:
				return False
			else:
				current = current.next
		return False
	def pop(self):
		current = self.head
		previous = None
		while current:
			if current.next is None:
				if previous is None:
					self.head = None
				else:
					previous.next = None
				return current.data
			else:
				previous = current
				current = current.next
	def add(self, item):
		added_node = Node(item)
		if self.is_empty():
			self.head = added_node
		else:
			previous = None
			current = self.head
			while current and current.data < item:
				previous = current
				current = current.next
			if previous is None:
				added_node.next = current
				self.head = added_node
			else:
				previous.next = added_node
				added_node.next = current
	def __iter__(self):
		current = self.head
		while current:
			yield current.data
			current = current.next
	def __repr__(self):
		return " -> ".join(map(str, self))