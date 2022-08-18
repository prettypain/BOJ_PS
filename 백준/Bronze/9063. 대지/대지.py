xs,ys = [], []
for i in range(int(input())):
    x,y = map(int, input().split())
    xs.append(x)
    ys.append(y)
print((max(xs)-min(xs))*(max(ys)-min(ys)))