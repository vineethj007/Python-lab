'''
Created on 24-Oct-2018

@author: vinee
'''
n = int(input("Enter the number of terms : "))
if( n <= 0):
  print("Number of terms should be greter than 0")
print("Fibonacci Series : ")
if( n == 1):
  print("0")
a,b,c = 0,1,0
for i in range(n):
  print(a,end=" ")
  c=a+b
  a,b = b,c