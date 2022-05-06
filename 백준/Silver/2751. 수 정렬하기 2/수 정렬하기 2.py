import sys
input = sys.stdin.readline

N = int(input())
L =[]
for i in range(N):
  L.append(int(input()))
L.sort()
print("\n".join(list(map(str, L))),sep='')
