memo = [1,1]
n = int(input())
if n<3:
    print(n + (-1 if n==2 else 0))
else:
    for i in range(n-2):
        memo.append(memo.pop(0)+memo[0])
    print(memo[1])