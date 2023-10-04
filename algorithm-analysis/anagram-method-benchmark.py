"""
Write boolean functions that will take two strings and return whether they are anagrams.
One string is an anagram of another if the second is simply a rearrangement of the first.
- two strings in question are of equal length
- strings are made up of symbols from the set of 26 lowercase alphabetic characters
"""
def anagram_checkoff(s1, s2):
	# All s1 chars must be in s2 for anagram.
	# Complexity: O(n^2) from 'in' usage.
	return all(c1 in s2 for c1 in s1)
def anagram_sorted(s1, s2):
	# Anagrams yield identical sorted strings.
	# Complexity: O(n log n) from sorting.
	return sorted(s1) == sorted(s2)
import collections
def anagram_count(s1, s2):
	# Anagrams have same char frequency.
	# Complexity: O(n) using Counter.
	return collections.Counter(s1) == collections.Counter(s2)