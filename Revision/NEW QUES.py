# 1=E,A,I,O,N,R,T,L,S,U
# 2=D,G
# 3=B,C,M,P
# 4=F,H,V,W,Y
# 5=K
# 8=J,X
# 10=Q,Z

def total_word(word):
    count = 0
    wordscrabble = {"EAIONRTLSU": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
    for i in word:
        for x in wordscrabble.keys():
            if i in x:
                count += wordscrabble[x]

    return count


y = total_word("ADVENTURES")
print(y)


def word_scores(word):
    wordscore = 0
    for i in word:
        if i in "EATONRTLSU":
            wordscore += 1
        elif i in "DG":
            wordscore += 2
        elif i in "BCMP":
            wordscore += 3
        elif i in "FHVWY":
            wordscore += 4
        elif i in "K":
            wordscore += 5
        elif i in "JX":
            wordscore += 8
        else:
            wordscore += 10
    return wordscore


y = word_scores("ADVENTURES")
print(y)


def total_sum(abc):
    count = 0
    wordscrabble = {"EAIONRTLSU": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
    for i in abc:
        for x in wordscrabble:
            if i in x:
                count += wordscrabble[x]
    return count


y = total_sum("EARTHINGS")
print(y)
