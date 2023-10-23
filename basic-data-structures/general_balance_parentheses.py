"""
Given a string composed of different types of brackets (parentheses (), square brackets [], and curly braces {}), determine if the string is balanced.
A string is balanced if:
- Each opening bracket has a corresponding closing bracket.
- The types of brackets match in the correct order.
Example:
	Balanced:
	- { { ( [ ] [ ] ) } ( ) }
	- [ [ { { ( ( ) ) } } ] ]
	- [ ] [ ] [ ] ( ) { }
	Unbalanced:
	- ( [ ) ]
	- ( ( ( ) ] ) )
	- [ { ( ) ]
Write a function to check if the given string is balanced.
"""
from Stack import Stack
def is_balanced(s):
	brackets = Stack()
	mapping =  {")": "(", "]": "[","}": "{" }
	for c in s:
		if c in mapping.values():
			brackets.push(c)
		elif c in mapping.keys():
			if brackets.pop() != mapping[c]:
				return False
	return brackets.is_empty()