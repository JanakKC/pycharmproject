file = open("C:/New folder/JK.txt", 'r')
text = file.read()
splitted_text = list(dict.fromkeys(text.split()))  # Removing duplicate
print(splitted_text)

file = open("C:/New folder/JK.txt", 'r')
text = file.read()
splitted_text = (text.split())
print(splitted_text)

file = open("C:/New folder/JK.txt", 'r')
text = file.read()
splitted_text = dict.fromkeys(text.split())
print(splitted_text)

file = open("C:/New folder/JK.txt", 'r')
text = file.read()
splitted_text = list(dict.fromkeys(text.split()))
splitted_text.sort(reverse=False)
print(splitted_text)

for i in range(1, 11, ):
    print("2*", i, "=", 2*i)
