# lamda람다
# lambda 매개변수 : 표현식
add = lambda a, b: a + b
result = add(1, 2)
print(result)

myList = [lambda a, b: a+b, lambda x, y: x+y]
print(myList[0](1, 2))
