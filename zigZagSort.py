def zigZagSort(listNum):
    zig = []
    listNum = sorted(listNum,reverse=True)
    for i in range(len(listNum)):
        if i % 2 != 0 or i == 1:
            zig.append(listNum.pop(len(listNum)-1))
        else:
            zig.append((listNum.pop(0)))

    return zig
print(zigZagSort([1, 2, 3, 4, 5, 6, 7, 8, 9]))