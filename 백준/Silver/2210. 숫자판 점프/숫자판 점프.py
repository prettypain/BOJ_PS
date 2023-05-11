import sys
sys.setrecursionlimit(10**6)

#우 상 좌 하
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

res = set()

def df(x, y, t):
    if len(t)==6:
        res.add(t)
        return
    t += graph[y][x]
    for dx, dy in zip(dxs, dys):
        dx,dy = dx+x, dy+y
        if 0<=dx<5 and 0<=dy<5: df(dx, dy, t)

graph = [list(input().split()) for _ in range(5)]
for i in range(5):
    for j in range(5):
        df(i, j, "")
print(len(res))
