def wordRemove(sentence,word):
    lsentence = sentence.split(' ')
    textremove = ""
    for i in range (len(lsentence)):
        if(lsentence[i] != word):
            textremove += lsentence[i]
            textremove += " "
    return textremove.strip()