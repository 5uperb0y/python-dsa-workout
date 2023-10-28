"""
Write a function to convert infix expression to postfix expression
- infix expression needs parenthesis to indicates precedence level A * ( B + C )
- prefix expression: * A + B C
- postfix expression: A B C + *

Algorithm:
1. Create a stack for operators and an output list.
2. Use the stack for operators and parentheses, appending operands and higher-precedence operators to output.
3. Append remaining operators from stack to output.
4. Manage parentheses: push left ones to stack and pop until a left one appears when a right one is encountered, appending operators but not parentheses.
"""
from Stack import Stack
def infix_to_postfix(exp):
	s = Stack()
	out = []
	# Operator precedence mapping
	opers = { "*": 1, "/": 1, "+": 0, "-": 0}
	for i in exp.split():
		if i in opers:
			# Use get() to prevent errors from unrecognized operators
			while not s.is_empty() and opers.get(s.peek(), -1) >= opers[i]:
				out.append(s.pop())
			s.push(i)
		elif i == "(":
			s.push(i)
		elif i == ")":
			while not s.is_empty() and s.peek() != "(":
				out.append(s.pop())
			s.pop()
		else:
			out.append(i)
	while not s.is_empty():
		out.append(s.pop())
	return " ".join(out)
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))