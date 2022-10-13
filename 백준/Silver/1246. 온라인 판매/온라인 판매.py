'''
판매할 계란 가격을 정해서 가장 큰 수익을 올리는 경우를 찾으면 된다.
(단 계란의 개수 이내에서 판매, (판매개수) <= n)

가격은 최대한 큰 편이 좋다.
그렇기에 1부터 1000까지가 아닌 lst를 넣어 반복하므로써 최소한이며
일정 개수를 판매할 수 있는 값으로 반복할 수 있다.

'''
from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
lst = [int(input()) for i in range(m)]

price = 0
m = 0 

for i in lst:
    l = len(list(filter(lambda x : x >= i, lst)))
    if l*i > m and l <= n:
        m = l*i
        price = i
print(price, m)