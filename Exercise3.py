#Miguel Dominguez
#Phyton CSC11300 12:30 CLASS

#A Passing score

def evaluate():
    score = int(input("Please enter your score"))

    if score >= 50:
        print("You passs")
    else:
        print("You do NOT pass")

#B Absoulte zero temperatures

def absoluteZero(letter):
    if letter == 'k' or letter == 'K':
        print("Kelvin O degree K ")
    elif letter == 'c' or letter == 'C':
        print("Celsius -273.15 degree C ")
    elif letter == 'f' or letter == 'F':
        print("Fahrenheit -459.67 degree F ")
    elif letter == 'r' or letter == 'R':
        print("Rankine 0 degree R ")
    else:
        print("Not a valid temperature sytem")
        
#C average
def average():
    num1 = int(input("Enter score 1"))
    num2 = int(input("Enter score 2"))

    av = (num1 + num2)/2

    if av >= 97:
        print("A+")
    elif av >= 93:
        print("A")
    elif av >= 90:
        print("A-")
    elif av >= 87:
        print("B+")
    elif av >= 83:
        print("B")
    elif av >= 80:
        print("B-")
    elif av >= 77:
        print("C+")
    elif av >= 73:
        print("C")
    elif av >= 70:
        print("C-")
    elif av >= 67:
        print("D+")
    elif av >= 65:
        print("D")
    else:
        print("F")
#D days numbers

def days():

    print("Print a number between 1 and 7 to represent the day")
    num = int(input("Number: "))

    if num > 7 or num < 1:
        print("Invalid")
    elif num == 1:
        print("Sunday")
    elif num == 2:
        print("Monday")
    elif num == 3:
        print("Tuesday")
    elif num == 4:
        print("Wedesneday")
    elif num == 5:
        print("Thrusday")
    elif num == 6:
        print("Friday")
    elif num == 7:
        print("Saturday")

# E Calculator

def calculator():
    op = input("Enter 'a' for addition or 's' for substraction")
    num1 = int(input("Number1: "))
    num2 = int(input("Number2: "))

    if op == 'a':
        print(num1 + num2)
    elif op == 'b':
        print(num1 - num2)


#F Prism
def prism():
    side = int(input("ENTER SIDE A: "))

    if side < 1:
        print("ERROR NEGATIVE OR ZERO VIOLATES PHYSICS")

    volume = side*(8*side)*(side*9)

    volcube = side*side*side


    fit = volume / volcube

    print("Number of fits = ", fit)

    
              
    
    
    
    
