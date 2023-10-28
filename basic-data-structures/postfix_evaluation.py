"""
Write a function to evaluate an expression is already in postfix notation
"""
from Stack import Stack
import operator
def evaluate_postfix(exp):
	s = Stack()
	opers = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv }
	for i in exp.split():
		if i.isdigit():
			s.push(float(i))
		else:
			# # Pop operands in reverse order because it's a stack
			operand2, operand1 = s.pop(), s.pop()
			s.push(opers[i](operand1, operand2))
	return s.pop()