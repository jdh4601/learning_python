# with as
# f라는 local변수를 생성한 후, 그곳에 파일을 넣는다.

with open("hello.txt", 'w') as f:
    f.write("Fake it till you make it!")