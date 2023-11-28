"""
Find the way to exit a maze
"""
import random
from maze import set_maze
def passable(maze, x, y):
	xlim = len(maze[0]) - 1
	ylim = len(maze) - 1
	if 0 <= x <= xlim and 0 <= y <= ylim and maze[x][y] == 1:
		return True
	else:
		return False
def is_exit(maze, x, y):
	xlim = len(maze[0]) - 1
	ylim = len(maze) - 1
	if 0 < x < xlim and 0 < y < ylim:
		return False
	else:
		return True
def find_exit(maze, x, y, path):
	if is_exit(maze, x, y):
		path.append((x, y))
		return path
	else:
		dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
		for d in dirs:
			nx, ny = x + d[0], y + d[1]
			if passable(maze, nx, ny) and (nx, ny) not in path:
				path.append((nx, ny))
				result = find_exit(maze, nx, ny, path)
				if result:
					return result
				else:
					path.pop()
			else:
				pass
		return None
def main():
	maze = set_maze(20, 20)
	x, y = 3, 3
	while maze[x][y] == 0:
		x = random.randint(1, len(maze) - 2)
		y = random.randint(1, len(maze[0]) - 2)
	path = find_exit(maze, x, y, [])
	for i, j in path:
		maze[i][j] = 2
	maze[x][y] = "s"
	def draw(n):
		if n == 0:
			return "█"
		elif n == 1:
			return " "
		elif n == 2:
			return "."
		else:
			return n
	for row in maze:
		print("".join(draw(n) for n in row))
if __name__ == "__main__":
	main()
