j = -1
n = int(input())
for i in range(n):
    print(" "*(n-i-1) + "*" + " "*j + "*"*(i!=0))
    j+=2
