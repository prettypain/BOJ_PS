a,b = map(int, input().split())
c,d = map(int, input().split())
List = [a/c+b/d, c/d+a/b, d/b+c/a, b/a+d/c]
dic = {}
for i in range(4):dic[List[i]] = i
print(dic[max(List)])
