import turtle
import random

arcs = [10,20,30,60,120,80] #list of angles
#col  = ["limegreen","aqua","moccasin","purple","darkred","yellow","skyblue"]
#Initialize circle of 200 radius with center(0,0)
x = 0
y = 0
turtle.colormode(255) #so we can randomize the RGB colors for the arc segments

turtle.up()
turtle.setposition(0,-200)
turtle.down()
#turtle.begin_fill()
turtle.pencolor("white")
turtle.circle(200)
#turtle.end_fill()
x = turtle.xcor()
y = turtle.ycor()
turtle.setposition(0,0)
turtle.up
turtle.setposition(x,y)

#Now, we would like to print the pie segments with the arc angles
for i in range(len(arcs)):
    
    r = random.randint(0,255) #Rand() rbg colors
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    turtle.begin_fill()
    turtle.color(r,g,b)
    turtle.circle(200,arcs[i])
    
    x = turtle.xcor()
    y = turtle.ycor()
    
    turtle.down()
    turtle.setposition(0,0)
    turtle.up()
    turtle.end_fill()
    turtle.setposition(x,y)
    
