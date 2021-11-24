def wrapGift(gifts, wrap):
    listgift = gifts.split(' ')
    strGift = ""
    for i in listgift:
        strGift += wrap[0] + i + wrap[1] + " "
    return strGift.strip()