n = int(input())
for t in range(n):
    x,y = map(int, input().split())
    for i in range(y):
        print("X"*x)
    if t+1!=n:print()