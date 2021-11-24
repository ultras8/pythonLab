def wordRemove(sentence, word):
    wordlist = sentence.split()
    newWordList = [x for x in wordlist if x not in word]
    newString = ""
    for word in newWordList: newString += word + " "
    return newString if newString != None else None

str = input("Pls write a sentence : ")
word = input("Pls write a word : ")
print(wordRemove("Cake batter Frappuchinno", "Cake"))
print(wordRemove("White Chocolate Cinnamon Cracker Latte", "Cinnamon"))
print(wordRemove("Cinnamon Toast Crunch Frappuchinno", "Frappuchinno"))
print(wordRemove("My test case", "My test case"))
print(wordRemove(str, word))