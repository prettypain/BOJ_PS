m = 0
p = 0
for i in range(10):
    a,b = map(int, input().split())
    p+=b
    p-=a
    if p > m: m = p
print(m)
