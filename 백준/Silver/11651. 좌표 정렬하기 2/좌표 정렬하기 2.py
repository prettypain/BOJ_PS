import sys
dic = {}
input = sys.stdin.readline
for i in range(int(input())):
    a,b = map(int, input().split())
    if dic.get(b):
        dic[b].append(a)
    else:
        dic[b] = [a]
for i in sorted(dic.keys()):
    for j in sorted(dic[i]):
        print(j,i)
