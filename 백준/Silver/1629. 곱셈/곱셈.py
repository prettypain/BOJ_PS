def quick_pow(a,b):
    if b==1:
        return a%c
    tmp = quick_pow(a,b//2)
    if b%2==0:
        return tmp*tmp%c
    else:
        return tmp*tmp*a%c

a,b,c = map(int,input().split())
print(quick_pow(a,b))
