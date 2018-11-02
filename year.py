'''
Created on 29-Oct-2018

@author: vinee
'''
def is_leap(year): 
    if year % 4 != 0: 
        return False
    if year % 100 == 0: 
        if year % 400 == 0: 
            return True
        else: 
            return False 
    else: 
        return True 
def numberOfDaysInAYear(year): 
    if is_leap(year): 
        return 366 
    else: 
        return 365
#test 

for i in range(2010, 2021): 
    print("There are ", numberOfDaysInAYear(i), " days in ", i)