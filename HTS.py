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
initial=True

nn_order=[]
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
exp_order= [x for x in range (0, 10, 1)]
food_pos=[]
nn=turtle.Turtle()
nn.penup()
nn.speed(0)
nn.st()
#exp_order=nn_order
for pos in food_pos:
    nn.goto(pos[0]+10,pos[1]+10)
    nn.write(str(food_pos.index(pos)))


def dist(posfin,positl):
    return abs(posfin[0]-positl[0]+posfin[1]-positl[1])



for kk in range(n_foods):
    food=turtle.Turtle()
    food.penup()
    food.speed(0)
    food.shape('square')
    food.color('blue')
    food.goto(random.randint(-200,200),random.randint(-200,200))
    food_pos.append(food.pos())
    list_foods.append(food)


dist_vect=[]
present=(0,0)
dmin=1000000000
kkmin=0
foods= [x for x in range(n_foods)]
while len(foods)>0:
    for kk in foods:
        D = dist(food_pos[kk], present)
        if D<dmin:
            dmin,kkmin=D,kk
    present=food_pos[kkmin]
    nn_order.append(kkmin)
    dist_vect.append(dmin)
    foods.remove(kkmin)
    dmin=1000000000
opdist = 0
for d in dist_vect:
    opdist+=d
opdist+=dist(food_pos[nn_order[-1]], (0,0))


eaten=[False]*n_foods
segments=[]
xpos=[]
ypos=[]
steps=0
Game_over=False
while not Game_over:
    if len(exp_order) > 0:
        for kk in range(n_foods):
            if kk == exp_order[0]:
                list_foods[kk].color('purple')
    if initial:
        time.sleep(5)
        initial=False
    
    steps=steps+1
    pen.write(len(segments),align='Center',font=('Courier',24,'normal'))
    for kk in range (n_foods):
        if not eaten[kk]:
            if t.distance(list_foods[kk])<20:
                eaten[kk]=True
                if kk == exp_order[0]:                    
                    list_foods[kk].color('green')
                    segments.append(list_foods[kk])
                    pen.clear()
                    exp_order.pop(0)
                else:
                    Game_over=True
                    time.sleep(1)
                    t.clear()
                    t.ht()
                    for kk in range (len(segments)):
                        segments[kk].ht()                    
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
            Game_over=True
            time.sleep(1)
            t.clear()
            t.ht()
            for kk in range (len(segments)):
                segments[kk].ht()
    time.sleep(0.1)

repo.write('Total Steps Taken Are:'+ str(steps*20),align='Center',font=('Courier',24,'normal'))
turtle.done()