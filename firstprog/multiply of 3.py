i = 1
j = 3
while i <= 10:
    print("{1{*{3{={1*3{".format(i, j, i * j))
    i += 1
