import sys
input = sys.stdin.readline
input()
List = []
for i in range(2): List+= list(map(int, input().split()))
print(" ".join(map(str, sorted(List))))