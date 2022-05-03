def fac(n):
    res = 1
    for i in range(2,n+1):
        res*=i
    return res

n,k = map(int, input().split())
res = int(fac(n)/(fac(n-k)*fac(k)))
print(res)
