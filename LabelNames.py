import turtle
import random

arcs = [10,20,30,60,120,80]       #list of angles
#arcs = [50,60,30,60,10,80]
#arcs = [120,70,130]
label  = ['a','b','c','d','e', 'f'] #list of labels

#col  = ["limegreen","aqua","moccasin","purple","darkred","yellow","skyblue"]
#Initialize circle of 200 radius with center(0,0)
x = 0
y = 0
turtle.colormode(255) #so we can randomize the RGB colors for the arc segments
turtle.speed(1) #speed ranges from 0 to 10, 10 being the fastest, 0 no animation

turtle.up()
turtle.setposition(0,-200)
turtle.down()
#turtle.begin_fill()
turtle.pencolor("white")
turtle.circle(200)
#turtle.end_fill()
x = turtle.xcor()
y = turtle.ycor()
Ang = turtle.heading()

inX   = turtle.xcor()#help us draw the labels
inY   = turtle.ycor()
inAng = 270

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
    turtle.circle(200,arcs[i])  #Creates the arc of arcs[i] degreess
    
    x = turtle.xcor()
    y = turtle.ycor()
    Ang = turtle.heading()      #Save end point and angle for the next segment
    
    turtle.down()
    turtle.setposition(0,0)     #Go to center to complete a slide of the pie
    turtle.up()
    turtle.end_fill()
    
    turtle.setposition(inX,inY) #Goes back to begining of the arc
    turtle.setheading(inAng)    #Sets the direction for label line
    
    turtle.down()
    if i%2 == 0:            #to avoid label overlapping at its best (wanted to avoid making a bigger circle)
        turtle.forward(200) #even numbers lines are longer
    else:
        turtle.forward(150) #odd number lines are shoter
        
    turtle.up()
    turtle.forward(20)  #moves 20 units to set free space away from line
    turtle.down()
    
    turtle.write(label[i] + " 0.1111",False,"center",("Arial",10,"normal"))
    turtle.up()

    turtle.setposition(x,y)     #Go to the saved point for next arc
    inX   = turtle.xcor()       #Saved those points again
    inY   = turtle.ycor()
    
    if inAng + arcs[i] >= 360:
        inAng =(inAng + arcs[i]) - 360
    else:
        inAng = inAng + arcs[i]
        
    turtle.setheading(Ang)      #Reset heading after drawing label line
    



