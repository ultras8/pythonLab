def sumType(a, b):
    if(a + b) > 0 :
        return "Positive"
    elif(a + b) < 0 :
        return "Negative"
    else : return "Zero"

print(sumType(1000, -1000))