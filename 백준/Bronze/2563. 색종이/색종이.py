lst = [[0 for j in range(100)] for i in range(100)]
n = int(input())
for _ in range(n):
    x,y = map(int, input().split())
    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            lst[i][j] = 1
print(sum(map(sum,lst)))