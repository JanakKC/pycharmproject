a = [2, 3, 44, 6, 11, 32]
lengtha = len(a)
count = 0
counter = 0
while lengtha > count:
    if count == 0:
        no1 = a[count]
    else:
        if a[count] > no1:
            no1 = a[count]
        else:
            pass
    if counter == 0:
        no2 = a[counter]
    else:
        if a[counter] < no2:
            no2 = a[counter]
        else:
            pass

    count += 1
print(no1)
print(no2)

