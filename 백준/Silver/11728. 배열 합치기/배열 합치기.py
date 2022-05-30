a,b = map(int, input().split())
List = []
for i in range(2):
    List+= list(map(int, input().split()))
for i in sorted(List):
    print(i,end=" ")