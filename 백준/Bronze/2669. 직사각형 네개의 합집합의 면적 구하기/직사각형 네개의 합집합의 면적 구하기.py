List = [[0 for i in range(101)] for j in range(101)]
for i in range(4):
    a,b,x,y = map(int, input().split())
    ax = x-a
    ay = y-b
    for i in range(a,x):
        for j in range(b,y):
            List[i][j] = 1
c = 0
for i in List:
    c+= i.count(1)
print(c)