n,m = map(int, input().split())

front = [-1]*n
back  = [-1]*n

for i in range(n):
    a,b = map(int, input().split())
    front[i] = a
    back[i] = b

now = front.copy()
for _ in range(m):
    k = int(input())
    for i in range(n):
        if now[i] <= k: now[i] = front[i] if now[i]!=front[i] else back[i]

print(sum(now))