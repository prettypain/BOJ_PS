import sys
sys.setrecursionlimit(10**6)
def dfs(v):
    for i in graph[v]:
        if not visited[i]:
            par[i] = v
            visited[i] = True
            dfs(i)

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
par = [0]*(n+1)

for i in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
for i in range(2, n+1):
    print(par[i])