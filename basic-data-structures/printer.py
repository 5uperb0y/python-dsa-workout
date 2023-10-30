"""
"""
from Queue import Queue
import datetime as date
class Task():
	def __init__(self, page):
		self.create_time = date.now()
		self.wait_time = int()
		self.page = page
	def waiting_time(self, current_time):
		self.wait_time = current_time - self.create_time
class Printer():
	def __init__(self, ppm):
		self.ppm = ppm
		self.tasks = Queue()
	def submit(self, page):
		self.tasks.enqueue(Task(page))
	def is_busy(self):
		return not self.tasks.is_empty()