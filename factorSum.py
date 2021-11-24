def factorSum(n):
    b = 2
    factor = 0
    if(n == 1): return 1
    while(n != 1):
        if(n % b == 0):
            factor += b
            n /= b
        else: b += 1
    return factor

print(factorSum(1))
print(factorSum(12))
print(factorSum(11))
print(factorSum(10))