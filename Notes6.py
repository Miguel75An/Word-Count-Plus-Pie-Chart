For loop: we need to know exactly how many times it willl run before running the progrsam

n = input
for i in range(n)

Indefinite Loops
    while loops

    structure:

        while <condition> :
            <body>

condition: can be a boolean expression
body: a set of sequences or 1 or more

transform for i in range(10): //ten is exclusive
    print(i)

output:
    0
    1
    2
    3
    .
    .
    .
    9
i = 0
while i < 10:
print(i)
i = i + 1

=============

interactive loops: it allows the user to repeat a certain portion of a program


==================

set a string moredata to  "yes"
while moredata is "yes"
    get the next data ite
    procress the item
    ask the user if there is more data

=============

sum_ = 0.0
count = 0
moredata = "yes"

while moredata == "yes":
    x = float(input("Insert a float number"))
    sum_ = sum_ + x
    count =  count + 1

    moredata = input("Do you have more numbers??? yes or no")

print("The average is", sum_/count)

====================

while moredata[0] == "y" or moredata[0] == "Y":

============

Sentinel loops:
    sentinel data: distinguishable from the actual data

=========

def main():
        sum_ 0.0
        count = 0
        x = float(input("insert number or -1 to exit")

        while x >= 0 :
                  coun = count + 1
                  sum_ sum_ + x
                  x = float(input.....)

        if count > 0:
                  print("the average...")
        else:
                  print("no value")
====================

sentinel data "\"

def main():
        sum = 0.0
        count = 0
        xString = input ("Enter a number <enter> to quit")

        while xString != ""
                  x = Float(xString)
                  sum = sum + x
                  count = count + 1

==================

terminate the loop: break statement, halts the loop in certain parts

number = -1

while number < 0:
        number = float(input("enter positive number"))

while True
        number float(Input("enter positive number") = -1
        if number >= 0:
                     break;

===================

if x <= 0:
    break
    x == ""

===============

PASS: pass or ignore this part of the body

while True
    x = int(input("enter a number"))

    if x == 0:
        break;
    elif x < 0:
        pass
    else:
        print(x)

=======================

a number with maximum 3 digits

    if s == "cancel":
        break;
    elif: len(s) < 4
        continue
    elif: len(s) > 3
        pass
    
                  
