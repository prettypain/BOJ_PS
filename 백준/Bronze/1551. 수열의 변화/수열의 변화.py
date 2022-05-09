l, n = map(int, input().split())
List = list(map(int, input().split(",")))
for k in range(n):
    for i in range(l-1):
        List[i] = List[i+1]-List[i]
for i in range(l-n):
    print(List[i],end=("," if i!=l-n-1 else ""))