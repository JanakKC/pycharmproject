# 2. Write a program to find the largest and smallest item in the list.
x = [10, 7, 5, 17, 3]
lengthx = len(x)
counter = 0
while counter < lengthx:
    if counter != 0:
        if x[counter] > no1:
            no1 = x[counter]
        else:
            pass
    else:
        no1 = x[counter]
    counter += 1
print(no1)



x = [6, 5, 4, 3, 6, 4]
new = []
for i in x:
    if i not in new:
        new.append(i)
print(new)
