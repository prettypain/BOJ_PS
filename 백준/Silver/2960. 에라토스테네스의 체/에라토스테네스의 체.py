n, k = map(int, input().split())
lst = list(range(2,n+1))
i=0
tar = None
while i!=k:
    m = min(lst)
    for j in range(len(lst)):
        if lst[j] == 100001: continue
        if lst[j]%m==0:
            i += 1
            if i==k:
                tar = lst[j]
                break
            lst[j] = 100001
print(tar)