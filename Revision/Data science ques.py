def word_in_letters(word, i=0, ):
    if i == len(word):
        print("".join(word))

    for j in range(i, len(word)):
        words = [c for c in word]

        words[i], words[j] = words[j], words[i]
        word_in_letters(words, i + 1)


print(word_in_letters("SAID"))


def word_from_let(word, letters):
    count = 0
    for i in word:
        if i in letters:
            if word.count(i) == letters.count(i):
                count += 1
        else:
            count -= 1
    if count == len(letters):
        aaa = True
    else:
        aaa = False
    return aaa


result2 = word_from_let("SAID", "DAIS")
print(result2)
