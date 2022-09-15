from sys import stdin
k, w, m = map(int, stdin.readline().split())

t = w-k
if t<0: c = 0
else:
    if t%m == 0:
        c = t//m
    else:
        c = (t//m)+1
print(c)