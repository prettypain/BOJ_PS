n = int(input())
List = list(map(int, input().split()))
m = int(input())
s = 0
for i in List:
    s+= m*((i//m) + (1 if (i%m)>0 else 0))
print(s)
