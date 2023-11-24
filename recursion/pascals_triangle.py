"""
Write a program that prints out Pascal’s triangle. Your program should accept a parameter
that tells how many rows of the triangle to print.
"""
def pascals_triangle(n):
	if n == 1:
		return [[1]]
	else:
		triangle = pascals_triangle(n - 1)
		last_row = triangle[-1]
		new_row = [1]
		for i in range(len(last_row) - 1):
			new_row.append(last_row[i] + last_row[i + 1])
		new_row.append(1)
		triangle.append(new_row)
		return triangle