n = int(input())
for i in range(1,n):n*=i
print(n%10 if n>1 else 1)