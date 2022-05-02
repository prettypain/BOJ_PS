import sys
input = sys.stdin.readline
n = int(input())
for i in sorted(set(map(int, input().split()))):
    print(i,end=" ")
