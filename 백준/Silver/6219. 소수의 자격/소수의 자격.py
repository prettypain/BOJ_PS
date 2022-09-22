def sieve(n):
    lst = list(range(n+1))
    lst[1] = 0
    for i in range(2, int(n**0.5)+1):
        if lst[i] == 0: continue
        for j in range(i+i, n+1, i): lst[j] = 0
    return list(filter(lambda x : x!=0, lst[a:]))

a,b,d = map(int, input().split())
a,b = min(a,b), max(a,b)
d = str(d)
res = 0
for i in sieve(b):
    res += (d in str(i))
print(res)
