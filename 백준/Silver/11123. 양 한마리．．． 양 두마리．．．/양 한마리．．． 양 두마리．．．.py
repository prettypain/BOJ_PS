'''
f함수는 그래프를 탐색하면서 양을 찾으면 X표시해주는 함수이다(dfs느낌으로 작동)
이 함수는 처음에 들어오는 x,y 좌표값에 있는 값을 X표시해준다.

(0, 0)부터 시작해서 우상좌하로 좌표값을 변경하면서 인덱스 범위에 들어와 있는지
체크 후 해당 좌표에 #(양)이 있으면 X표시해 다시 방문하지 않게 처리해준다.
위 행동을 요소의 개수만큼 방문한다.
'''
import sys
sys.setrecursionlimit(10**6)
def in_range(x,y):
    return 0<=x<w and 0<=y<h

def f(x,y):
    graph[y][x] = "X"
    for dx, dy in zip(dxs, dys):
        if in_range(x+dx,y+dy) and graph[y+dy][x+dx]=="#":
            f(x+dx,y+dy)

#      우 상 좌 하
dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]

for _ in range(int(sys.stdin.readline())):
    h,w = map(int, sys.stdin.readline().split())
    graph = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
    c = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j]=="#":
                f(j,i)
                c+=1
    sys.stdout.write(f'{c}\n')