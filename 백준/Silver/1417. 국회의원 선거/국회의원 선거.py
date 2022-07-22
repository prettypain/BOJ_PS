c = 0
n = int(input())
lst = [int(input()) for i in range(n)]
while True:
    m = max(lst)
    cm = lst.count(m)
    if lst.index(m)==0 and cm==1: break
    idx = lst[1:].index(m)+1
    lst[idx]-=1
    lst[0] += 1
    c+=1
print(c)