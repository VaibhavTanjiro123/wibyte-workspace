import turtle
import time
import random
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
n_foods=10
list_foods=[]
for kk in range(n_foods):
    food=turtle.Turtle()
    food.penup()
    food.speed(0)
    food.shape('turtle')
    food.color('violet')
    food.goto(random.randint(-200,200),random.randint(-200,200))
    list_foods.append(food)
Game_over=False
while not Game_over:
    t.forward(20)
    time.sleep(0.1)
turtle.done()