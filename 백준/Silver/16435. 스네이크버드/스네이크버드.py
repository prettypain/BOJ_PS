n, st = map(int, input().split())
lst = sorted(map(int, input().split()))
while lst[0]<=st:
    st+=1
    lst.pop(0)
    if len(lst)==0: break
print(st)
