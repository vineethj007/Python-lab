'''
Created on 28-Oct-2018

@author: vinee
'''
from tkinter import *
class DrawArea(Frame):
    def __init__(self): 
        super().__init__() 
        self.canvas = Canvas(self, width=300, height=200)
        self.canvas.pack()
    def draw_rect(self, filled): 
        if filled:
          self.canvas.create_rectangle(10, 10, 250, 200, fill="cyan") 
        else:
         self.canvas.create_rectangle(10, 10, 250, 180)
    def draw_oval(self, filled): 
        if filled: 
            self.canvas.create_oval(10, 10, 200, 100, fill="cyan") 
        else: 
            self.canvas.create_oval(10, 10, 200, 100) 
class MainWindow: 
    def __init__(self): 
        self.root = Tk() 
        self.draw = DrawArea()
        self.draw.pack() 
        self.shape = IntVar() 
        self.filled = BooleanVar() 
        Radiobutton( self.root, text="Rectangle", variable=self.shape, value=1, command=self.shape_select).pack() 
        Radiobutton( self.root, text="Oval", variable=self.shape, value=2, command=self.shape_select).pack() 
        Checkbutton( self.root, text="filled", variable=self.filled, onvalue=True, offvalue=False, command=self.shape_select ).pack() 
        self.root.mainloop() 
    def shape_select(self): 
            self.draw.canvas.delete(ALL) 
            if self.shape.get() == 1: 
                self.draw.draw_rect(self.filled.get())
            else: 
                self.draw.draw_oval(self.filled.get())
MainWindow()