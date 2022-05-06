x = 0
y = 0
while x < 10:
    x = x + 1
    y = y + x
print(y)

even_count = odd_count = 0
x = 0
while x < 100:
    x = x + 1
    if x % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("even", even_count)
print("odd", odd_count)

x = 0
while x < 10:
    x = x + 1
    if x == 2 or x == 5:
        pass
    else:
        print(x)
