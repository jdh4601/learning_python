# Loop(while)

# break
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("number %d trees." % treeHit)
    if treeHit == 4:
        print("The end.")
        break
    
# continue
age = 10
while age < 20:
    age += 1
    if age % 8 == 0: 
        continue
    print("I'm %d years old." %age)
    
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
     