'''
dfs나 bfs나 1과 연관된 노드만 탐색해서 1를 제외한
노드스를 출력하면 그만이라 둘중 어떤 알고리즘을 사용해도
문제를 해결할 수 있음 1과 연관된 노드는 어떻게 구하느냐?
간단하게 방문처리할때 사용하는 visited리스트를 통해서
개수를 출력하면 된다!
'''

def dfs(graph : list[list[int]], v : int, visited : list[bool]) -> list[int]:
    visited[v] = True

    for i in graph[v]:
        if not visited[i]: dfs(graph, i, visited)

    return [idx for idx, val in enumerate(visited) if val]


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    


print(len(dfs(list(map(sorted, graph)), 1, [False]*(n+1)))-1)