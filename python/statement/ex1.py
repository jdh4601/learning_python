def add_many(*args):
    result = 0
    for i in args:
        result += 1
    return result

print(add_many(1, 2, 3, 4))
    
def say_myself(name, old, gender):
    print('my name is %s' %name)
    print('I;m %d years old' %old)
    if gender == 'man':
        print('man')
    else:
        print('woman')
say_myself('Jayden', 21, 'man')

# 함수호출 없음 -> return을 해야한다. or 함수호출해야한다.
def lead_name(name):
    if name == 'Jayden':
        print(name)
      
variable = lead_name('Jayden')
print(variable)