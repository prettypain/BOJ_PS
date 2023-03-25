res = 1
n,m = map(int, input().split())
for i in list(map(int, input().split())):res*=i
print(res%m)