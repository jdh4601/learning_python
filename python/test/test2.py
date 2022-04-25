# 1 (o)
class Calculator:
  def __init__(self):
    self.value = 0
  def add(self, val):
    self.value += val

'''class UpgradeCalculator(Calculator):
  def minus(self, val):
    self.value = self.value - val'''
    
'''cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)'''

# 2 클래스 상속 + 메소드 오버라이딩 -> (x)틀림
# 💩
class MaxLimitCalculator(Calculator):
  def add(self, val):
    self.value += val
    if self.value > 100:
      return 100 # ???
# 👍
class MaxLimitCalculator(Calculator):
  def add(self, val):
    self.value += val
    if self.value > 100:
      self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value) 

# 3 (o)
'''a = all([1, 2, abs(-3)-3])
print(a)
b = chr(ord('a')) == 'a'
print(b)'''

# 4 (x)
'''def positive(x):
  return x > 0
a = list(filter(positive, [1, -2, 3, -5, 8, -3]))
print(a)
# 👍 filter(함수이름, 재사용할것)
a = list(filter(lambda x : x>0, [1, -2, 3, -5, 8, -3]))
print(a)
# 💩 lambda함수의 복잡도를 높이지 말기
positive = lambda num = [1, -2, 3, -5, 8, -3] : list(filter(num)) if num > 0 else num
print(positive)'''

# 5 (o)
'''x = hex(234)
print(x)
y = int('0xea', 16)
print(y)'''

# 6 (o)
'''def multiple(n):
  return n * 3

target = [1,2,3,4]
result = []

for i in target:
  result.append(multiple(i))
print(result)'''

# map사용하기
'''target = [1, 2, 3, 4]
result = map(lambda x : x * 3, target)
print(list(result))

# 7 (o)
list = [-8, 2, 7, 5, -3, 5, 0, 1]
print(min(list))
print(max(list))

# 8 (o)
x = round(17/3, 4)
print(x)'''

# 9 (x)
'''import sys
# 파일 이름을 제외한 명령 행의 모든 입력
numbers = sys.argv[1:]
result = 2
for number in numbers:
  result += int(number)
print(result)'''

# 11 (o)
'''import glob
glob.glob('python/*.py')
a = glob.glob('test/*.py')
print(a)
b = glob.glob('python_fly/ex?.py')
print(b)'''

# 12 ()
import time
a = time.asctime(time.localtime())
print(a)



