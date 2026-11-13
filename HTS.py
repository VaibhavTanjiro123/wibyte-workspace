import turtle
import time
import random
t=turtle.Turtle()
ts=t.screen
pen=turtle.Turtle()
pen.color('Black')
pen.hideturtle()
pen.penup()
pen.goto(150,150)
repo=turtle.Turtle()
repo.color('Black')
repo.hideturtle()
repo.penup()
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
    food.shape('square')
    food.color('blue')
    food.goto(random.randint(-200,200),random.randint(-200,200))
    list_foods.append(food)
eaten=[False]*n_foods
segments=[]
xpos=[]
ypos=[]
steps=''
Game_over=False
while not Game_over:
    steps=steps+1
    pen.write(len(segments),align='Center',font=('Courier',24,'normal'))
    for kk in range (n_foods):
        if not eaten[kk]:
            if t.distance(list_foods[kk])<20:
                eaten[kk]=True
                list_foods[kk].color('green')
                segments.append(list_foods[kk])
                pen.clear()
    for idx in range(len(segments)-1,0,-1):
            x = segments[idx-1].xcor()
            y = segments[idx-1].ycor()
            segments[idx].goto(x,y)
    if len(segments)>0:
        x=t.xcor()
        y=t.ycor()
        segments[0].st()
        segments[0].goto(x,y)        
    if len(segments)==n_foods:
        if abs(t.xcor())<20 and abs(t.ycor())<20:
            Game_over= True
            time.sleep(1)
            t.clear()
            t.ht()
        for kk in range(len(segments)):
            segments[kk].ht()
        repo.write('Total Steps Taken Are:'+ str(steps*20),align='Center',font=('Courier',24,'normal'))    
    t.forward(20)
    time.sleep(0.1)
turtle.done()