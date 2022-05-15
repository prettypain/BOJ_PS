c = int(input())
col,ma = map(int, input().split())
if c<(col//2 + ma):
    print(c)
else:
    print(col//2 + ma)
