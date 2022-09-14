c = 0
n = int(input())
for a in range(1, 501):
    for b in range(1, 501):
        if a**2 == b**2 + n:
            c+=1
print(c)