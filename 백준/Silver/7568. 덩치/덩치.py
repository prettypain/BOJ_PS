n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
rank = []
for w,h in arr:
    c = 1
    for i in range(n):
        tar = arr[i]
        if tar[0] > w and tar[1] > h:
            c+=1
    rank.append(c)
for i in rank:
    print(i,end=" ")
