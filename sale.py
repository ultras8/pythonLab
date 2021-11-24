def sale(price, amount):
    sum = 0
    while amount != 0 :
        if amount >= 5 :
            sum += price*0.5
        elif amount == 4 :
            sum += price*0.7
        elif amount == 3 :
            sum += price*0.8
        elif amount == 2 :
            sum += price*0.9
        else :
            sum += price*0.95
        amount-=1 
    return sum

print(sale(200, 20))