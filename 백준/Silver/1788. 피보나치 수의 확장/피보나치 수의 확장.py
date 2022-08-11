def fibo(n):#피보나치수열 for버전  
    memo = [1,1]
    if n<3:return n + (-1 if n==2 else 0)
    else:
        for i in range(n-2):
            memo.append((memo.pop(0)+memo[0])%1000000000)
        return memo[1]

n = int(input())
print(f'{1 if n>0 else 0 if n==0 else -1 if n%2==0 else 1}\n{fibo(abs(n))}')