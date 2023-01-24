n,p = map(int, input().split())
for i in range(2,n): n = (n*i)%p
print(n%p)