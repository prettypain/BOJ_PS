import sys
input = sys.stdin.readline
dic = {}
arr = []
n,m = map(int,input().split())
for i in range(n):
    a = input().rstrip()
    dic[a] = 1
for i in range(m):
    a = input().rstrip()
    if dic.get(a):
        arr.append(a)
arr.sort()
print(len(arr))
for i in arr:
    print(i)