def find_words(word_list, letters):
    matched = {}
    wordscrabble = {"EAIONRTLSU": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
    for i in word_list:
        value = 0
        flag = True
        for x in i:
            if x in letters:
                if (i.count(x) <= letters.count(x)):
                    flag = True
                    for ws in wordscrabble.keys():
                        if x in ws:
                            value += wordscrabble[ws]
                        else:
                            pass

                    pass
                else:
                    flag = False
                    break
            else:
                flag = False
        if flag == True:
            matched[i]=value
    return matched


y = find_words(["AAAA", "SAID", "DAIS", "AIDS"], "IASDT")
print(y)
