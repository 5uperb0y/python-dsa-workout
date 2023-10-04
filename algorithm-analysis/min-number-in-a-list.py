"""
Write two Python functions to find the minimum number in a list.
The first function should compare each number to every other number on the list. O(n^2).
The second function should be linear O(n).
"""
def min_quadratic(nums):
	"""fuction with quadratic O(n^2)"""
	for n1 in nums:
		# check if the current number is smaller than or equal to all other numbers in the list.
		is_min = all(n1 <= n2 for n2 in nums)
		if is_min:
			return n1
def min_linear(nums):
	"""function with linear O(n)"""
	min_number = nums[0]
	for n in nums[1:]:
		if min_number > n:
			min_number = n
	return min_number