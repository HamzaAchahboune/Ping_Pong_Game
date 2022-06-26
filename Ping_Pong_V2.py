import turtle

# Window
win = turtle.Screen()
win.title("Ping Pong Game")
win.setup(width=800, height=600)
win.tracer(0)
win.bgcolor(1,1,1)
P1 = win.textinput("Nom :" , "Enter name of Player 1 :")
P2 = win.textinput("Nom :" , "Enter name of Player 2 :")

# game ball :
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.shapesize(1)
ball.goto(x=0,y=0)
ball.penup()
ball_dx , ball_dy = 1, -1
ball_speed = 0.5

#center line :
Centre_Line = turtle.Turtle()
Centre_Line.speed(0)
Centre_Line.shape("square")
Centre_Line.color("black")
Centre_Line.shapesize(stretch_len=.1,stretch_wid=25)
Centre_Line.penup()
Centre_Line.goto(0,0)

#Player 1 :
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.shapesize(5,1)
p1.color("green")
p1.penup()
p1.goto(-350,0)
p1_score = 0

#Player 1 :
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.shapesize(5,1)
p2.color("red")
p2.penup()
p2.goto(350,0)
p2_score = 0

#Text:
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.goto(0,260)
score.write(f"{P1}:0  {P2}:0 Pause : p " , align="center" , font=("Courier",14,"normal"))
score.hideturtle()

#player 1 movement:
player_Speed = 20
def p1_move_up():
    p1.sety(p1.ycor() + player_Speed)
def p1_move_down():
    p1.sety(p1.ycor()- player_Speed)

#player 1 movement:
def p2_move_up():
    p2.sety(p2.ycor() + player_Speed)
def p2_move_down():
    p2.sety(p2.ycor() - player_Speed)

#get user input
win.listen()
win.onkeypress(p1_move_up,"Up")
win.onkeypress(p1_move_down,"Down")

win.onkeypress(p2_move_up,"q")
win.onkeypress(p2_move_down,'w')

# the pause function
paused = False
def Paused():
    global paused
    if paused == True:
        paused=False
    else :
        paused=True
win.onkeypress(Paused,"p")


#Game loop :
while True:
    if not paused:
        win.update()

        #First move of ball
        ball.setx(ball.xcor() + (ball_speed * ball_dx))
        ball.sety(ball.ycor() + (ball_speed * ball_dy))

        #ball & border
        if(ball.ycor()>290):
            ball.sety(290)
            ball_dy *=-1

        #ball & border
        if(ball.ycor()<-290):
            ball.sety(-290)
            ball_dy *=-1

        #Ball and player collision
        #Player 1
        if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (p1.ycor()-60) and ball.ycor() < (p1.ycor()+60):
            ball.setx(-340)
            ball_dx *= -1

        #Player2 :
        if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (p2.ycor()-60) and ball.ycor() < (p2.ycor()+60):
            ball.setx(340)
            ball_dx *= -1

        # score handling
        if(ball.xcor() > 390):
            ball.goto(0, 0)
            ball_dx *= -1
            score.clear()
            p1_score+=1
            score.write(f"{P1}:{p1_score}  {P2}:{p2_score} Pause :p", align="center", font=("Courier", 14, "normal"))

        if(ball.xcor() < -390):
            ball.goto(0, 0)
            ball_dx *= -1
            score.clear()
            p2_score+=1
            score.write(f"{P1}:{p1_score}  {P2}:{p2_score} Pause :p", align="center", font=("Courier", 14, "normal"))
    else:
        win.update()


