# 1 (o)
pin = '881120-106832'
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)
print(pin[7]) 

# 2 (o)
a = 'a : b : c : d'
b = a.replace(':', '#')
print(b)

# 3 (o)
a = [1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)

# 4 (o)
a = ['Life is too short']
result = "".join(a)
print(result)

# 5 (x)
a = (1, 2, 3)
a = a+(4, ) 
print(a)

# 6 (o)
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

# 7 (o)
a = [1,1,2,2,3,3,3,4]
aSet = set(a)
b = list(aSet)
print(b)

# 8 (o)
a = b = [1,2,3]
a[1] = 4
print(b)