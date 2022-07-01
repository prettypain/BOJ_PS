import sys
input = sys.stdin.readline
print('Yes' if int(input()) == sum(map(lambda x : x[0]*x[1],[list(map(int, input().split())) for i in range(int(input()))]))else 'No')