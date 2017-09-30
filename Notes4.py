#Notes 4

#code injection attack (way of hacking)

#two input fuctions: raw-input()(only phyton 3 // return string and input() returns string always

#simultaneous assigment:

# <var1>,<var2>,......=<expr>,<expr>....

# sum, diff, aa = x+1, x-1, (x+1/2)

def f():
    a,b,c = eval(input("please enter the value")) #insert in this way numbers 4,5,6 dont forget the coomans
    print(a,b,c)

def x():
     a,b,c,d = eval(input("please enter the value")) #insert in this way numbers 4,5,6,"dog" dont forget the coomans
     print(a,b,c,d)

                 
#x,y,z = 1,2 VALUE ERROR NOT ENOUGHT VALUES
#x,y = 1,2,3 TOO MANY VALUES

###Standard data types
     #number int, complex, float
     #(-2 billion, +2billion) integer range 4bytes

    #no boundaries for integners a = maxsize 19 digits
     # a*a  36 digits
     #a*a*a still gives ur an bigger number


#  a = Float("inf")
#  inf - inf = nan

# A = -0x260 that prints -608 since we got hexanumbers
# int(3.9) = 3 truncates
#round(3.9) = 4
#ceeling(3.1) = 3 not 4!!!!

#round(3.999999, 3) // round 3 places
# that gives us 3.5

# 2.6525589e + 32 = 2.652553565 * 10^32 //the little e makes the value FLOAT

# real, floating point number and an imaginary part 3+4j , 3 + j (write j instead of i)

# -.6545 + 0j

# complex(real, imaginary (write j))

# from math import *
# sqrt(x), p, exp(x), e,, sin(x), cos(x), tan(x), asin(x), acos(x), atan(x), log(x), log10(x), log(x, base)
# pow(x,2)

#STRINGS +, * , [], can split string, get a specific char

#LIST like arrays

list = ['abcd',768, 2.0,"chon"]

# TUPLES tuple = ("abcd", 768,......) not dynamic, read only

#DICTIONARY : consists key value pairs, key value can by phton type
#               values are the objects

dict = {}
dict = {'one'} = "this is one"
dict = {z} = "this is true






