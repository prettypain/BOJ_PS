'''
2~103까지의 소수만 탐색하는 이유는 "연속한 두 소수의 곱으로 이루어져 있으면 특별한 수"
그리고 그 N보다 큰 특별한 수를 찾는게 답이다.
여기서 N의 범위는 최대 10000이다. 그리고 103까지 탐색했을 때
마지막에 있는 두 수의 곱이 10000을 넘는다. 그래서 103까지 소수를 구해 불필요한
시간을 줄였다.

위 설명이 이 문제의 핵심이며 시간을 줄이는 방법이다.
아무리 오래 걸려도 O(sqrt(103))에 정답이 나온다.
'''
def sieve(n):
    lst = list(range(n+1))
    lst[1] = 0
    for i in range(2, int(n**0.5)+1):
        if lst[i] == 0: continue
        for j in range(i+i, n+1, i): lst[j] = 0
    return list(filter(lambda x : x!=0, lst))

lst = sieve(103)
n = int(input())
for i in range(len(lst)-1):
    if n<lst[i] * lst[i+1]:
        print(lst[i] * lst[i+1])
        break
