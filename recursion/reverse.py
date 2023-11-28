"""
Write a function that takes a string as a parameter and returns a new string that is the reverse of
the old string.
"""
def reverse(s):
	if len(s) == 1:
		return s
	else:
		return f"{s[-1]}{reverse(s[:-1])}"