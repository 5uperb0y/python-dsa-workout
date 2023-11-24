"""
Generate a maze with width * height
"""
import random
def is_valid(grid, x, y):
	xlim = len(grid)
	ylim = len(grid[0])
	# ensure that the position isn't at edge
	if 0 < x < xlim and 0 < y < ylim:
		# ensure the position hasn't been visited
		return grid[x][y] == 0
	else:
		return False
def pathing(grid, x, y):
	dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	random.shuffle(dirs)
	# Explore valid path in the four direction recursively
	for s in dirs:
		nx, ny = x + s[0] * 2, y + s[1] * 2
		if is_valid(grid, nx, ny):
			# break the wall
			grid[x + s[0]][y + s[1]] = 1
			# move through the wall
			grid[nx][ny] = 1
			pathing(grid, nx, ny)
		else:
			pass
def add_exit(grid):
	width = len(grid[0]) - 1
	height = len(grid) - 1
	edges = [(0, y) for y in range(0, width)] + \
			[(height, y) for y in range(0, width)] + \
			[(x, 0) for x in range(0, height)] + \
			[(x, width) for x in range(0, height)]
	while True:
		x, y = random.choice(edges)
		if grid[x][y] == 1:
			break
		else:
			for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
				nx, ny = x + dx * 2, y + dy * 2
				if 0 <= nx <= height and 0 <= ny <= width:
					if grid[nx][ny] == 1:
						grid[x + dx][y + dy] = 1
						grid[x][y] = 1
					else:
						x, y = nx, ny
				else:
					pass
	return grid

def set_maze(width, height):
	grid = [
		[0 for _ in range(width)]
		for _ in range(height)
	]
	x = random.randint(1, height - 1)
	y = random.randint(1, width - 1)
	grid[x][y] = 1
	pathing(grid, x, y)
	maze = add_exit(grid)
	return maze
def main():
	maze = set_maze(20, 20)
	for row in maze:
		print("".join(["█" if cell == 0 else " " for cell in row]))
if __name__ == "main":
	main()