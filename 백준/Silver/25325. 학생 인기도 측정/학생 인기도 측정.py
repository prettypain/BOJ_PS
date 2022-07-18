n = int(input())
lst = sorted(input().split())
score = [0]*n
dic = {}
for _ in range(n):
    for i in input().split():
        score[lst.index(i)] += 1
for i in range(n):
    if dic.get(score[i]): dic[score[i]] += ' '+lst[i]
    else: dic[score[i]] = lst[i]

for v in sorted(dic.keys(),reverse=1):
    for n in sorted(dic[v].split()):
        print(n,v)