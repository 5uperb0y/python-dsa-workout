"""
Design an Unordered List class in Python, capturing the essence of the list data structure.
- UnorderedList(): creates an empty list. No parameters needed. Returns the empty list.
- is_empty(): checks whether the list is empty and returns a boolean.
- add(item): adds a new and unique item to the list. It needs the item and returns nothing. Assume the item is not already in the list.
- search(item): searches for the item in the list and returns a boolean.
- size(): counts the number of items within the queue, returning the total count as an integer.
- index(item): returns the position of item in the list. It needs the item and returns the index.  Assume the item is in the list.
- remove(item): removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
- append(item): adds a new and unique item to the end of the list.
- insert(pos,item): adds a new item to the list at position pos. It needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.
- pop(): removes and returns the last item in the list. It needs nothing and returns an item.  Assume the list has at least one item.
- pop(pos): removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.
"""
class Node():
	def __init__(self, data):
		self.data = data
		self.next = None
class UnorderedList():
	def __init__(self):
		self.head = None
	def is_empty(self):
		return self.head is None
	def add(self, item):
		current = Node(item)
		current.next = self.head
		self.head = current
	def size(self):
		count = 0
		current = self.head
		while current:
			current = current.next
			count = count + 1
		return count
	def search(self, item):
		current = self.head
		while current:
			if current.data == item:
				return True
			else:
				current = current.next
		return False
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
	def index(self, item):
		pos = 0
		current = self.head
		while current:
			if current.data == item:
				return pos
			current = current.next
			pos = pos + 1
		return False
	def append(self, item):
		if self.is_empty():
			self.head = Node(item)
		else:
			current = self.head
			while current.next is not None:
				current = current.next
			current.next = Node(item)
	def insert(self, pos, item):
		current = self.head
		current_pos = 0
		previous = None
		while current:
			if current_pos == pos:
				if previous is None:
					self.head = Node(item)
					self.head.next = current
				else:
					previous.next = Node(item)
					previous.next.next = current
			previous = current
			current = current.next
			current_pos = current_pos + 1
	def pop(self, pos = None):
		current = self.head
		current_pos = 0
		previous = None
		if self.is_empty():
			raise Exception("pop from empty stack")
		else:
			pop_item = current.data
			if self.size() == 1:
				self.head == None
			else:
				while current.next is not None:
					if current_pos == pos:
						if previous is None:
							self.head = None
						else:
							previous.next = current.next
						return current.data
					previous = current
					current = current.next
					current_pos = current_pos + 1
				previous.next = current.next
			return pop_item
	def __iter__(self):
		current = self.head
		while current:
			yield current.data
			current = current.next
	def __repr__(self):
		return " -> ".join(map(str, self))