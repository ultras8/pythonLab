def kamehameha(sentence):
    maxCnt, curCnt, startIdx, stopIdx = 0, 0, 0, 0
    for i in range (0 ,len(sentence)-1):
        if((i == len(sentence) - 1) & maxCnt < curCnt):
            maxCnt = curCnt
            startIdx = i - curCnt
            stopIdx = i
        if(sentence[i] == sentence[i+1]):
            curCnt += 1
        else:
            if maxCnt < curCnt:
                maxCnt = curCnt
                startIdx = i - curCnt
                stopIdx = i
            curCnt = 0
    return '(' + str(startIdx) + ", " + str(stopIdx) + ')'