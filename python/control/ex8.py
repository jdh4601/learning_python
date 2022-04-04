# list 
# ..for..in..if..
# 표현식 for 변수 in 반복가능객체 if 조건문
a = [1, 2, 3, 4]

result = []
for num in a:
	result.append(num*3)
print(result)

result = [num*3 for num in a]
print(result)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(last * first)
    print(last // first)
    print(last % first)
    
numbers = [1,2,3,4]
result = [num*3 for num in numbers if num > 1]
print(result)