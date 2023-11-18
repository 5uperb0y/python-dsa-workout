"""
Convert an integer to a string in some base between binary and hexadecimal by using recursion
"""
def to_str(n, base):
	digit = "0123456789ABCDEF"
	if n < base:
		return digit[n]
	else:
		return f"{to_str(n//base, base)}{digit[n%base]}"