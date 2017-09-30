try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
win = Tk()

win.wm_title("Magic Frequency Box")

la = Label(win,text="Enter a 'n' integer for the number of 'n' frequent words.")
la.pack()

v = StringVar()
e = Entry(win,textvariable =v)
e.pack()

b1 = Button(win,text="Start PIE")
b1.pack()

def but1():
    print(v.get())
b1.configure(command=but1)
