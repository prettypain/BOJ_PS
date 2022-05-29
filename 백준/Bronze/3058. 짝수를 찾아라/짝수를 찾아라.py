import sys
input = sys.stdin.readline
n=int(input())
for i in range(n):
    List = list(filter(lambda x : x%2==0, map(int, input().split())))
    print(sum(List),min(List))
