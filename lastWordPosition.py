def lastWordPosition(word):
    wordAns = ""
    for i in range (len(word)):
        temp = word[i]
        if(word.count(temp) > 1):
            tempword = word[i]
            max = 0
            for x in range (len(word)):
                if tempword == word[x]:
                    max = x
            wordAns += str(max+1)
        else:
            wordAns += str(i+1)
    return wordAns