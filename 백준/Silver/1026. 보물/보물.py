n = int(input())
res = [0]*n
lst = sorted(map(int, input().split()))
arr = list(map(int, input().split()))
tar = arr.copy()
for i in range(n):
    idx = tar.index(max(tar))
    res[idx] = lst.pop(0)
    tar[idx] = -1
print(sum(map(lambda x,y : x*y, res,arr)))