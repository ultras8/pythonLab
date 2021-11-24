def currentTime(startTime, minute):
    while minute > 0 :
        if(minute >= 60):
            minute -= 60
            startTime+=1
        else: break
    startTime += (minute*(1/100))
    while(startTime >= 0):
        if startTime >= 24:
            startTime -= 24
        else: break
    if (startTime == 0.0): return "{:.1f}".format(startTime)
    return "{:.2f}".format(startTime)

print(currentTime(23.00, 60))