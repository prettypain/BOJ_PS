import sys
#input = sys.stdin.readline
#print = sys.stdou.write
def sieve(n):
    arr = list(range(n+1))
    arr[1] = 0
    for i in range(2, int(n**0.5)+1):
        if arr[i] == 0: continue
        for j in range(i+i, n+1, i): arr[j] = 0
    return list(filter(lambda x : x!=0, arr))

def sang(n):
    tmp = []
    while n!=1:
        n = sum(map(lambda x : int(x)**2, str(n)))
        if n in tmp: return False
        else: tmp.append(n)
    return True

n = int(input())
lst = sieve(n if n<1000000 else 1000000)
for i in lst:
    if sang(i): print(i)