"""
After creating a Stack class, write a function rev_string(my_str) that uses a stack to reverse the characters in a string.
"""
import Stack
def rev_string(string):
	chars = Stack()
	for char in string:
		chars.push(char)
	return "".join(chars.pop() for _ in range(chars.size()))