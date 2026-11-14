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
food_pos=[]
for kk in range(n_foods):
    food=turtle.Turtle()
    food.penup()
    food.speed(0)
    food.shape('square')
    food.color('blue')
    food.goto(random.randint(-200,200),random.randint(-200,200))
    food_pos.append((food.xcor(),food.ycor()))
    list_foods.append(food)
eaten=[False]*n_foods
segments=[]
xpos=[]
ypos=[]
steps=0
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
    t.forward(20)
    if len(segments)==n_foods:
        if abs(t.xcor())<20 and abs(t.ycor())<20:
            time.sleep(1)
            t.clear()
            
    time.sleep(0.1)

repo.write('Total Steps Taken Are:'+ str(steps*20),align='Center',font=('Courier',24,'normal'))

input()


repo.clear()
pen.ht()
pen.clear()

nn_order=[]
for kk in range(n_foods):
    list_foods[kk].goto(food_pos[kk])
    list_foods[kk].st()
    list_foods[kk].color('purple')
    nn_order.append(food_pos[kk])
    print (nn_order)
t_a=turtle.Turtle()
t_a.shape('square')
t_a.color('violet')
t_a.goto(0,0)
t_a.st()

presentpos=(0,0)
presentx=presentpos[0]
presenty=presentpos[1]
nextpos=(0,0)
eaten=[False]*n_foods
segmentsauto=[]
jj=0
stepsa=0
Game_over=False
while not Game_over:
    stepsa+=1
    pen.write(len(segmentsauto),align='Center',font=('Courier',24,'normal'))
    for kk in range (n_foods):
        if not eaten[kk]:
            if t_a.distance(list_foods[kk])<20:
                eaten[kk]=True
                list_foods[kk].color('green')
                segmentsauto.append(list_foods[kk])
                jj=jj+1
                print(kk)
                pen.clear()
    for idx in range(len(segmentsauto)-1,0,-1):
            x = segmentsauto[idx-1].xcor()
            y = segmentsauto[idx-1].ycor()
            segmentsauto[idx].goto(x,y)
    if len(segmentsauto)>0:
        x=t_a.xcor()
        y=t_a.ycor()
        segmentsauto[0].st()
        segmentsauto[0].goto(x,y)        
    t_a.forward(20)
    if len(segmentsauto)==n_foods:
        if abs(t_a.xcor())<20 and abs(t_a.ycor())<20:
            Game_over= True
            time.sleep(1)
            t_a.clear()
            t_a.ht()
            for kk in range(len(segments)):
                segmentsauto[kk].ht()

    time.sleep(0.1)
    
    if jj <=9:
        nextpos=nn_order[kk]
    else:
        nextpos = (0,0)
    nextx=nextpos[0]
    nexty=nextpos[1]

    presentx=t_a.xcor()
    presenty=t_a.ycor()
    if abs(presentx-nextx)>10:
        if nextx>presentx:
            t_a.setheading(0)
        else:
            t_a.setheading(180)
    else:
        if abs(presenty-nexty)>10:
            if nexty>presenty:
                t_a.setheading(90)
            else:
                t_a.setheading(270)
repo.write('Total Steps Taken Are:'+ str(stepsa*20),align='Center',font=('Courier',24,'normal'))
turtle.done()