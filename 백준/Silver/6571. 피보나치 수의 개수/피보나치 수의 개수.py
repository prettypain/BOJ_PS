while 1:    
    a,b = map(int, input().split())
    if a==b==0: break
    memo = [1,2]
    c = 1 if a<=1<=b else 0
    c = c+1 if a<=2<=b else c
    while memo[1]<b:
        memo.append(memo.pop(0) + memo[0])
        if a<=memo[1]<=b:
            c+=1
    print(c)