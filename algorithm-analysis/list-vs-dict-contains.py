"""
Compare the performance of the contains operation between lists and dictionaries.
Expect constant time O(1) for dictionaries (O(1)), but increasing time O(n) for lists.
Example:
	# Amplify the execution time readability by performing 1,000 repetitions.
	element list contains   dict contains
	0       0.00003190      0.00003670
	10000   0.04292619      0.00003420
	20000   0.08161509      0.00003100
	30000   0.12125548      0.00003110
	40000   0.16572067      0.00003180
	50000   0.24346315      0.00003460
	60000   0.25293495      0.00003050
	70000   0.27636345      0.00002880
	80000   0.32097874      0.00003620
	90000   0.40013075      0.00003140
"""
import timeit
def measure_contains_time(element, size, rep):
	# Ordered numbers in the list serve as positions for the lookup.
	l = list(range(size))
	d = {k: v for k, v in enumerate(l)}
	l_timer = timeit.Timer(f"{element} in l", globals = locals())
	d_timer = timeit.Timer(f"{element} in d", globals = locals())
	l_time = l_timer.timeit(number = rep)
	d_time = d_timer.timeit(number = rep)
	return l_time, d_time
if __name__ == "__main__":
	size = 100000
	rep = 1000
	print("# Amplify the execution time readability by performing 1,000 repetitions.")
	print("element\tlist contains\tdict contains")
	for element in range(0, size, size//10):
		l_time, d_time  = measure_contains_time(element, size, rep)
		print(f"{element}\t{l_time:.8f}\t{d_time:.8f}")