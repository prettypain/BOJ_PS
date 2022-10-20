from itertools import product
from sys import stdin
input = stdin.readline

lst = [1,2,3]
t = int(input())
for _ in range(t):
    c = 0
    n = int(input())
    
    for j in range(1, n+1):
        for i in product(lst, repeat=j):
            if sum(i) == n:
                c += 1
    print(c)