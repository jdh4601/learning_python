#1
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
    
print(is_odd(2)) 
is_odd = lambda x : True if x % 2 == 1 else False

#2
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

#3
input1 = input("첫번째 숫자를 입력하세요: ")
input2 = input("두번째 숫자를 입력하세요: ")

total = int(input1) + int(input2)
print("두 수의 합은 %d입니다." %total)

#4 3번

#5
f1 = open("test1.txt", 'w', encoding="UTF-8")
f1.write("you need java.")
f1.close()

f2 = open('test1.txt', 'r')
print(f2.read())
f2.close()

#6
user_input = input("Enter a number: ")
f = open('test1.txt', 'a')
f.write(user_input)
f.write("\nHi my name is Jayden!")
f.close()

#7
f = open('test1.txt', 'r')
body = f.read
f.close()

body = body.replace('java', 'Python')

f.open('test1.txt', 'w')
f.write(body)
f.close()
