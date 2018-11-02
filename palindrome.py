'''
Created on 24-Oct-2018

@author: vinee
'''
def isPalindrome(s): 
    # Calling reverse function 
    # Checking if both string are equal or not 
    if (s == s[::-1]): 
        return True
    return False
  
# Driver code 
s = input("Enter the string to be checked:")
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No") 