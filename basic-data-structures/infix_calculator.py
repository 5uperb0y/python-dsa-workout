"""
Design an infix calculator
1. Modify the infix-to-postfix algorithm so that it can handle errors.
2. Modify the postfix evaluation algorithm so that it can handle errors.
3. Implement a direct infix evaluator that combines the functionality of infix-to-postfix conversion
   and the postfix evaluation algorithm.  Your evaluator should process infix tokens from left to right
   and use two stacks, one for operators and one for operands, to perform the evaluation.
4. Turn your direct infix evaluator from the previous problem into a calculator.
"""
# importing "readline" module to enable retrieving previous commands with the up arrow key
import readline
import operator
from Stack import Stack
from general_balance_parentheses import is_balanced
def is_prior(op1, op2):
	rank = {"*": 2, "/": 2, "^": 2, "+": 1, "-": 1, "(": 0}
	return rank[op1] >= rank[op2] 
def infix_to_postfix(expr):
	if not is_balanced(expr):
		raise Exception("the expression is not balanced")
	else:
		elems = expr.split()
		opers = Stack()
		out = []
	for e in elems:
		if e.isdigit():
			out.append(e)
		elif e in "+-*/^(":
			while not opers.is_empty() and is_prior(opers.peek(), e) and e != "(":
				out.append(opers.pop())
			opers.push(e)
		elif e == ")":
			while opers.peek() != "(":
				out.append(opers.pop())
			# remove "(" from the operator stack
			opers.pop()
		else:
			raise Exception(f"unvalid element: {e}")
	while not opers.is_empty():
		out.append(opers.pop())
	return " ".join(out)
def postfix_evaluator(expr):
	elems = expr.split()
	terms = Stack()
	methods = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "^": operator.pow }
	for e in elems:
		if e.isdigit():
			terms.push(float(e))
		elif e in "+-*/^":
			term1, term2 = terms.pop(), terms.pop()
			terms.push(methods[e](term2, term1))
		else:
			raise Exception(f"unvalid ement: {e}")
	return terms.pop()
def infix_evaluator():
	print("Enter exit() to exit the calculator")
	while True:
		expr = input()
		if expr == "exit()":
			return
		else:
			print(postfix_evaluator(infix_to_postfix(expr)))
infix_evaluator()