'''
Created on 30-Oct-2018

@author: vinee
'''
import pymysql
from tkinter import *
import tkinter as T
import tkinter.messagebox
import tkinter.simpledialog

class DBUI:
    def __init__(self,db):
        self.db = db 
        self.root = Tk()
        
        self.name = StringVar()
        self.usn = StringVar() 
        self.age = IntVar() 
        self.branch = StringVar()
        
        Label(self.root,text="Name").grid(row=0,column=0)
        Entry(text=self.name).grid(row=0, column=1) 
        Label(text="Enter USN : ").grid(row=1, column=0) 
        Entry(text=self.usn).grid(row=1, column=1) 
        Label(text="Enter Age : ").grid(row=2, column=0) 
        Entry(text=self.age).grid(row=2, column=1) 
        Label(text="Enter Branch : ").grid(row=3, column=0) 
        Entry(text=self.branch).grid(row=3, column=1) 
        Button(text="Insert", command=self.insert).grid(row=4, column=0) 
        Button(text="Search", command=self.search).grid(row=4, column=1) 
        self.root.mainloop()
        
    def insert(self): 
            try: 
                cursor = self.db.cursor() 
                query = "INSERT INTO stu values('%s', '%s', %d, '%s');" % (self.name.get(), self.usn.get(), self.age.get(), self.branch.get()) 
                print(query) 
                cursor.execute(query)
                self.db.commit() 
                tkinter.messagebox.showinfo("Success", "Inserted!")
            except Exception as ex: 
                tkinter.messagebox.showerror("Insert Error", ex) 
    def search(self): 
            try: 
                usn_inp = T.simpledialog.askstring("Search", "Enter USN to search")
                cursor = self.db.cursor() 
                query = "select * from stu where usn = '%s';" % (usn_inp) 
                print(query)
                
                cursor.execute(query)
                
                if cursor.rowcount == 0: 
                    raise Exception("No student of that USN found") 
                else: result = cursor.fetchone() 
                show_string = "Name : " + result[0] + "\n" 
                show_string += "USN : " + result[1] + "\n" 
                show_string += "Age : " + str(result[2]) + "\n" 
                show_string += "Branch : " + result[3] + "\n" 
                tkinter.messagebox.showinfo(usn_inp, show_string) 
            except Exception as ex: 
                tkinter.messagebox.showerror("Not found", ex)
                
connection = pymysql.connect(host='localhost', user='root', password='', db='student')
DBUI(connection)    
