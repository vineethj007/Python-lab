file_name = input("Enter file name : ") 
try: 
    file = open(file_name) 
    scores = [] 
    for line in file: 
        line = line.split(' ') 
        line = list(map(int, line)) 
        scores += line 
    total = 0 
    for score in scores: 
        total += score 
    print("Total score : ", total) 
    print("Average score : ", total / len(scores)) 
except FileNotFoundError: 
    print("file not found")