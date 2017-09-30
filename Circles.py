import turtle
##print(turtle.position())
##turtle.circle(100)
##print(turtle.position())
##turtle.up()
##
##turtle.circle(100,30)
##print(turtle.position())
x = 0
y = 0

turtle.setposition(0,0)
print(turtle.position())

turtle.up()

turtle.setposition(0,-100)
print(turtle.position())

turtle.down()
turtle.circle(100)
turtle.setposition(0,0)
turtle.up()

turtle.setposition(0,-100)
inX = turtle.xcor()
inY = turtle.ycor()
inAng = 90

turtle.circle(100,30)
print(turtle.position())
print(turtle.heading())
inAng = turtle.heading()
x = turtle.xcor()
y = turtle.ycor()

turtle.down()
turtle.setposition(0,0)

turtle.up()

turtle.setposition(inX, inY)
turtle.circle(100,30/2)
turtle.setheading(270) #initial
turtle.left(30/2)


turtle.down()
turtle.forward(200)
turtle.up()

turtle.setposition(x,y)
turtle.setheading(inAng)
print(turtle.position())

turtle.circle(100,50)
turtle.down()
turtle.setposition(0,0)

#turtle.backward(200)

