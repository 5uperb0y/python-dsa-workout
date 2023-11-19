"""
Write a function `draw_spiral` using Turtle graphics to recursively draw a spiral,
The spiral should reduce in size with each recursive call until it disappears.
"""
import turtle
def draw_spiral(my_turtle, line_len):
	if line_len > 0:
		my_turtle.forward(line_len)
		my_turtle.right(90)
		draw_spiral(my_turtle, line_len - 5)
my_turtle = turtle.Turtle()
window = turtle.Screen()
draw_spiral(my_turtle, line_len = 100)
window.exitonclick()
