"""
Write a program that solves the following problem:
Three missionaries and three cannibals come to a river and find a boat that holds two people.
Everyone must get across the river to continue on the journey. However, if the cannibals ever
outnumber the missionaries on either bank, the missionaries will be eaten. Find a series of
crossings that will get everyone safely to the other side of the river.
Algorithm:
1. list all potential method to cross the river
2. check if the method valid
	1) the method is safe
	2) the method has not been used (to prevent infinitive loop)
3. try all methods
4. if any method achieves the goal (safely transports missionaries and cannibals), 
   return the crossing history
5. if no valid methods remains, return fail (the problem has no solution)
"""
def is_safe(m, c):
	return (m >= c) or (m * c == 0)
def generate_crossings(M, C, load):
	return [
		(m, c) for m in range(0, M + 1)
		for c in range(0, C + 1)
		if (m > 0 or c > 0) and m + c <= load 
	]
def cross_river(lm, lc, rm, rc, side, history, load):
	if lm == 0 and lc == 0:
		return history
	else:
		if side == "left":
			crossings = generate_crossings(lm, lc, load)
			for m, c in crossings:
				nlm, nlc = lm - m, lc - c
				nrm, nrc = rm + m, rc + c
				current = (nlm, nlc, nrm, nrc, "right")
				if is_safe(nlm, nlc) and is_safe(nrm, nrc) and current not in history:
					history.append(current)
					solution = cross_river(*current, history, load)
					if solution:
						return solution
					else:
						history.pop()
				else:
					pass
		elif side == "right":
			crossings = generate_crossings(rm, rc, load)
			for m, c in crossings:
				nlm, nlc = lm + m, lc + c
				nrm, nrc = rm - m, rc - c
				current = (nlm, nlc, nrm, nrc, "left")
				if is_safe(nlm, nlc) and is_safe(nrm, nrc) and current not in history:
					history.append(current)
					solution = cross_river(*current, history, load)
					if solution:
						return solution
					else:
						history.pop()
				else:
					pass
		return "No solution"
a = cross_river(4, 4, 0, 0, "left", [], 4)
print(a)