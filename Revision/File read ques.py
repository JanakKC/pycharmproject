# Replace hyphens with single space
# Convert all characters to uppercase
# Split hyphenated words into separate words
# strip off all contractions and possessives from words;'s,'re etc.
# remove all punctuatution,whitespace characters and numbers.
# only keep words which occur in the official Sowpods.
# No duplicate in the list

file = open("C:/New folder/ABC.txt", 'r')
text = file.read()
splitted_text = text.split()
print(splitted_text)
x = text.upper()
a = x.replace("-", " ")
y = list(dict.fromkeys(x.split()))



print(x)
print(a)
