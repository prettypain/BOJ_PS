n = int(input())
List = list(map(int,input().split()))
List.sort()
print(List[0]*List[-1])
