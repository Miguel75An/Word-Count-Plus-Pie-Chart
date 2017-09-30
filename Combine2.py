import turtle
import random


dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0,'g':0, 'h':0,'i':0, 'j':0,'k':0, 'l':0,'m':0, 'n':0,'o':0,
        'p':0, 'q':0,'r':0, 's':0,'t':0, 'u':0,'v':0, 'w':0,'x':0, 'y':0,'z':0, 'A':0,'B':0, 'C':0,'D':0, 'E':0,
        'F':0, 'G':0,'H':0, 'I':0,'J':0, 'K':0,'L':0, 'M':0,'N':0, 'O':0,'P':0, 'Q':0,'R':0, 'S':0,'T':0, 'U':0,
        'V':0, 'W':0,'X':0, 'Y':0,'Z':0, '0':0,'1':0, '2':0,'3':0, '4':0,'5':0, '6':0,'7':0, '8':0,'9':0,
        '\n':0, ' ':0,'!':0, '"':0,'#':0, '$':0,'%':0, '&':0,'\'':0, '(':0,')':0, '*':0,'+':0, ',':0,'-':0, '.':0,
        '':0,'/':0, ':':0,';':0, '<':0,'=':0, '>':0,'?':0, '@':0,'[':0, '\\':0,']':0, '^':0,'_':0, '`':0, '~':0,'\t':0,
        '{':0,'|':0,'}':0} 

counter = 0

with open("Words.txt") as f:
  while True:
    c = f.read(1)
    dict[c] = dict[c] + 1
    counter = counter + 1
    #print(dict[c])
    
    if not c:
      print("End of file")
      break
   
#find n times most frequent character
n = 3

label = []    #list of labels
frequency = []
   
#We are planning to find the n most frequent letters
for i in range(0,n):
    maxval = 0
    maxkey = ""
    for key,value in dict.items():
        if value > maxval:
            maxval = value
            maxkey = key
    label.append(maxkey)
    frequency.append(maxval)
    
    #delete current max key and max value
    del dict[maxkey]
   
#We need to the probabilities based on the frequencies
probabilities = []
for i in range(0,n):
    probabilities.append(round(frequency[i]/counter,4))

#We need to find the arc's angles based on the probabilities
arcs = []   #list of angles
for i in range(0,n):
    arcs.append(round(probabilities[i]*360,0))

#Find sum of n probabilities in order to get probability of "others"
sums = 0
angles = 0
for i in probabilities:
    sums = sums + i
othersprob = 1 - sums
#Find angle of "others"
for i in arcs:
    #print(i)
    angles = angles + i
othersang = 360 - angles
#print(othersprob," ",othersang)

#-----------------------#
#-----INTRODUCTION------#
#-----------------------#
turtle.up()
turtle.setposition(-700,300)
turtle.pencolor("blue")
turtle.write("MIGUEL DOMINGUEZ",False,"center",("Helvetica",15,"bold"))         #Writes name and class
turtle.setposition(-700,280)
turtle.write("CSC 11300" ,False,"center",("Helvetica",15,"bold"))
turtle.setposition(-700,260)
turtle.write("Programming Languages" ,False,"center",("Helvetica",15,"bold"))
#-----------------------#
#-------PIE CHART-------#
#-----------------------#

#Initialize circle of 200 radius with center(0,0)
x = 0
y = 0
turtle.colormode(255) #so we can randomize the RGB colors for the arc segments
turtle.speed(5) #speed ranges from 0 to 10, 10 being the fastest, 0 no animation

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

inX   = turtle.xcor()   #Help us draw the labels
inY   = turtle.ycor()
inAng = 270

turtle.setposition(0,0)
turtle.up()
turtle.setposition(x,y)

#Now, we would like to print the pie segments with the arc angles
#for i in range(len(arcs)):
for i in range(len(arcs)-1,-1,-1):
    
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
    if label[i] == '\n':
        text = "NewLine" + ":" + str(probabilities[i])  #Special cases for white spaces
    elif label[i] == '\t':
        text = "Tab" + ":" + str(probabilities[i])
    elif label[i] == ' ':
        text = "Space" + ":" + str(probabilities[i])
    else:
        text = label[i] + ":" + str(probabilities[i])
    turtle.write(text,False,"center",("Arial",10,"normal"))
    turtle.up()

    turtle.setposition(x,y)     #Go to the saved point for next arc
    inX   = turtle.xcor()       #Saved those points again
    inY   = turtle.ycor()
    
    if inAng + arcs[i] >= 360:
        inAng =(inAng + arcs[i]) - 360
    else:
        inAng = inAng + arcs[i]
        
    turtle.setheading(Ang)      #Reset heading after drawing label line
    
#Finally we handle the case for "other" letters separately
turtle.setheading(inAng)
turtle.pencolor("black")
turtle.down()
turtle.forward(200)
turtle.up()
turtle.forward(20)
turtle.down()
text = "OTHERS" + ":" + str(round(othersprob,4))
turtle.write(text,False,"center",("Arial",10,"normal"))
turtle.up()
    




