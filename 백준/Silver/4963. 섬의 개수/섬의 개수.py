'''
1012문제에서 대각선 방향으로 탐색을 추가한 문제이다.
빠른 i/o를 사용하지 않아도 68ms라는 빠른 속도로 문제가 해결된다.

문제를 해결한 방식은 생각보다 간단하다.
단순히 그래프를 (0, 0)부터 하나하나 방문해 보면서 땅(1)를 발견하면
상하좌우대각선을 모두 탐색해 1이 있으면 0으로 바꾸고 땅(1)를 발견한 시점에서
c+=1를 해주고 최종적으로 그래프를 모두 탐색했다면 c를 출력한다.

단순하지만 그래프 이론 알고있어야 편하게 해결할 수 있는 문제이다.

'''
import sys
sys.setrecursionlimit(10**6)
def dfs(x,y):
    #전역변수에 있는 graph를 방문처리이면서 동시에 그래프로 사용
    graph[y][x] = 0

    #가로이동
    if x+1<w and graph[y][x+1]: dfs(x+1, y)
    if x-1>=0 and graph[y][x-1]: dfs(x-1, y)

    #세로이동
    if y-1>=0 and graph[y-1][x]: dfs(x, y-1)
    if y+1<h and graph[y+1][x]: dfs(x, y+1)

    #대각선 이동
    if x+1<w and y+1<h and graph[y+1][x+1]: dfs(x+1, y+1)
    if x+1<w and y-1>=0 and graph[y-1][x+1]: dfs(x+1, y-1)
    if x-1>=0 and y+1<h and graph[y+1][x-1]: dfs(x-1, y+1)
    if x-1>=0 and y-1>=0 and graph[y-1][x-1]: dfs(x-1, y-1)

while True:
    #w: 가로, h: 세로, k: 배추개수
    c = 0
    w,h = map(int ,input().split())
    if w==0: break
    graph = [list(map(int, input().split())) for _ in range(h)]
    #for i in graph:print(*i)

    for i in range(h):
        for j in range(w):
            if graph[i][j]:
                dfs(j, i)
                c+=1
                #for t in graph:print(*t)
    print(c)