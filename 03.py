n = int(input())
dic = {}
for i in range(n):
    temp = input().split('/') 
    dic.update({temp[0] : (temp[1])})
check = input()
if check in dic:
    print(dic[check])
else: print("NOT HAVE")