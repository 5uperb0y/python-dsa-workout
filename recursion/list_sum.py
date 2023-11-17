"""
Get the total sum of numbers in a list by using recusion method.
"""
def list_sum(nums):
	if len(nums) == 1:
		return nums[0] 
	else:
		mid = len(nums)//2
		return list_sum(nums[:mid]) + list_sum(nums[mid:])