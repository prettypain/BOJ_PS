def f(x,y):
    if x<0 or x>=n or y<0 or y>=n: return False
    return int(arr[x][y]) if arr[x][y].isdigit() else 0
n = int(input())
arr = [list(input()) for i in range(n)]
res = []
for x in range(n):
    tmp = ""
    for y in range(n):
        if arr[x][y].isdigit(): 
            tmp += "*"
        else:
            t=f(x-1, y-1)+f(x-1, y)+f(x-1, y+1) + f(x, y-1)+f(x, y)+f(x, y+1) + f(x+1, y-1)+f(x+1, y)+f(x+1, y+1)
            tmp += "M" if t>9 else str(t)
    res.append(tmp)
for i in res: print(i)
