def is_prime(n):
    if n==1 or (n!=2 and n%2==0): return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0: return False
    return True

n = int(input())+1
while is_prime(n):
    n+=1
print(n)