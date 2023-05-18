r,s = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
s,t = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(s)]

res = [[0 for _ in range(t)] for __ in range(r)]
for i in range(r):
    for j in range(s):
        for k in range(t): res[i][k] += a[i][j]*b[j][k]

for i in res:print(*i)
