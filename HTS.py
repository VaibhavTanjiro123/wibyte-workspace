import turtle
import time
t=turtle.Turtle()
ts=t.screen
ts.bgcolor('khaki')
t.shape('square')
t.color('black')
def down():
    if t.heading() !=90.0:
        t.setheading(-90.0)
    
def up():
    if t.heading() !=270.0:
        t.setheading(90.0)

def left():
    if t.heading() !=0.0:
        t.setheading(180.0)

def right():
    if t.heading() !=180.0:
        t.setheading(0.0)

ts.onkey(down, "Down")
ts.onkey(up, "Up")
ts.onkey(left, "Left")
ts.onkey(right, "Right")
ts.listen()
Game_over=False
while not Game_over:
    t.forward(20)
    time.sleep(0.1)
turtle.done()