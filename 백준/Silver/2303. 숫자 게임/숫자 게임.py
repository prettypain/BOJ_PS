import sys
input = sys.stdin.readline
res=-1
for k in range(int(input())):
    lst = list(map(int, input().split()))
    arr = []
    for i in lst:
       arr1 = lst.copy()
       arr1.remove(i)
       for j in arr1:
           arr2 = arr1.copy()
           arr2.remove(j)
           arr.append(int(str(sum(arr2))[-1]))
    m = max(arr)
    if m >= res:
        res = m
        idx = k+1
print(idx)