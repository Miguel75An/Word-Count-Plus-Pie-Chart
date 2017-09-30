try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

win = Tk()
b1 = Button(win,text="lol")
b2 = Button(win,text="lol2")

##b1.pack() #top of each other, default
##b2.pack()

##b1.pack(side=LEFT) #top of each other, default
##b2.pack(side=RIGHT)

b1.grid(row=0,column=0)
b2.grid(row=1,column=1)

l = Label(win,text="Lol LABEL")
l.grid(row=0,column=1)

def but1():
    print("LOl 1 key button")

b1.configure(command=but1)
