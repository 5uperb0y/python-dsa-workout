"""
Devise an experiment to verify that the list index operator is O(1).
Example:
	# Measure time to access middle element in lists of varying sizes.
	List size       Time (seconds)
	10      7.999999525054591e-07
	100     9.000000318337698e-07
	1000    7.999999525054591e-07
	10000   7.000001005508238e-07
	100000  2.300000005561742e-06
	1000000 1.8999999156221747e-06
	# Measure time to access element at different positions in a fixed-size list
	Position        Time (seconds)
	1       4.999999418942025e-07
	1001    4.0000008993956726e-07
	2001    1.999999312829459e-07
	3001    3.000000106112566e-07
	4001    3.000000106112566e-07
	5001    3.000000106112566e-07
	6001    3.000000106112566e-07
	7001    3.999998625658918e-07
	8001    1.999999312829459e-07
	9001    3.000000106112566e-07
"""
import timeit
print("# Measure time to access middle element in lists of varying sizes.")
print(f"List size\tTime (seconds)")
for size in [10**e for e in range(1,7)]:
	l = list(range(size))
	timer = timeit.Timer("l[len(l)//2]", globals = globals())
	t = timer.timeit(number = 1)
	print(f"{size}\t{t}")
print("# Measure time to access element at different positions in a fixed-size list")
print(f"Position\tTime (seconds)")
for pos in range(1, 10000, 1000):
	l = list(range(10000))
	timer = timeit.Timer(f"{l[pos]}", globals = globals())
	t = timer.timeit(number = 1)
	print(f"{pos}\t{t}")