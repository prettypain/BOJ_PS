m=9999999
for i in range(int(input())):
    a,b = map(int, input().split())
    if b//a < m:m = b//a
print(m)