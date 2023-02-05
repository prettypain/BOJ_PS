from itertools import product

def sieve(n):
    lst = list(range(n+1))
    lst[1] = 0
    for i in range(2, int(n**0.5)+1):
        if lst[i]==0: continue
        for j in range(i+i, n+1, i): lst[j] = 0
    return list(filter(lambda x : x!=0, lst))


n = int(input())
pb = False

if n>=8 and n%2==0: #2, 2
    n-=4
    lst = sieve(n)
    for i in product(lst, repeat = 2):
        if sum(i) == n:
            print(2,2,*i)
            pb = True
            break
elif n>=8 and n%2==1: # 2 3
    n-=5
    lst = sieve(n)
    for i in product(lst, repeat = 2):
        if sum(i) == n:
            print(2,3,*i)
            pb = True
            break
if not pb:print(-1)