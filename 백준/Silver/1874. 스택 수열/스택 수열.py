import sys
input=sys.stdin.readline

cur = 1
ans = []
stack = []
pb = True
n = int(input())
for i in range(n):
    tar = int(input())
    while cur <= tar:
        stack.append(cur)
        ans.append("+")
        cur+=1

    if stack[-1] == tar:
        stack.pop()
        ans.append("-")
    else:
        print("NO")
        pb = False
        break

if pb:
    for i in ans:
        print(i)
