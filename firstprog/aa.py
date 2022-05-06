# Write a program to print the sum of numbers from 1 to 10

x = 0
y = 0
while x < 10:
    x = x + 1
    y = x + y
print(y)

# Write a program to count the number of even and odd numbers from 1 to 100

even = odd = 0
x = 0
while x < 100:
    x = x + 1
    if x % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("odd:", odd)
print("even:", even)

# write a program that prints all the numbers from 1 to 10 except 2 and 5

x = 0
while x < 10:
    x = x + 1
    if x == 2 or x == 5:
        pass
    else:
        print(x)
