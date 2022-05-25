n = int(input())
List = list(range(1,n+1))
while len(List) != 1:
    List = List[1::2]
print(List[0])