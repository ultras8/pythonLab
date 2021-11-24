def palindromeInside(str, size):
    word_list = str.split()
    for word in word_list:
        if(len(word) < size): continue
        else: 
            for i in range(len(word) - size + 1):
                seq = word[i:i+size]
                if(seq == seq[::-1]):
                    return seq
    return "None"

print( palindromeInside ("Please come this way, madam", 5) )
print( palindromeInside ("This madam looks like our mom", 3) )
print( palindromeInside ("Our radar isn't working", 4) )