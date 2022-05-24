n = int(input())
for i in range(n-1,1,-1):
    n*=i
n = str(n)
c = 0
if n!='0':
    for i in range(len(n)-1,-1,-1):
        if n[i]!='0':break
        c+=1
print(c)
