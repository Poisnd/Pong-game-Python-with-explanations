import turtle

win = turtle.Screen()
win.title("Ping pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#Score
score_a = 0
score_b = 0

# Paddle A (1 (WASD))
paddle_a = turtle.Turtle() # Make object
paddle_a.speed(0) # Animation speed (No animation no animation speed)
paddle_a.shape("square") # Object shape (obvv)
paddle_a.color("blue") # Object color (ima kms)
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # Dawg i aint even gon explain no mo
paddle_a.penup() # Turtle works by drawing so pen up makes it not draw anymore dk how to explain it type shit
paddle_a.goto(-350, 0) # Object position

# Paddle B (2 (Arrow keys))
paddle_b = turtle.Turtle() # Make object
paddle_b.speed(0) # Animation speed (No animation no animation speed)
paddle_b.shape("square") # Object shape (obvv)
paddle_b.color("blue") # Object color (ima kms)
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # Dawg i aint even gon explain no mo
paddle_b.penup() # Turtle works by drawing so pen up makes it not draw anymore dk how to explain it type shit
paddle_b.goto(350, 0) # Object position

# Ball type shi type shi
# Pretty much same concept as paddles tbh
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions bla bla bla boring but very fun
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Binding tp shit
win.listen() # Listens when a key and what key is pressed
win.onkeypress(paddle_a_up, "w") # runs the function if the W key is pressed
win.onkeypress(paddle_a_down, "s") # same shit as above instead its S key
win.onkeypress(paddle_b_up, "Up") # same shit just Arrow key up
win.onkeypress(paddle_b_down, "Down") # aint even gon explain
# note this vaki if its a letter pressed it has to be lowercase and if its arrows its gotta be uppercase first letter

while True: # this is just a loop
    win.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx) # Moves the ball sideways
    ball.sety(ball.ycor() + ball.dy) # moves the ball upwards
    # Basically the ball starts moving diagonally up and right works by changing the balls x/y cor and changing it to current x/y cor + ball.dx 

    # borders and shit
    if ball.ycor() > 290: #checks if it goes over 290 (border of the screen)
        ball.sety(290) #so if the function is ran (ball went over 290 pixels) then the ball is set to 290 pixels (border of the screen)
        ball.dy *= -1 #just reverses the direction
        #if the ball is on 290 pixels (border of the screen) then it sets the ball on that pixel and reverses the direction making it "bounce"
    
    if ball.ycor() < -290: #same shit just reversed cuz its switched dont be dumb use your brain 
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: # same shit
        ball.goto(0, 0) # ball goes to center
        ball.dx *= -1 # ball changes direction
        score_a += 1 # score type shit
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    # different than y cor because when the ball goes off the side the player gets a point yk yk type shit type shit

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1 # score type shit
        pen.clear
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    # same shit just reversed yk yk

    # bouncing of paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1