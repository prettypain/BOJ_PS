'''
파이썬은 pow()가 있어서 씹사기....
'''
def is_prime(n):
    if n==1 or (n!=2 and n%2==0): return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0: return False
    return True

while True:
    p, a = map(int ,input().split())
    if a==0: break
    print("yes"if not is_prime(p) and pow(a, p, p)==a else"no")