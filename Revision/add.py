def sum(a):
    total = 0
    for x in a:
        total += x
    return total


y = sum([1, 2, 3, 4, 5])
print(y)

# REverse the list


x = [3, 4, 7, 8, 2]
y = []
length = len(x)
while length > 0:
    y.append(x[length - 1])
    length = length - 1
print(y)

# to find the sum
x = [3, 4, 7, 8, 2]
total = 0
for i in x:
    total = total + i
print(total)

x = [1, 2, 3, 45]
length = len(x)
y = []
while length > 0:
    y.append(x[length - 1])
    length = length - 1
print(y)

# Write a program to find those numbers divisible by 7 and multiple of 5 between 1500 and 2700

count = []
for x in range(1500, 2700):
    if (x % 7 == 0) and (x % 5 == 0):
        count.append(str(x))
print(count)


def word_from_letter(letters, words):
    count = 0
    for i in letters:
        if i in words:
            if (letters.count(i) == words.count(i)):
                count += 1
        else:
            count -= 1
    if count == len(letters):
        x = True
    else:
        x = False
    return x


y = word_from_letter("ram", "arm")
print(y)
