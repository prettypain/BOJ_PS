import sys
sys.setrecursionlimit(10**6)
def dfs(v: int, visited: [int], c: int) -> None:
    visited[v] = True
    if v == target[1]: lst.append(c)
    c+=1
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited, c)

n = int(input()) #사람 수
target = list(map(int, input().split()))#타겟
m = int(input()) #노드 입력 횟수
lst = []#target까지의 촌수

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(target[0], [False]*(n+1), 0)
print(min(lst) if len(lst) else -1)
