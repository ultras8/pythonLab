def wrapGift(gifts, wrap):
    list = gifts.split()
    str = ''
    for i in list: str += wrap[0] + i + wrap[1] + ' '
    return str

print(wrapGift("chocolate white-chohcolate", "()"))
print(wrapGift("choco candy gummy", "[]"))
print(wrapGift("cookies pocky cake M&M", "{}"))