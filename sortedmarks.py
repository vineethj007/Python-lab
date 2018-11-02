'''
Created on 30-Oct-2018

@author: vinee
'''
marks_list = { 'John': 86.5, 'Jack': 91.2, 'Jill': 84.5, 'Harry': 72.1, 'Joe': 80.5 } 
sorted_keys = sorted(marks_list, key=marks_list.get, reverse=True) 
print("Top 3 students: ") 
for student in sorted_keys[:3]: 
    print(student, " : ", marks_list[student]) 
sum = 0 
for student in marks_list: 
    sum += marks_list[student] 
print("Average mark : ", sum/len(marks_list))