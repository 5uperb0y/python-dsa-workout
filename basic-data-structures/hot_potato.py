"""
Write a function that takes a list of names and a constant (call it “num” to be used for counting) as inputs.
It will return the name of the last person remaining after repetitive counting by num.
"""
from Queue import Queue
def hot_potato(names, num):
	q = Queue()
	# fill items into a queue
	for n in names:
		q.enqueue(n)
	while q.size() > 1:
		for _ in range(num):
			q.enqueue(q.dequeue())
		q.dequeue()
	return q.dequeue()