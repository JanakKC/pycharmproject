x = [10, 3, 4, 1, 30, 20]
total = sum(x)
print(total)

# 2. Write a program to find the largest and smallest item in the list.
a = [10, 3, 4, 1, 30, 20]
largest = max(a)
smallest = min(a)
print("largest", max(a))
print("smallest", min(a))






x = [4, 3, 7, 3, 5]
y=[]
for a in x:
    if a not in y:
        x.append(a)
print(y)