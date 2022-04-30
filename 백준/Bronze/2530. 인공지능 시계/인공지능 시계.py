h,m,s = map(int, input().split())
sc = int(input())
s+= sc

m+=s//60
s%=60

h+=m//60
m%=60
h%=24
print(h,m,s)
