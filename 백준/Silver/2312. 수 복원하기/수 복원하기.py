def seive(n):
    lst = list(range(n+1))
    lst[1] = 0
    for i in range(2, int(n**0.5)+1):
        if lst[i]==0: continue
        for j in range(i+i, n+1, i): lst[j] = 0
    return list(filter(lambda x: x!=0, lst))
def div(x):
    d = 2
    while d <= x:
        if x % d == 0:
            if dic.get(d): dic[d]+=1
            else: dic[d] = 1
            x = x / d
        else:
            d = d + 1

lst = seive(100000)
for _ in range(int(input())):
    n = int(input())
    dic = {};div(n)
    for k, v in dic.items():print(k, v)