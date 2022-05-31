import sys
input=sys.stdin.readline
for _ in range(int(input())):
    input()
    a=list(map(int,input().split()))
    print(min(a),max(a))