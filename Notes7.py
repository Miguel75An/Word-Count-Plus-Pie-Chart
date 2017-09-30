
import sys

import os


print("a","b",end = 'c')

print("a", "b", "c", 2, 3, sep = "\n")

print("a", "b", "c", 2, 3, sep = " doge ")

print("a", "b", sep = " ", end = "\n", file = sys.out)

file1 = open ("trial.txt", "w")
print("Im Phyton", file = file1)

os.getcwd()

File1.close()

#any extension

##################

f = open("personalinfor.txt", "w")

print("Mike lol", file = f)
print("NYC", file = f)
print("CCNY", file = f)
print("Lool", file = f, Flush = True)
f.close()


ths = open ("prices.txt","w")
ths.write("earphones: $30.00\n") #returns amount of characters written in prices file
ths.write("laptops: $1000.00")'

ths.open("princes.txt", "r")
read()
readline()
readlines()
ths.read()
print(ths.read())

list = this.readlines()


phones = open("phones.txt", "r")

print(phones.readline())
#Prints A:1234

Phones.close()

with open("phonebook.txt", "r") as fil:
    print(fil.read())


f.read()
f.seek(0) #takes u to that byte
f.tell() #this byte

f.seek(f.tell())

f = open("filename", "a") //apend a
with open("phonebook.txt", "a") as f:
    f.write("\nZ: 0123")


with open("phonebook.txt") as f:
    record = f.read()
    f.seek(0)
    f.write("G:0458\n" + record)


with open("phonebook.txt", "r+") as f:
    record = f.readlings()
    



