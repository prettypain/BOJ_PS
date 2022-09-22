'''
이 문제의 핵심은(소수 구하는거는 둘쨰치고)
소수에 d가 몇번 들어가는게 아니라 d가 포함된 소수의 개수를 구하는 문제라는 점을
이해야만 한다(이거 떄문에 싸대기(wa) 7번 맞았음)
이것만 이해했을때 다른건 상대적으로 쉬웠음
'''
from sys import stdin
def sieve(n):
    lst = list(range(n+1))
    lst[1] = 0
    for i in range(2, int(n**0.5)+1):
        if lst[i] == 0: continue
        for j in range(i+i, n+1, i): lst[j] = 0
    return list(filter(lambda x : x!=0, lst[a:]))

a,b,d = map(int, stdin.readline().split())
a,b = min(a,b), max(a,b)
d = str(d)
res = 0
for i in sieve(b): res += (d in str(i))
print(res)
