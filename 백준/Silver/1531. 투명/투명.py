lst = [[0 for j in range(100)] for i in range(100)]
n, m = map(int, input().split())
for _ in range(n):
    bx, by, tx,ty = map(int, input().split())
    for x in range(bx-1, tx):
        for y in range(by-1, ty):
            lst[x][y] += 1
c = 0
for i in range(100):
    for j in range(100):
        if lst[i][j]>m:
            c+=1
print(c)