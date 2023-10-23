from Stack import Stack
"""
Convert decimal numbers to binary and to any base up to 16.
"""
def decimal_to_binary(num):
	s = Stack()
	while num >= 1:
		s.push(num % 2)
		num = num//2
	return "".join(str(s.pop()) for _ in range(s.size()))
def decimal_to_base(num, base):
	# Digits to represent numbers in bases greater than 10
	digits="0123456789ABCDEF"
	s = Stack()
	while num >= 1:
		s.push(num % base)
		num = num//base
	# Map the remainders to their notation in the specified base and reassemble the number
	return "".join(digits[s.pop()] for _ in range(s.size()))