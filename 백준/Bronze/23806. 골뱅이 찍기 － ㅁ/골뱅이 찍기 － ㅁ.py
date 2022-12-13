n = int(input())
print(*["@"*5*n]*n,*["@"*n+" "*3*n+"@"*n]*n*3,*["@"*5*n]*n,sep="\n")