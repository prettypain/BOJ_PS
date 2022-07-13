a,b = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dic = {}
c = 0
lst = []
for i in b:
    dic[i] = 1

for i in a:
    if None==dic.get(i):
        c+=1
        lst.append(i)
if c:
    print(c)
    print(" ".join(map(str, sorted(lst))))
else:
    print(0)