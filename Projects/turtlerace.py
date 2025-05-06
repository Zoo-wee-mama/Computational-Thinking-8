# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite


# Section 2 - Variables
# TODO - add starting values for all the variables
x1 = -200
y1 = -200
x2 = -210
y2 = -100
x3 = -200
y3 = 0
x4 = -200
y4 = 100
# Section 3 - Setup
# TODO - use your own background, and set your four turtles to images of your choice
set_background("castle")
t1 = create_sprite("basketball",x1,y1)
t2 = create_sprite("applecore",x2,y2)
t3 = create_sprite("sodacan",x3,y3)
t4 = create_sprite("waterbottle",x4,y4)


# # Section 4 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - t1 has a high range, t2 has a very fixed range, t3 has super high potential but might go bad, and t4 is in the middle
for i in range(30):
	x1 += random.randint(10,30)
	x2 += random.randint(16,18)
	x3 += random.randint(2,50)
	x4 += random.randint(4,22)
	t1.goto(x1, y1)
	t2.goto(x2, y2)
	t3.goto(x3, y3)
	t4.goto(x4, y4)
	time.sleep(0.1)


# # Section 5 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
	print("player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >=x4:
	print("player 2 wins!")
elif x3 >= x1 and x3 >= x2 and x3 >=x4:
	print("player 3 wins!")
elif x4 >= x1 and x4 >= x3 and x4 >=x2:
	print("player 4 wins!")




turtle.exitonclick()
