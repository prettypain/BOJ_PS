n = int(input())
i,j,c=1,2,1
while i!=j:
    s = sum(range(i,j+1))
    if s==n:
        c+=1
        j+=1
    elif s<n:
        j+=1
    elif s>n:
        i+=1
print(c)