import turtle
import time
import random

## Variables
# Speed
speed = 20

# Delay
delay = 0.1

# Colors
colors  = ["red","blue","orange","purple","pink","yellow"]

# Set up the screen
wn = turtle.Screen()
wn.title("Snake!")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0) 

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake body
body = []

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("green")
food.speed(0)
food.penup()
food.goto(0, 200)

# Score display
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color = "white"
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Score
curr_score = 0
high_score = 0










## Functions
# Directions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Keyboard input
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# Snake movement
def move():
    if head.direction == "up":
        head.sety(head.ycor() + speed)
    if head.direction == "down":
        head.sety(head.ycor() - speed)
    if head.direction == "left":
        head.setx(head.xcor() - speed)
    if head.direction == "right":
        head.setx(head.xcor() + speed)        


# Game loop
while True:
    wn.update()

    # Check for border collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        high_score = max(curr_score, high_score)
        curr_score = 0

        # Need to 'move' the body since Turtle delete gets funky
        for b in body:
            b.goto(1000, 1000)
        
        # Clear body
        body.clear()

    # When the snake eats food 
    if head.distance(food) < 20: # Since turtle objects are 20 x 20 pixels
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        speed += 0.5
        curr_score += 1

        # Snake body
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color(random.choice(colors))
        new_body.penup()
        body.append(new_body)
    
    # Moving the snake body, in reverse order 
    for i in range(len(body) - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)

    # Moving body[0] to where the head is
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)
        
    move()

    time.sleep(delay)
