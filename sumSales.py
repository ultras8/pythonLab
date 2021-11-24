def sumSales(listsale,listprod):
    count = 0
    for i in range(len(listsale)):
        count += listprod.count(listsale[i][0]) * listsale[i][1]
    return count