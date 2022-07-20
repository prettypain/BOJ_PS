n = int(input())
tar = 1
for _ in range(n):
    a,b = map(int ,input().split())
    tar = a if tar==b else b if tar==a else tar
print(tar)