f1=open("sample","r")
f2=open("copy","w")
for i in f1:
    f2.write(i)
f1.close()
f2.close()
print("File copied")