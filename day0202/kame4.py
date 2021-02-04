import turtle
t=turtle.Turtle()
t.shape('turtle')
t.forward(100)
for _ in range(5):
	t.right(135)
	t.forward(100)
t.home()
turtle.mainloop()
