'''
Created on 30-Oct-2018

@author: vinee
'''
from tkinter import * 
root = Tk() 
canvas = Canvas(root, width=400, height=400) 
canvas.pack() 
#encloses circle in bound rectangle 
bound = 50, 50, 300, 300 
#draws 30degree arcs from angles 0, 90, 180, 270 
for i in [0, 90, 180, 270]: 
    canvas.create_arc(bound, start=i, extent=30, fill="red") 
canvas.pack() 
root.mainloop()