"""
Write a function that uses Deques to determine whether a string is a palindrome.
(A palindrome is a string that reads the same forward and backward, for example, *radar* and *toot*.)
"""
from Deque import Deque
def is_palindrome(word):
	chars = Deque()
	for char in word:
		chars.add_front(char)
	while chars.size() > 1:
		if chars.remove_front() != chars.remove_rear():
			return False
	return True