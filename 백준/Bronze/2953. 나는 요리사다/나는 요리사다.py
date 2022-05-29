dic = {}
List = []
for i in range(1,6):
    s = sum(map(int, input().split()))
    dic[s] = i
    List.append(s)
print(dic[max(List)],max(List))
