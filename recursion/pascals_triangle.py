"""
Write a program that prints out Pascal’s triangle. Your program should accept a parameter
that tells how many rows of the triangle to print.
"""
def pascals_triangle(n):
	if n == 1:
		return [[0, 1, 0]]
	else:
		o = pascals_triangle(n - 1)
		n = [0] + [o[-1][e] + o[-1][e + 1] for e in range(len(o[-1]) - 1)] + [0]
		o.append(n)
		return o
a = pascals_triangle(5)
for r in a:
	print(r)
