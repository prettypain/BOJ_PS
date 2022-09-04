def is_prime(n):
    if n==1 or (n!=2 and n%2==0): return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0: return False
    return True

a,b = input().split()
print("Yes" if is_prime(int(b+a)) and is_prime(int(a)) else "No")