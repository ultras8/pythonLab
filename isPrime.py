def isPrime(num):
    flag = False
    if num == 1 : return False 
    if num > 1 :
        for i in range(2, num):
            if num % i == 0 :
                flag = True
                break
    if flag : return False
    else : return True

print(isPrime(1))