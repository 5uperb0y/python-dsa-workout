"""
To implement the length method, we counted the number of nodes in the list.  An alternative strategy
would be to store the number of nodes in the list as an additional piece of data in the head of the list.
Modify the UnorderedList class to include this information and rewrite the length method.
"""
class Node():
	def __init__(self, data):
		self.data = data
		self.next = None
class UnorderedList():
	def __init__(self):
		self.head = None
		self.len = 0
	def is_empty(self):
		return self.head is None
	def add(self, item):
		current = Node(item)
		current.next = self.head
		self.head = current
		self.len = self.len + 1
	def remove(self, item):
		current = self.head
		previous = None
		while current:
			if current.data == item:
				if previous is None:
					self.head = current.next
				else:
					previous.next = current.next
				self.len = self.len - 1
				return
			else:
				previous = current
				current = current.next
	def append(self, item):
		if self.is_empty():
			self.head = Node(item)
		else:
			current = self.head
			while current.next is not None:
				current = current.next
			current.next = Node(item)
		self.len = self.len + 1
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
				self.len = self.len + 1
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
				self.head = None
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
			self.len = self.len - 1
			return pop_item
	def size(self):
		return self.len
a = UnorderedList()
a.add("a")
print(a.size())
a.pop()
print(a.size())