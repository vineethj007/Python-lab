'''
Created on 27-Oct-2018

@author: vinee
'''
def get_caps_only(string1, string2): 
    res = "" 
    merge = string1 + string2
    for char in merge: 
        if char.isupper():
             res += char 
    return res 
string1 = input("Enter first string : ") 
string2 = input("Enter second string : ")

print("Mergeg Strings",get_caps_only(string1, string2))