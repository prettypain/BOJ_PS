'''
https://velog.io/@kjh107704/그래프-연결-요소
연결 요소(Connected Component)는 그래프가 주어질 때
덩어리가 몇개 있냐 즉 연결되지 않은 노드의 그룹의 개수를 말한다.
예를들어 1부터 5까지의 노드가 있을 때
1부터 3까지 서로 무방향으로 연결되어있고
4와 5는 서로 무방향으로 연결되어있다고 할 때
연결 요소의 개수는 2개라고 할 수 있다.
여기에 6이 홀로 추가된다고 하면

(1,2,3), (4,5), (6)으로써 총 3개라고 할 수 있다.
이 문제는 dfs든 bfs든 어떤 탐색을 사용해도 문제를 해결할 수 있을 것이다.
나는 visited의 변화에 따라 갯수를 탐색할 것이다.
처음 visited = [False]*(노드의 개수 + 1)이라고 할 떄
1부터 탐색후 visited를 리턴받고 방문하지 않은 노드 번호로 다시 탐색을한다
위를 방문하지 않는 노드가 없을 떄까지 반복하고 총 반복한 횟수는
즉 연결 요소의 개수가 된다.
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(graph: list([int]), v: int, visited: [bool]) -> [bool]:
    visited[v] = True

    for i in graph[v]:
        if not visited[i]: dfs(graph, i, visited)
    return visited


n,m = map(int, input().split())
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
#탐색 순서는 상관 없으므로 정렬은 안함(시간 복잡도 줄이기위해서)
c = 0
while sum(visited)!=n:
    for i in range(1, n+1):
        if not visited[i]:
            v = i
            break
    visited = dfs(graph, i, visited)
    c += 1
sys.stdout.write(f'{c}\n')