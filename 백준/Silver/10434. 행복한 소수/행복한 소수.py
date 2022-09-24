import sys
input = sys.stdin.readline
print = sys.stdout.write
def is_prime(n):
    if n==1 or n%2==0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0: return False
    return True

for _ in range(int(input())):
    no, n = map(int, input().split())
        
    if is_prime(n):#소수인 경우
        t = n
        for __ in range(20):
            t = sum(map(lambda x : int(x)**2, str(t)))
        if t==1:
            print(f'{no} {n} YES\n')
        else:
            print(f'{no} {n} NO\n')
    else:
        print(f'{no} {n} NO\n')