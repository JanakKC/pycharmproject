def find_words(word_list, letters):
    matched = {}
    wordscrabble = {"EAIONRTLSU": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
    for i in letters:
        value = 0
        flag = True


y = find_words(["AAAA", "SAID", "DAIS", "AIDS"], "IASDT")
print(y)
