def letterAfter(sentence, word):
    for i in range (len(sentence)):
        if word[0] == sentence[i]:
            if(sentence[i:len(word)+i] == word):
                if(len(word)+i == len(sentence)): return "NULL"
                elif(sentence[len(word)+i] == ' '): return "NULL"
                else: return sentence[len(word)+i]

print(letterAfter("Expand", "Expan"))
print(letterAfter("HotChili", "Chili"))
print(letterAfter("Space Bar", "Space"))