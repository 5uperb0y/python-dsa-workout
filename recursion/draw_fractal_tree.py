"""
Write a function `draw_fractal_tree` using Turtle graphics to recursively draw a fractal tree.
The algorithm creates a fractal tree by drawing a line (representing a tree branch), then
recursively calling itself twice to draw smaller branches at the end of the current branch,
first turning right, then left. Each recursive call decreases the length of the branch, and
the process repeats until the branch length is too small, creating a tree-like fractal pattern.
"""
import turtle
def draw_fractal_tree(my_turtle, branch_len):
	if branch_len > 5:
		my_turtle.forward(branch_len)
		my_turtle.right(20)
		draw_fractal_tree(my_turtle, branch_len - 5)
		my_turtle.left(40)
		draw_fractal_tree(my_turtle, branch_len - 5)
		my_turtle.right(20)
		my_turtle.backward(branch_len)
my_turtle = turtle.Turtle()
window = turtle.Screen()
draw_fractal_tree(my_turtle, branch_len = 50)
window.exitonclick()