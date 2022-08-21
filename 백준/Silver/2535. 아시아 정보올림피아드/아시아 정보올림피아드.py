n = int(input())
dic = {}
for i in range(n):
    coutry, num, score = map(int, input().split())
    dic[score] = [coutry, num]

res = []
for i in sorted(dic.keys(), reverse=1):
    t = dic[i]
    c = 0
    for j in res:
        if j[0] == t[0]: c+= 1
    if c<2: res.append(t)
    else:continue
    if len(res)==3:break
for i in res:print(*i)