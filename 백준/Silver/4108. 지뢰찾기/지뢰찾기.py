def f(x,y):
    if x<0 or x>=r or y<0 or y>=c: return False
    return arr[x][y]=="*"
while True:
    r,c = map(int, input().split())
    if r==0 or c==0: break
    arr = [list(input()) for i in range(r)]
    res = []
    for x in range(r):
        tmp = ""
        for y in range(c):
            if arr[x][y] == "*":
                tmp += arr[x][y]
            else:
                tmp += str(f(x-1, y-1)+f(x-1, y)+f(x-1, y+1) + f(x, y-1)+f(x, y)+f(x, y+1) + f(x+1, y-1)+f(x+1, y)+f(x+1, y+1))
        res.append(tmp)
    for i in res:
        print(i)