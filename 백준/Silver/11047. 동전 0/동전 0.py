import sys
n, k =map(int,sys.stdin.readline().split())
List = [int(sys.stdin.readline()) for i in range(n)]
c = 0
for i in List[::-1]:
    c += k//i
    k%=i
print(c)
