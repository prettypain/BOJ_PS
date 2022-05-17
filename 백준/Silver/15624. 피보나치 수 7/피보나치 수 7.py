#비네공식써도 못맞추는걸 이렇게 맞추니 허무하다....
def fibo(t):
    a, b = 0, 1
    for i in range(t):
        a, b = b%1000000007, (a+b)%1000000007
    return a
n = int(input())
print(fibo(n))
