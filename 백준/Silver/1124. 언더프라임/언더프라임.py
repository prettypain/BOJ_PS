import sys
input = sys.stdin.readline
print = sys.stdout.write
def sieve(start, end):
    lst = list(range(end+1))
    lst[1] = 0
    for i in range(2, int(end**0.5)+1):
        if lst[i] == 0: continue
        for j in range(i+i, end+1, i): lst[j] = 0
    return lst
def factorization(x):
    val = []
    d = 2
    sqx = int(x**0.5)+1
    while d <= sqx:
        if x % d == 0:
            val.append(d)
            x = x / d
        else:
            d = d + 1
    if x > 1: val.append(x)
    return val

res = 0
a,b = map(int, input().split())
prime = sieve(0, b)
lst = [idx for idx, val in enumerate(prime) if val==0]
for i in range(a, b+1):
    if prime[len(factorization(i))]: res+=1
print(f'{res}')