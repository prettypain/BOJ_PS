import sys, math
input = sys.stdin.readline

top = 0
time = math.inf
n,m,b = map(int, input().split())
List = [list(map(int, input().split())) for i in range(n)]

for h in range(257):
    Max = 0 
    Min = 0
    for i in range(n):
        for j in range(m):
            if List[i][j] < h:
                Min+= (h - List[i][j])
            else:
                Max+= (List[i][j] - h)
    
    if b+Max < Min:
        continue

    tmp = Max*2 + Min
    if time >= tmp:
        time = tmp
        top = h
print(time, top)
