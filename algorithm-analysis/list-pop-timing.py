"""
Verify the performance of the pop operation on a list of a known size,
1) Popping from the list's end (O(1)).
2) Popping from the list's start (O(n)).
Measure times for lists of varying sizes. Expect constant time for end pops, but increasing time for start pops.
Example:
	size    pop_start        pop_end
	10      0.00000040       0.00000130
	100     0.00000030       0.00000040
	1000    0.00000040       0.00000050
	10000   0.00000320       0.00000050
	100000  0.00007130       0.00000120
	1000000 0.00098660       0.00000120
	10000000        0.01007550       0.00000100
"""
import timeit
def measure_pop_time(n):
	l = list(range(n))
	pop_end_timer = timeit.Timer("l.pop()", globals = locals())
	pop_start_timer = timeit.Timer("l.pop(0)", globals = locals())
	return pop_end_timer.timeit(number = 1), pop_start_timer.timeit(number = 1)
if __name__ == "__main__":
	print("size\tpop_start\t pop_end")
	for size in (10**e for e in range(1, 8)):
		pop_end_time, pop_start_time = measure_pop_time(size)
		print(f"{size}\t{pop_start_time:.8f}\t {pop_end_time:.8f}")