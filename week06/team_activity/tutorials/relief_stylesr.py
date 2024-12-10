"""
The relief style of a widget refers to certain 
simulated 3-D effects around the outside of the 
widget. Here is a screenshot of a row of buttons 
exhibiting all the possible relief styles.
"""

from tkinter import *
import tkinter

top = Tk()

B1 = Button(top, text ="FLAT", relief=FLAT )
B2 = Button(top, text ="RAISED", relief=RAISED )
B3 = Button(top, text ="SUNKEN", relief=SUNKEN )
B4 = Button(top, text ="GROOVE", relief=GROOVE )
B5 = Button(top, text ="RIDGE", relief=RIDGE )

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
top.mainloop()
