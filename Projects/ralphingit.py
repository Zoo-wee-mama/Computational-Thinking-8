# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
# TODO - create your player character
s2 = create_sprite("bar",0,0)
s1 = create_sprite("ralph-l",0,0)
s3 = create_sprite("guy", -280,0)
#Two sprites are inserted, and one background.

# TODO - set your background

# TODO - set the starting value for your variable
bottles=0
s1.direction = "left"
# Section 3: Controls
# TODO - define your controls
def move_left():
	s1.setheading(180)
	s1.forward(10) 
	if s1.direction == "right":
		set_image(s1, "ralph-l")
		s1.direction = "left"
def move_right():
	s1.setheading(0)
	s1.forward(10)
	if s1.direction == "left":
		set_image(s1, "ralph-r")
		s1.direction = "right"

# TODO - pick keys for each control
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

#s1 can move left and right based on arrow keys. s3 is an interactive component.

s4 = 0
def talk():
	global s4
	if s4 == 0:
		s3.color("White")
		s3.write("Hullo!",font = ("Arial", 25, "normal"))
		s4 = 1
	elif s4 == 1:
		s3.clear()
		s3.color("White")
		s3.write("Here, sit down, mate!🤯🤯🤯",font = ("Arial", 25, "normal"))
		s4 = 2
	elif s4 == 2:
		s3.clear()
		s3.color("White")
		s3.write("Fancy a drink?", font = ("Arial", 25, "normal"))
		s4 = 3
	elif s4 == 3:
		s3.clear()
		s3.color("Red")
		s3.write("bro ts pmo sb sybau ikiag ong fr", font = ("Arial", 25, "normal"))
		s4 = 4
	elif s4 == 4:
		s3.clear()
		s3.color("Yellow")
		s3.write("Hooray! You successfully didn't fall back into your alchohol addiction!!!!", font = ("Arial", 12, "normal"))
		s4 = 5
	elif s4 == 5:
		s3.clear()
		s4 = 6

window.onkeypress(talk, "space")


# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.1)
	timer += 1  
	 
    
 	# TODO - code for automatic actions


	window.update()

	if s4 == 6:
		break
	

print("Game Over")
