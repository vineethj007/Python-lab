'''
Created on 28-Oct-2018

@author: vinee
'''
def binser(sortl,item):
    lower,upper=0,len(sortl)-1
    while lower<=upper:
        mid=(lower+upper)//2
        mid_item=sortl[mid]
        if item == mid_item:
            return mid + 1 
        if mid_item >item: 
            upper = mid - 1 
        else:
            lower = mid + 1
    return -1 
sorted_list = input("Enter list items [in sorted order] : ") 
search_item = int(input("Enter the element to search : ")) 
sorted_list = sorted_list.split(' ') 
sorted_list = list(map(int, sorted_list)) #converts elements from string to integers 
result = binser(sorted_list, search_item)
if result is -1: 
    print("Element not found") 
else:
    print(search_item, "found at position ", result)
    
    