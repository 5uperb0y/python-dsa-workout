"""
Create a list of n numbers starting with 0 using the following methods,
- concatenation: use a for loop and create the list by concatenation 
- appendation: use a for loop and create the list by appendation
- comprehension: create the list using list comprehension
- range function: use the range function wrapped by a call to the list constructor
Example:
	Time required for each list creation method (run 10,000 times):
	create_list_concatenation: 0.4964 seconds
	create_list_appendation: 0.3381 seconds
	create_list_comprehension: 0.1829 seconds
	create_list_range: 0.0841 seconds
"""
import timeit
def create_list_concatenation(n):
	l = []
	for i in range(n):
		l += [i]
	return l
def create_list_appendation(n):
	l = []
	for i in range(n):
		l.append(i)
	return l
def create_list_comprehension(n):
	return [i for i in range(n)]
def create_list_range(n):
	return list(range(n))
def measure_time(func_name, n=1000, num_executions=10000):
    exec_time = timeit.timeit(f"{func_name}({n})", globals=globals(), number=num_executions)
    print(f"{func_name}: {exec_time:.4f} seconds")
def measure_time(func, n = 1000, rep = 10000):
	t = timeit.Timer(f"{func}({n})", f"from __main__ import {func_name}")
	print(f"{func}: {t.timeit(number = rep):.4f} seconds")
if __name__ == "__main__":
	print("Time required for each list creation method (run 10,000 times):")
	for func_name in ["create_list_concatenation", "create_list_appendation", "create_list_comprehension", "create_list_range"]:
		measure_time(func_name)