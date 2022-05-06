fruits = ["apple", "mango"]
word = "abc-xy"
test = word.split("-")
fruits.append(test[0])
print(test)
print(test[0])

fruits = ["apple", "mango"]
word = "abc-xyz"
fruits.append(word.split("-")[0])
print(fruits)

