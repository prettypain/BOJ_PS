n = int(input())
st = input()

c = 0
for i in range(n//2):
    if st[i] != st[-(i+1)]:
        c+=1
print(c)