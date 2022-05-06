# name=["ram","shyam", "hari"]
# write a program that prints the following output

name = ["ram", "shyam", "hari"]
for x in name:
    print("hello" + " " + x)

# write a program that prints the no.of occurance of r in the word parrot and no,of occurance of other letters.

i = j = 0
word = "parrot"
for letters in word:
    if letters == "r":
        i += 1
    else:
        j += 1
print(i, j)

i = 0
while i < 5:
    if i == 2:
        print("hi")
    else:
        print("hello")
    i += 1

i = 1
j = 3
while i <= 10:
    print("{1{*{3{={i*j", format(j, i, i * j))
i+=1