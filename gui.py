#----------------------------------------------------------
# Developer ----- Bryce Martin
# Description --- This program will use tkinter; a python
#                 library that is used to create a GUI.
#----------------------------------------------------------

#tkinter is a python built in library
from tkinter import *

#opens a window
window = Tk()

#button function for tkinter
b1 = Button(window, text='Execute')
b1.grid(row=0,column=0) #widget method

e1 = Entry(window)
e1.grid(row = 0, column=1)

t1 = Text(window,height=1,width=20)
t1.grid(row=0,column=2)

#this should always be at the end of the code. it will allow us to close when we want
window.mainloop()