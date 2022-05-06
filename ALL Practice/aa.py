x = [3, 55, 66, 1, 0]
lengthx = len(x)
count1 = 0
while count1 < lengthx:
    if count1 == 0:
        no1 = x[count1]
    else:
        if x[count1] <= no1:
            pass
        else:
            no1 = x[count1]
    count1 += 1
print(no1)
