'''
주어진 그래프의 모든 인덱스들을 방문하면서 1을 발견 했을 때 해당 위치의
인덱스를 x,y라고할 때 그래프 범위를 벗어나지 않는 선에서
상하좌우를 모두 탐색한다. (x+1, y), (x-1, y), (x, y+1), (x, y-1)
탐색을 완료한 후 c(필요한 지렁이 개수, 정답)에 +1를 해준다.
이후 c를 출력해 완성.

기본적인 그래프 탐색 알고리즘 이론을 알고 있다면 쉽게 해결할 수 있다.
나는 그중에서 dfs 느낌으로 구현했기에 이름을 dfs라고 명했다.
'''
import sys
sys.setrecursionlimit(10**6)
def dfs(x,y):
    #전역변수에 있는 graph를 방문처리이면서 동시에 그래프로 사용
    graph[y][x] = 0
    if x+1<m and graph[y][x+1]: dfs(x+1, y)
    if y-1>=0 and graph[y-1][x]: dfs(x, y-1)
    if x-1>=0 and graph[y][x-1]: dfs(x-1, y)
    if y+1<n and graph[y+1][x]: dfs(x, y+1)


for t in range(int(sys.stdin.readline())):
    #m: 가로, n: 세로, k: 배추개수
    c = 0
    m,n,k = map(int ,sys.stdin.readline().split())
    graph = [[0 for _ in range(m)] for __ in range(n)]
    for _ in range(k):
        x,y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                dfs(j, i)
                c+=1
    print(c)