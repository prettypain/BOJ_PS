def is_prime(n):#소수 판별
    if n==1 or (n!=2 and n%2==0): return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0: return False
    return True        
a,b = map(int, input().split())
for i in range(a, b+1):
    if is_prime(i):
        print(i)
