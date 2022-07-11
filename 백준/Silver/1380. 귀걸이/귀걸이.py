List = []
j=1
while(s:=int(input()))!=0:
    arr = [input() for i in range(s)]
    c=[]
    for i in range(2*s-1):
        t = int(input().split()[0])
        if t in c: c.remove(t)
        else: c.append(t)
    print(j,arr[c[0]-1])
    j+=1