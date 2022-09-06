n = int(input())
lst = list(map(int, input().split()))
k = int(input())

c = 0
start, end = 0, 0
while end < n:
    s = sum(lst[start:end+1])
    if s>k:
        c += (n-end)
        start += 1
    elif end!=n and s<=k:
        end += 1
    else:
        start += 1
print(c)
