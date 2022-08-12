from sys import stdin
def same_fibo(n):
    memo = [1,1,1] #1,2,3
    if n<=3: return 1
    else:
        for i in range(n-3):
            memo.append(memo.pop(0) + memo[1])
        return memo[2]

n = int(stdin.readline())
print(same_fibo(n))