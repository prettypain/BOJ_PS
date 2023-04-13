import sys
sys.setrecursionlimit(10**6)
def in_range(x,y):
    return 0<=x<w and 0<=y<h

def f(x,y):
    graph[y][x] = "X"
    for dx, dy in zip(dxs, dys):
        if in_range(x+dx,y+dy) and graph[y+dy][x+dx]=="#":f(x+dx,y+dy)

def draw_graph():
    for i in graph:print(*i,sep="")

#      우 상 좌 하
dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]

for _ in range(int(input())):
    h,w = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    c = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j]=="#":
                f(j,i)
                c+=1
    print(c)