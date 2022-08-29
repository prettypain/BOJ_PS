n, t = map(int, input().split())
dic = {}
for i in range(1, n+1):
    for j in str(i):
        if dic.get(j):
            dic[j]+=1
        else:
            dic[j] = 1
print(dic[str(t)])