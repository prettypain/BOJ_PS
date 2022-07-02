import sys
input = sys.stdin.readline
name = ['Soongsil', 'Korea', 'Hanyang']
arr = list(map(int, input().split()))
print("OK" if sum(arr) >= 100 else name[arr.index(min(arr))])