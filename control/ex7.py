scores = [90, 80, 85, 95]

number = 0
for score in scores:
    number += 1
    if score < 85: continue
    print("congratulation %d!!" %number)
    
for i in range(1, 101):
    print(i)