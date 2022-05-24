import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(map(int, input().split()),reverse=True)
for i in range(n):
    arr[i] += i+1
print(max(arr)+1)
