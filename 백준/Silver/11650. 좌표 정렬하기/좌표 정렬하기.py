import sys
dic = {}
input = sys.stdin.readline
for i in range(int(input())):
    a,b = map(int, input().split())
    if dic.get(a):
        dic[a].append(b)
    else:
        dic[a] = [b]
for i in sorted(dic.keys()):
    for j in sorted(dic[i]):
        print(i,j)
