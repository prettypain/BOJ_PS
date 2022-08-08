def quick_pow(a,b): #빠른 제곱
    if b==1: return a
    tmp = quick_pow(a,b//2)
    if b%2==0:
        return tmp*tmp%10
    else:
        return tmp*tmp*a%10
    
n = int(input())
for i in range(n):
    a,b = map(int ,input().split())
    t = quick_pow(a,b)%10
    print(10 if t==0 else t)