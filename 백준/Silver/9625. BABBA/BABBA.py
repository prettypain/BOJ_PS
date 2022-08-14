def fibo(n):
    memo = [0, 1]
    for i in range(n-1):
        memo.append(memo.pop(0)+memo[0])
    return memo
print(" ".join(map(str, fibo(int(input())))))