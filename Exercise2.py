#MIGUEL DOMINGUEZ
#09/20/16
#CSC113
#EXERCISE 2

#########PART 1############
# QUESTION A

#A function is a sequence of statements that can be used many times and they are used to
#accomplish many operations and tasks.It's components are parameters, statements, returs, loops.
#In general functions take inputs and also return outputs

# QUESTION B

#Some type conversion functions that we find in Phyton are str(32)
# also int(5.0) float(10)

# QUESTION C

#Module Objects are classes with attributes, fuctions and values that a program can have
# access to or a reference too. Module Objects provide utilities and tools such as the math library.
#To use them we need to import them first.

# QUESTION D

#Local variables are variables that are subject to a specific scope such as the scope of a function
# they store values that belong to the body of the function only, and they cannot be accessed by other functions outside that scope
#Void functions are functions that return null or return a value not in the domain. SOme of those are exit() or print()

#QUESTION E

# The output would be '2.0'


#########PART 2############

#PART A converint minutes to milliseconds

def minsToMil(minutes):
    Milliseconds = (60000)*minutes
    return Milliseconds

#for example print(minsToMil(2)) will print 120000

#PART B calculate volume of a square based pyramid

def volumePir(side, height):
    volume = ((side*side)*(height))/3
    return volume

#Example: volumePir(5,10) gives us 83.333333....

#PART C Average of 2 exams

def average(score1, score2):
    average = (score1 + score2)/2
    return average

#Example: average(100, 200) gives us 150.0

#PART D math module for SQRT()

from math import*

#import math --> also an option

def root1(a, b, c):
    root1 = (((-1)*b) + sqrt((b*b) - (4*a*c)))/(2*a)
    return root1

def root2(a, b, c):
    root2 = (((-1)*b) - sqrt((b*b) - (4*a*c)))/(2*a)
    return root2

#Example: The two roots for an quadratic equation with coefficients a = 2, b = 6 and c = 1
#           gives us root1(2,6,1) = -0.17712434446770464
#                    root2(2,6,1) = -2.8228756555322954

#PART E Speed Problem

def averageSpeed(kilometers1, hours1, kilometers2, hours2):
    average = ((kilometers1*hours1 + kilometers2*hours2)/(hours1 + hours2))*(1000/(60*60))
    return average

#Example: For speeds 40km/h and 60km/h and 2 and 3 hours respectively we calculate that as averageSpeed(40,2,60,3) = 14.444444444444445

#PART F Function to convert Kelvin to Reamur to Celsious 

def KelvinToReaumur(kelvin):
    reaumur = (kelvin - 273.15)*(0.80000)
    return reaumur

def ReaumurtoCelsius(reaumur):
    celsius = reaumur/0.80000
    return celsius

#Example to make a conversion using our TWO functions and we want to convert Kelvin to Celsious
#we call a function inside another one such as ReaumurtoCelsius(KelvinToReaumur(90)) = -183.14999999999998

#Part G Rectangular Prism

def fitR(a):
    prismVol = a*(8*a)*(9*a)
    cubeVol = (2*a)*(2*a)*(2*a)

    return prismVol/cubeVol

#Example when a = 5 , fitR(5) = 9

#Part H Marbles and Cubes

def cubeVol(n):
    return n*n*n

def marbleVol(n):
    radio = n/4
    
    return (radio*radio*radio)*(4/3)*pi

def fitMarble(n):
    return cubeVol(n)/marbleVol(n)

#Example: for n = 5, fitMarble(5) = 15.278874536821952 About 15 marbles can fin in the cube

#PART I Printing Graph 
def MyPrinter():
    print("^-^-^^-^-^^-^-^^-^-^^")
    i = 3
    while i >= 0:
        print("i    i    i    i    i")
        print("i    i    i    i    i")
        print("i    i    i    i    i")
        print("i    i    i    i    i")
        print("^-^-^^-^-^^-^-^^-^-^^")
        i = i -1

#THIS WILL PRINT THE REQUIRED OUTPUT
        
