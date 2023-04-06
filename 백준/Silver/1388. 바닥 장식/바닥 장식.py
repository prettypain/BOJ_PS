'''
"-"의 경우 x축 이동으로만 탐색해 인접해 있는 -만 모두 방문 처리한다.
"|"의 경우 y축 이동으로만 탐색해 인접해 있는 |만 모두 방문 처리한다.
방문한 노드의 경우 " "으로 만든다.
'''
import sys
sys.setrecursionlimit(10**6)
#시간초과하면 mx, my로 f그래프를 따로 def해라(if때문에 시간)
def f(x: int, y: int, v: str) -> None:
    tile[y][x] = ""
    if v=="-": #x축
        #print("x", x, y, x+1<m , tile[y][x]=="-")
        if x+1<m and tile[y][x+1]=="-": f(x+1, y, v)
        if x-1>0 and tile[y][x-1]=="-": f(x-1, y, v)
    else:
        #print("y")
        if y+1<n and tile[y+1][x]=="|": f(x, y+1, v)
        if y-1>0 and tile[y-1][x]=="|": f(x, y-1, v)

#세로(y): n, 가로(x): m
c = 0
n,m = map(int, input().split())
tile = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if tile[i][j] != "":
            f(j, i, tile[i][j])
            c += 1
print(c)