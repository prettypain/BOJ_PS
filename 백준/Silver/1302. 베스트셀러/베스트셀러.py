import sys
input = sys.stdin.readline
dic = {}
for i in range(int(input())):
    n = input().strip()
    if dic.get(n): dic[n] +=1
    else: dic[n] = 1
m = max(dic.values())
for k,v in sorted(dic.items()):
    if v==m:
        print(k)
        break