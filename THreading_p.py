'''
Created on 31-Oct-2018

@author: vinee
'''
import threading
def palin(str):
    if str==str[::-1]:
        print("Plaindrome")
        return 
    print("Not a palindrome")
def vow(str):
    v={'A','E','I','O','U','a','e','i','o','u'}
    c=0
    for char in str:
        if char in v:
            c=c+1
            
    print("The number of voewles in string is:",c)
def main():
    s=input("Enter String")
    t1=threading.Thread(target=palin,args=(s,))
    t2=threading.Thread(target=vow,args=(s,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done")
main()