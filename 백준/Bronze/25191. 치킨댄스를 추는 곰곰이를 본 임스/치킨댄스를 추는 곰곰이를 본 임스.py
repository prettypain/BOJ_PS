c = int(input())
col,ma = map(int, input().split())
print(c if (c<(col//2 + ma)) else col//2 + ma)