List = []
s =  0
for _ in range(4):
    a,b = map(int, input().split())
    s+= b-a
    List.append(s)
print(max(List))