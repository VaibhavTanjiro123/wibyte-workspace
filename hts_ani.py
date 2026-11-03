import turtle
import time
import random
import math

# create snake and screen
t = turtle.Turtle()
t_auto = turtle.Turtle()
ts = turtle.Screen()

turtle.setup(width=1200, height=600)

bnd = turtle.Turtle()
bnd.hideturtle()

score = turtle.Turtle()
score.penup()
score.color("blue")
score.goto(150, 150)
score.hideturtle()

intro = turtle.Turtle()
intro.penup()
intro.hideturtle()

#create eyes
eye1 = turtle.Turtle()
eye2 = turtle.Turtle()

eye1.shape("circle")
eye2.shape("circle")

eye1.turtlesize(0.3)
eye2.turtlesize(0.3)

eye1.penup()
eye2.penup()

eye1.speed(0)
eye2.speed(0)

#color snake and background
t.color("gold")
t_auto.color("firebrick")
ts.bgcolor("khaki")

#setup shapes
star_shape = ((0, 10), (-3, 3), (-10, 3), (-4, -1), 
              (-6, -8), (0, -4), (6, -8), (4, -1), 
              (10, 3), (3, 3))

trapizoid_shape = ((-10, 0), (10, 0), (12, 22), (-12, 22))

base_head_shape = ((-10, -7), (10, -7), (14, 15),(0, 20), (-14, 15))
head_shape = ((-10, -10), (10, -10), (14, 12),(0, 17), (-14, 12))

turtle.register_shape("small_star", star_shape)

turtle.register_shape("trapizoid", trapizoid_shape)

turtle.register_shape("snake_head", head_shape)

#shape head
t.shape("snake_head")
t_auto.shape("snake_head")

#define movement
def right():
    if t.heading() != 180:
        t.setheading(0)
    position_eyes()
def left():
    if t.heading() != 0:
        t.setheading(180)
    position_eyes()
def up():
    if t.heading() != 270:
        t.setheading(90)
    position_eyes()
def down():
    if t.heading() != 90:
        t.setheading(270)
    position_eyes()
    


#setup foods

num_foods = 10




def place_foods(color):  
    foods = []
    food_pos = []

    for _ in range(num_foods):
        food = turtle.Turtle()
        food.shape("small_star")
        food.penup()
        food.speed(0)
        food.color(color)
        food.goto(random.randint(-200, 200), random.randint(-200, 200))
        food.setheading(random.randint(0, 180))
        foods.append(food)
        food_pos.append(food.pos())

    return foods, food_pos

foods, food_pos = place_foods("yellow")

eaten = [False] * num_foods

segments = []
segments_auto = []

x_pos = []
y_pos = []

def position_eyes():
    x = t.xcor()
    y = t.ycor()

    if t.heading() == 0 or t.heading() == 180:
        eye1.goto(x, y + 5)
        eye2.goto(x, y - 5)
    elif t.heading() == 90 or t.heading() == 270:
        eye1.goto(x + 5, y)
        eye2.goto(x - 5, y)
    
def position_eyes_auto():
    x = t_auto.xcor()
    y = t_auto.ycor()

    if t_auto.heading() == 0 or t_auto.heading() == 180:
        eye1.goto(x, y + 5)
        eye2.goto(x, y - 5)
    elif t_auto.heading() == 90 or t_auto.heading() == 270:
        eye1.goto(x + 5, y)
        eye2.goto(x - 5, y)

def ManhattanDist(pos0, pos1):
    return abs(pos1[0] - pos0[0]) + abs(pos1[1] - pos0[1])

index = turtle.Turtle()

index.penup()
index.speed(0)
index.hideturtle()

for i in food_pos:
    index.goto(i[0] + 10, i[1] + 10)
    index.write(str(food_pos.index(i)))

index.clear()

def FindDist(foods_locate, i_min, present, D_min):
        for i in foods_locate:
            D = ManhattanDist(food_pos[i], present)
            if D < D_min:
                D_min, i_min = D, i
        return D_min, i_min


def find_optimal(food_pos_val): 
    order = []
    dist_vect = []

    present = (0, 0)
    D_min = math.inf

    i_min = 0
    print(food_pos_val)

    foods_locate = [x for x in range(num_foods)]

    while len(foods_locate) > 0:
        D_min, i_min = FindDist(foods_locate, i_min, present, D_min)
    
        present = food_pos_val[i_min]
        order.append(i_min)
        dist_vect.append(D_min)
        foods_locate.remove(i_min)

        D_min = math.inf

    print(order)
    print(dist_vect)

    nearest_neigbor_optimal = 0
    for d in dist_vect:
        nearest_neigbor_optimal += d

    nearest_neigbor_optimal += ManhattanDist(food_pos_val[order[-1]], (0 ,0))

    return order, dist_vect, nearest_neigbor_optimal

order, dist_vect, nearest_neigbor_optimal = find_optimal(food_pos)

def begin(game_over):
    bnd.speed(0)
    bnd.penup()
    bnd.goto(-220, -220)
    bnd.pendown()
    bnd.goto(220, -220)
    bnd.goto(220, 220)
    bnd.goto(-220, 220)
    bnd.goto(-220, -220)
    intro.clear()
    steps = 0
#game loop
    while not game_over:

        score.write(len(segments), align = "Center", font = ("Courier", 24, "normal"))

        position_eyes()

        for i in range(num_foods):
            if not eaten[i]:
                if t.distance(foods[i]) < 20:
                    eaten[i] = True
                    if len(segments) % 2 == 0:
                        foods[i].color("green")
                    else:
                        foods[i].color("orange")
                    foods[i].shape("square")
                    foods[i].setheading(0)
                    segments.append(foods[i])
                    score.clear()


        for i in range(len(segments) - 1, 0, -1):
            x_pos = segments[i - 1].xcor()
            y_pos = segments[i - 1].ycor()
            segments[i].goto(x_pos, y_pos)

    
        if len(segments) > 0:
            x_pos = t.xcor()
            y_pos = t.ycor()

            segments[0].goto(x_pos, y_pos)
        
        if len(segments) >= num_foods:
            if abs(t.xcor()) < 20 and abs(t.ycor()) < 20:
                for i in range(len(foods)):
                     foods[i].hideturtle()
                t.hideturtle()
                game_over = True
                intro.goto(0, -100)
                intro.write("Steps taken are: {}".format(steps*20), align = "Center", font = ("Courier", 30, "normal"))
                intro.goto(0, -150)
                
                intro.write("Steps by the nearest neighbour algorithm are : {}".format(nearest_neigbor_optimal), align = "Center", font = ("Courier", 30, "normal"))
                return steps


        t.forward(20)
        steps += 1
        position_eyes()
        x_pos = t.xcor()
        y_pos = t.ycor()

        if x_pos > 220:
                t.speed(0)
                t.penup()
                t.goto(-220, y_pos)
                t.pendown()
        if x_pos < -220:
                t.speed(0)
                t.penup()
                t.goto(220, y_pos)
                t.pendown()
        if y_pos > 220:
                t.speed(0)
                t.penup()
                t.goto(-x_pos, -220)
                t.pendown()
        if y_pos < -220:
                t.speed(0)
                t.penup()
                t.goto(-x_pos, 220)
                t.pendown()

        time.sleep(0.1)


def begin_auto(steps, foods, food_pos):

   # order, dist_vect, nearest_neigbor_optimal = find_optimal(food_pos)

    game_over = False

    eaten = [False] * num_foods
    bnd.speed(0)
    bnd.penup()
    bnd.goto(-220, -220)
    bnd.pendown()
    bnd.goto(220, -220)
    bnd.goto(220, 220)
    bnd.goto(-220, 220)
    bnd.goto(-220, -220)
    intro.clear()
    j = 0
    steps_auto = 0
#game loop
    while not game_over:

        score.write(len(segments_auto), align = "Center", font = ("Courier", 24, "normal"))

        position_eyes_auto()

        for i in range(num_foods):
            if not eaten[i]:
                if t_auto.distance(foods[i]) < 20:
                    eaten[i] = True
                    if len(segments_auto) % 2 == 0:
                        foods[i].color("blue")
                    else:
                        foods[i].color("red")
                    foods[i].shape("square")
                    foods[i].setheading(0)
                    segments_auto.append(foods[i])
                    j += 1
                    score.clear()


        for i in range(len(segments_auto) - 1, 0, -1):
            x_pos = segments_auto[i - 1].xcor()
            y_pos = segments_auto[i - 1].ycor()
            segments_auto[i].goto(x_pos, y_pos)

    
        if len(segments_auto) > 0:
            x_pos = t_auto.xcor()
            y_pos = t_auto.ycor()

            segments_auto[0].goto(x_pos, y_pos)


        if len(segments_auto) >= num_foods:
            if abs(t_auto.xcor()) < 20 and abs(t_auto.ycor()) < 20:
                game_over = True
                intro.goto(0, -100)
                intro.write("Steps taken are: {}".format(steps_auto*20), align = "Center", font = ("Courier", 30, "normal"))
                intro.goto(0, -150)
                intro.write("Steps by the nearest neighbour algorithm are : {}".format(nearest_neigbor_optimal), align = "Center", font = ("Courier", 30, "normal"))

        if j <= 9:
             next_pos = food_pos[order[j]]
        else:
            next_pos = (0, 0)
        next_x = next_pos[0]
        next_y = next_pos[1]

        present_x = t_auto.xcor()
        present_y = t_auto.ycor()

        if abs(present_x - next_x) > 10:
             if next_x > present_x:
                  t_auto.setheading(0)
             else:
                  t_auto.setheading(180)
        
        else:
            if abs(present_y - next_y) > 10:
                if next_y > present_y:
                    t_auto.setheading(90)
                else:
                    t_auto.setheading(270)
             

        t_auto.forward(20)
        steps_auto += 1
        position_eyes_auto()
        x_pos = t_auto.xcor()
        y_pos = t_auto.ycor()

        if x_pos > 220:
                t_auto.speed(0)
                t_auto.penup()
                t_auto.goto(-220, y_pos)
                t_auto.pendown()
        if x_pos < -220:
                t_auto.speed(0)
                t_auto.penup()
                t_auto.goto(220, y_pos)
                t_auto.pendown()
        if y_pos > 220:
                t_auto.speed(0)
                t_auto.penup()
                t_auto.goto(-x_pos, -220)
                t_auto.pendown()
        if y_pos < -220:
                t_auto.speed(0)
                t_auto.penup()
                t_auto.goto(-x_pos, 220)
                t_auto.pendown()

        time.sleep(0.1)

def play(x, y, game_over):
    if game_over:
        return
    t_auto.hideturtle()
    if x > -100 and x < 100 and y > -100 and y < -50:
        steps = begin(game_over)
        index = turtle.Turtle()

        index.penup()
        index.speed(0)
        index.hideturtle()

        for i in food_pos:
            index.goto(i[0] + 10, i[1] + 10)
            index.write(str(food_pos.index(i)))
    elif x > -100 and x < 100 and y > -200 and y < -150:
        t.hideturtle()
        #steps = begin(game_over)
        steps = 0
        #foods = []
        #food_pos = []
        #foods, food_pos = place_foods("red")
        index = turtle.Turtle()

        index.penup()
        index.speed(0)
        index.hideturtle()

        for i in food_pos:

            index.goto(i[0] + 10, i[1] + 10)
            index.write(str(food_pos.index(i)))

        
        steps = 0
        t_auto.showturtle()

        print(foods)
        
        begin_auto(steps, foods, food_pos)


#allow movement
game_over = False

intro.speed(0)

intro.goto(-210, -210)
intro.color("white")
intro.fillcolor("white")
intro.pendown()
intro.begin_fill()
intro.goto(210, -210)
intro.goto(210, 210)
intro.goto(-210, 210)
intro.goto(-210, -210)
intro.end_fill()

intro.color("blue")
intro.fillcolor("#5EFFFF")
intro.penup()
intro.goto(-100, -100)
intro.pendown()
intro.begin_fill()
intro.goto(-100, -50)
intro.goto(100, -50)
intro.goto(100, -100)
intro.goto(-100, -100)
intro.end_fill()

intro.color("blue")
intro.fillcolor("#FFC595")
intro.penup()
intro.goto(-100, -200)
intro.pendown()
intro.begin_fill()
intro.goto(-100, -150)
intro.goto(100, -150)
intro.goto(100, -200)
intro.goto(-100, -200)
intro.end_fill()

intro.penup()

intro.goto(0, -75)
intro.write("Play!", align = "Center", font = ("Courier", 24, "normal"))

intro.goto(0, 100)
intro.write("The Hungry Traveling Snake", align = "Center", font = ("Courier", 24, "normal"))

intro.goto(0, 0)
intro.write("Snake likes starfruit! Get 10 starfruits for him", align = "Center", font = ("Courier", 10, "normal"))

ts.onclick(lambda x, y, game_over=game_over: play(x, y, game_over))
ts.onkey(right, "Right")
ts.onkey(left, "Left")
ts.onkey(up, "Up")
ts.onkey(down, "Down")
ts.listen()