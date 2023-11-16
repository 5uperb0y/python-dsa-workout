"""
Implement a Doubly Linked List, in which, each node has a reference to hte next node ("next") as well as
a reference to the preceding node ("back"). The head reference also contains two references, one to the 
first node in the linked list and one to the last.
"""
class Node():
	def __init__(self, data):
		self.data = data
		self.next = None
		self.back = None
	def get_data(self):
		return self.data 
	def get_next(self):
		return self.next
	def get_back(self):
		return self.back
	def set_next(self, next_node):
		self.next = next_node
	def set_back(self, back_node):
		self.back = back_node
class DoublyLinkedList():
	def __init__(self):
		self.head = None
		self.tail = self.head
	def is_empty(self):
		return self.head is None
	def size(self):
		current = self.head
		count = 0
		while current:
			current = current.get_next()
			count = count + 1
		return count
	def add(self, item):
		new_node = Node(item)
		new_node.set_next(self.head)
		if self.is_empty():
			self.tail = new_node
		else:
			self.head.set_back(new_node)
		self.head = new_node
	def search(self, item):
		current = self.head
		while current:
			if current.get_data() == item:
				return True
			else:
				current = current.get_next()
		return False
	def remove(self, item):
		current = self.head
		while current:
			if current.get_data() == item:
				back_node = current.get_back()
				next_node = current.get_next()
				if back_node is None:
					self.head = next_node
				else:
					back_node.set_next(next_node)
				if next_node is None:
					self.tail = back_node
				else:
					next_node.set_back(back_node)
				return
			else:
				current = current.get_next()
	def append(self, item):
		new_node = Node(item)
		new_node.set_back(self.tail)
		if self.is_empty():
			self.head = new_node
		else:
			self.tail.set_next(new_node)
		self.tail = new_node
	def insert(self, pos, item):
		current = self.head
		current_pos = 0
		while current:
			if current_pos == pos:
				new_node = Node(item)
				new_node.set_next(current)
				if current.get_back() is None:
					self.head = new_node
				else:
					current.get_back().set_next(new_node)
					new_node.set_back(current.get_back())
				current.set_back(new_node)
				return
			else:
				current_pos = current_pos + 1
				current = current.get_next()
	def pop(self, pos = None):
		if pos is None:
			pop_item = self.tail.get_data()
			if self.size == 1:
				self.tail = None
				self.head = None
			else:
				self.tail = self.tail.get_back()
				self.tail.set_next(None)
			return pop_item
		else:
			current = self.head
			current_pos = 0
			while current:
				if current_pos == pos:
					pop_item = current.get_data()
					back_node = current.get_back()
					next_node = current.get_next()
					if back_node is None:
						self.head = next_node
					else:
						back_node.set_next(next_node)
					if next_node is None:
						self.tail = back_node
					else:
						next_node.set_back(back_node)
					return pop_item
				else:
					current_pos = current_pos + 1
					current = current.get_next()

	def __iter__(self):
		current = self.head
		while current:
			yield current.data
			current = current.next
	def __repr__(self):
		return "[" + ", ".join(map(str, self)) + "]"