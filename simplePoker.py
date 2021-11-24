def FTofkind(play1, play2, ordi, n):
    check = 0
    tmp1 = ""
    tmp2 = ""
    for i in play1:
        if play1.count(i) == n :
            tmp1 = i
            check += 1
            break
    for j in play2:
        if play2.count(j) == n :
            tmp2 = j
            check += 1
            break
    if( check == 0 ) : return check 
    if( check == 1 ) : return "Player 2 Wins" if tmp1 == "" else "Player 1 Wins" 
    return "Player 1 Wins" if ordi.index(tmp1) > ordi.index(tmp2) else "Draw" if ordi.index(tmp1) == ordi.index(tmp2) else "Player 2 Wins" 

def twopair(play1, play2, ordi):
    check1 = 0
    max1 = -1
    tmp1 = ""
    tmp2 = ""
    for i in play1:
        if play1.count(i) == 2 and ordi.index(i) > max1:
            tmp1 = i
            max1 = ordi.index(i)
            check1 = 1
    max2 = -1
    check2 = 0
    for j in play2:
        if play2.count(j) == 2 and ordi.index(j) > max2:
            tmp2 = j
            max2 = ordi.index(j)
            check2 = 1
    if( check1 == 0 and check2 == 0) : return 0
    if( check1 == 0 or check2 == 0 ) : return "Player 2 Wins" if tmp1 == "" else "Player 1 Wins" 
    return "Player 1 Wins" if max1 > max2 else "Draw" if max1 == max2 else "Player 2 Wins"

def simplePoker(midf, play1, play2):
    play1.extend(midf)
    play2.extend(midf)
    ordi = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    ft = FTofkind(play1, play2, ordi, 4)
    if ft != 0 : return ft
    ft = FTofkind(play1, play2, ordi, 3)
    if ft != 0 : return ft
    ft = twopair(play1, play2, ordi)
    if ft != 0 : return ft
    max1 = -1
    max2 = -1
    for i in play1:
        if ordi.index(i) > max1: max1 = ordi.index(i)
    for j in play2:
        if ordi.index(j) > max2: max2 = ordi.index(j)
    return "Player 1 Wins" if max1 > max2 else "Draw" if max1 == max2 else "Player 2 Wins"

print( simplePoker (['4','9','4'], ['4','5'], ['K','K']) )
print( simplePoker (['3','2','5'], ['A','2'], ['3','6']) )
print( simplePoker (['2','Q','Q'], ['Q','A'], ['Q','3']) )