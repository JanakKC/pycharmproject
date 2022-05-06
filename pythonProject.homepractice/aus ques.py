x = 10
list = [4, 10, 7, 8, 9]

if x in list:
    print("it is present")

x = 10
count = 0
list = [4, 10, 7, 8, 9]
for y in list:
    count += 1
    if x == y:
        print("x is present")
        break
    else:
        if count == len(list):
            print("it is not present")

