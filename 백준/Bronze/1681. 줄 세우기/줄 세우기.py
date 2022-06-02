n, l = input().split()
List = []
i = 1
n = int(n)
while len(List) != n:
    if l not in str(i):
        List.append(i)
    i+=1
print(List[-1])
