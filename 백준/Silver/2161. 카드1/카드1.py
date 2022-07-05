n = int(input())
List = [i for i in range(1,n+1)]
s = 1
t = []
while len(List)!=1:
    t.append(List.pop(0))
    List.append(List.pop(0))
for i in t:
    print(i,end=" ")
print(List[0])