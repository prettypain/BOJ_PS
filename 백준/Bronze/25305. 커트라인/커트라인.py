import sys
input = sys.stdin.readline
n, k = map(int, input().split())
print(sorted(map(int,input().split()),reverse=1)[k-1])