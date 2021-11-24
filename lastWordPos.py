def lastWordPosition(sentence):
    word = ""
    for c in sentence:
        word += str(sentence.rfind(c) + 1)
    return word
print(lastWordPosition("room"))
print(lastWordPosition("apartment"))
print(lastWordPosition("123/31"))