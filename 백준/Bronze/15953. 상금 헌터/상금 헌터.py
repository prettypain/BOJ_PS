arr = [500,300,300,200,200,200]+[50]*4+[30]*5+[10]*6+[0]
lst = [512,256,256]+[128]*4+[64]*8+[32]*16+[0]
for i in range(int(input())):
    a,b = map(int, input().split())
    if a>21: a = 22
    if b>31: b = 32
    print((arr[a-1]+lst[b-1])*10000)