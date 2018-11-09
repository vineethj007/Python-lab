str=input("Enter string")
d=0
l=0
for i in str:
    if i.isalpha():
        l+=1
    if i.isdigit():
        d+=1
print('Number of digits : ',d)
print('Number of letters :',l)
