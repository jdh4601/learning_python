# List
num = [1, 2, 3, 4, 5, [300, 400, 500]]
print(num[0])
print(num[0]+num[2])
print(num[5])
del num[1]
num[2] = 7
print(num)

num.append(8)
print(num)
print(num[4][1])
print(num[0:2])
print(num.extend([3, 4]))