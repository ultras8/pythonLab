n, s = input().split()
q = input()
lstq = []
for x in q:
    lstq.append(x)
for i in range(int(s)):
    j = int(n)-2
    while j >= 0:
        if lstq[j] == "B" and lstq[j+1] == "G":
            lstq[j+1] = "B"
            lstq[j] = "G"
        j-=1
print("".join(lstq))