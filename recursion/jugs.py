"""
Write a program to solve the following problem: You have two jugs: a 4-gallon jug and
a 3-gallon jug. Neither of the jugs have markings on them. There is a pump that can
be used to fill the jugs with water. How can you get exactly two gallons of water in the
4-gallon jug?
Generalize the problem above so that the parameters to your solution include the sizes of
each jug and the final amount of water to be left in the larger jug.
Notes:
- this problem could be solved using breadth-first search
"""
def is_valid(vol1, vol2, max_vol1, max_vol2):
	return 0 <= vol1 <= max_vol1 and 0 <= vol2 <= max_vol2
def dfs_jugs(vol1, vol2, max_vol1, max_vol2, target, steps):
	# suppose that jug 1 is the larger jug (i'm lazy)
	if  vol1 == target:
		return steps
	else:
		operations = {
			"fill_jug1": (max_vol1, vol2),
			"fill_jug2": (vol1, max_vol2),
			"empty_jug1": (0, vol2),
			"empty_jug2": (vol1, 0),
			"pour_jug2_into_jug1": (vol1 - min(vol1, max_vol2 - vol2), vol2 + min(vol1, max_vol2 - vol2)),
			"pour_jug1_into_jug2": (vol1 + min(vol2, max_vol1 - vol1), vol2 - min(vol2, max_vol1 - vol1))
		}
		for oper, vol in operations.items():
			# extract volume histories
			# operation types are not necessary information for solving problem
			# including operation types in the statement would induce redundant steps
			states = [s[1] for s in steps]
			if is_valid(vol[0], vol[1], max_vol1, max_vol2) and vol not in states:
				# append operaiton types for output readability
				steps.append([oper, vol])
				solution = dfs_jugs(vol[0], vol[1], max_vol1, max_vol2, target, steps)
				if solution:
					return solution
				else:
					steps.pop()
			else:
				pass
	# I has write `return "no solution"`. This results in premature stop because of `if solution` return wrong thing
	return None
solution = dfs_jugs(0, 0, 4, 3, 2, [])
for s in solution:
	print(s)