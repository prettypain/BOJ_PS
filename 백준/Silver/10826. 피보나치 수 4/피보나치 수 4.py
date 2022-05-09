def fibo(t):
    if t<3:
        return t + (-1 if t==2 else 0)
    else:
        memo = [1,1]
        for i in range(t-2):
            memo.append(memo.pop(0)+memo[0])
        return memo[1]
print(fibo(int(input())))