c = 0
n = int(input())
i = 1
while n>0:
    if n < i:
        i = 1
    n -= i
    i += 1
    c += 1
print(c)
