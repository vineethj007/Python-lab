l=[]
print("Enter lines")
while True:
    str=input(">")
    if not str:
        break
    l.append(str.upper())
for i in range(0,len(l)):
    print(">"+l[i])
        
  
    