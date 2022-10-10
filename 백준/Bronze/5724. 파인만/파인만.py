while(n:=int(input()))!=0:
    print(sum([i*i for i in range(1, n+1)]))
'''
while(n:=int(input()))!=0:
    c = 0
    i = 1
    n = n*n
    while True:
        c += (n//(i**2))
        i+=1
        print(c, i)
        if i**2>n: break
    print(c)
'''