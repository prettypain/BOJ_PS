def fibo(n):
    memo = [1,1]
    if n<3:return n + (-1 if n==2 else 0)
    else:
        for i in range(n-2):
            memo.append(memo.pop(0)+memo[0])
        return memo[1]
print(fibo(int(input())))