from tkinter import *
import math
from bokeh.layouts import column

class MainWindow:
    def __init__(self):
        self.root=Tk()
        self.root.title("Account")
        self.invest_amnt = DoubleVar() 
        self.intrest_rate = DoubleVar()
        self.years = DoubleVar()
        Label(self.root,text="Investment amount").grid(row=0,column=0)
        