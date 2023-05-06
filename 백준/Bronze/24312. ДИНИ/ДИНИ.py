lst = sorted(map(int, input().split()))
a,b = 0,0

for i in range(4):
    if a>b:
        b += lst.pop()
    else:
        a += lst.pop()
print(abs(a-b))