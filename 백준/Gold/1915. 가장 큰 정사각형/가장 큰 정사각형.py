h,w = map(int, input().split())
c = 0

#search big square
g2 = [list(map(int, list(input()))) for _ in range(h)]
for i in range(1, h):
    for j in range(1, w):
        if g2[i][j]:
            g2[i][j] = min(g2[i-1][j-1], g2[i][j-1], g2[i-1][j]) + 1

print(max(map(max, g2))**2)