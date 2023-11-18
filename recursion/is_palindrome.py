"""
Write a function that takes a string as a parameter and returns True if the string is a palindrome,
False otherwise.
"""
from reverse import reverse 
def is_palindrome(s):
	return s == reverse(s)