n = int(input())
i = 1
f = 1
s = 1
while i<n:
    f,s = s, s+f
    i+=1
print(f)