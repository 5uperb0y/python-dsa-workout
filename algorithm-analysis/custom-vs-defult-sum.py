"""
Benchmarking comparison between custom sum and built-in sum functions
This script demonstrates how to perform benchmark tests using two different modules, `timeit` and `time`.
Example: 
	Time for custom sum: 0.237206302001141 seconds
	Time for built-in sum: 0.048756201002106536 seconds
	Time for custom sum: 0.23102545738220215 seconds
	Time for built-in sum: 0.04398012161254883 seconds
"""
# functions to compare
def mysum(nums):
	"""Custom sum function using a for loop"""
	result = 0
	for n in nums:
		result += n
	return result
def pysum(nums):
	"""Built-in sum function"""
	return sum(nums)
# generate a list of numbers
large_numbers = list(range(10000))
# Benchmarking with `timeit` module 
import timeit
custom_time = timeit.timeit("mysum(large_numbers)", globals = globals(), number = 1000)
print(f"Time for custom sum: {custom_time} seconds")
built_in_time = timeit.timeit("pysum(large_numbers)", globals = globals(), number = 1000)
print(f"Time for built-in sum: {built_in_time} seconds")
# Benchmarking with `time` module
import time
start_time = time.time()
[mysum(large_numbers) for _ in range(1000)]
end_time = time.time()
print(f"Time for custom sum: {(end_time - start_time)} seconds")
start_time = time.time()
[pysum(large_numbers) for _ in range(1000)]
end_time = time.time()
print(f"Time for built-in sum: {(end_time - start_time)} seconds")