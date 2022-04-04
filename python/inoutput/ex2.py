# 파일 생성하기, 쓰기, 읽기
# 'w'모드로 완전히 새롭게 추가
# write()함수 이용해서 파일 쓰기
f = open("new_file.txt", 'w', encoding="UTF-8")
for i in range(1, 11):
    data = "%d번째 줄이다.\n" % i
    f.write(data)
f.close()

# readline()함수 이용해서 파일 한줄 읽기, 무한루프 이용
f = open("new_file.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# readlines()함수 이용해서 파일 모두 읽기, 리스트 형태로 들어감
f = open("new_file.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line, end='')
f.close

# 'a' 추가모드 : 기존 파일 그대로에 추가
f = open("new_file.txt", 'a')
for i in range(1, 5):
    text = "%dth number!!\n" %i
    f.write(text)
f.close()

# read()함수 이용해서 통째로 읽기, 띄어쓰기 x
f = open("new_file.txt", 'r')
data = f.read()
print(data)
f.close()