n,w,h = map(int, input().split())
m = (h**2+w**2)**0.5
for _ in range(n):
    print("DA" if int(input())<=m else"NE")
