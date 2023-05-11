# '*'는 소행성 덩어리
# '.' 빈 공간이 없는 광대한 공간
# 방문된 경우 그룹넘버 부여
'''
상하좌우로 연결된 소행성덩어리를 모두 그룹화시켜서 그룹의 개수를 출력한다.
'''

import sys
sys.setrecursionlimit(1000*1000)
#우, 하, 좌, 상
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

def df(x,y):
    lst = [(x,y)]
    while lst:
        x,y = lst.pop()
        graph[y][x] = group
        for dx, dy in zip(dxs, dys):
            dx, dy = dx+x, dy+y
            if 0<=dx<n and 0<=dy<n and graph[dy][dx]=="*": lst.append((dx,dy))
        

group = 1
n = int(input())
graph = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == "*":
            df(j, i)
            group += 1
print(f'{group-1}')#마지막 그룹을 찾아내고 +1를 하므로 이를 빼면 정답이다.
