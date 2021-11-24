def baseConvert(num, base1, base2):
    result = base10toanother(num, base1)
    if( base2 == 10 ): return result
    elif( base1 == 10 ): return anotherto10(num, base2)
    else: return anotherto10(result, base2)
def base10toanother(num, base1):
    base = 0
    count = 0
    lstnum = []
    for i in str(num):
        lstnum.append(i)
    for i in lstnum[::-1]:
        base += int(i)*(base1**count)
        count+=1
    return base
def anotherto10(base10, baseant):
    tmp10 = base10
    lst = []
    strre = ""
    while(tmp10 > 0):
        lst.append(int(tmp10%baseant))
        tmp10 = int(tmp10 / baseant)
    for i in lst[::-1]:
        strre += str(i)
    return strre