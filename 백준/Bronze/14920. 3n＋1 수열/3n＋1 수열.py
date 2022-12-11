n = int(input())
c = 1
while n!=1:
    n = n//2 if n%2==0 else n*3+1
    c += 1
print(c)