def kamehameha(sentence):
    max = 0
    tmp = 0
    count = 0
    for i in range (1 ,len(sentence)):
        if(sentence[tmp] == sentence[i]):
            count += 1
        else:
            if max < count:
                max = count
                stop = i
            count = 0
        tmp += 1
    if max < count:
        max = count
        stop = len(sentence)
    return (stop-1)-max, stop-1
print(kamehameha("kamehamehaaaaaaaaaaaaaaa"))