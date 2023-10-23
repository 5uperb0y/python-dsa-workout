"""
Determine if a given string of parentheses is balanced.
A string is considered balanced if:
- Every opening '(' has a corresponding closing ')'.
- Parentheses are properly nested.
Examples:
    Balanced: 
    - (()()()())
    - (((())))
    - (()((())()))
    Un-balanced: 
    - ((((((())
    - ())
    - (()()(()
Write a function to read the string of parentheses from left to right and decide if they're balanced.
Edge Cases:
- Empty string: should return True (nothing is unbalanced).
- Without closing: e.g. "((("
- Without opening: e.g. ")))"
- Mixed without pairing: e.g. ")("
"""
from Stack import Stack
def is_balance(s):
	parens = Stack()
	for c in s:
		if c == "(":
			parens.push(c)
		elif c == ")" and parens.is_empty():
			return False
		elif c == ")":
			parens.pop()
	return parens.is_empty()