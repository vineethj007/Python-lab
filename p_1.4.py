str=input("Enter string")
str=str.split(',')
str.sort()
print('Sorted list is:')
for i in str:
    print(i,end=',')
