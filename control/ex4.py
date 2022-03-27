for i in range(2, 10):
    for j in range(1, 10):
        print(i * j)
    print('')
    
# list, for
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num+2)
print(result)

result = [num + 2 for num in a if num % 2 == 0]
