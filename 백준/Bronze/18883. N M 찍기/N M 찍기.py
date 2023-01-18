n, m =map(int, input().split())
c = 1
for i in range(n):
    for j in range(m):
        print(c,end=("\n" if c%m==0 else " "))
        c+=1