#----------------------------------------------------------
# Developer ----- Bryce Martin
# Description --- This program will use tkinter; a python
#                 library that is used to create a GUI.
#----------------------------------------------------------

#tkinter is a python built in library
from tkinter import *

#opens a window
window = Tk()

def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END,miles) #will insert this into t1

def convert():
    grams = float(e2_value.get())*1000
    pounds = float(e2_value.get())*2.20462
    ounces = float(e2_value.get())*35.274

    t2.insert(END,grams)
    t3.insert(END,pounds)
    t4.insert(END,ounces)

#button function for tkinter
b1 = Button(window, text='Execute', command=km_to_miles)
b1.grid(row=0,column=0) #widget method


e1_value = StringVar() #takes user input
e1 = Entry(window, textvariable=e1_value)
e1.grid(row = 0, column=1)

t1 = Text(window,height=1,width=20,border=1)
t1.grid(row=0,column=2)

#---------------------------
#practice - more conversions
#---------------------------

kg = Label(window, text="Kg")
kg.grid(row=1,column=0)

e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=1,column=1)

b2 = Button(window,text="Convert",command=convert)
b2.grid(row=1,column=2)

t2 = Text(window,height=1,width=20)
t2.grid(row=2,column=0)

t3 = Text(window,height=1,width=20)
t3.grid(row=2,column=1)

t4 = Text(window,height=1,width=20)
t4.grid(row=2,column=2)


#this should always be at the end of the code. it will allow us to close when we want
window.mainloop()