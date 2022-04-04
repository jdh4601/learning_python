num = 0
marks = [90, 98, 70, 80]
for mark in marks:
    num += 1
    if mark <= 70:
        continue
    print("%d" %num)