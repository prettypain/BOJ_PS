import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    oc=0
    tmp = input().strip()
    for i in tmp:
        if i=="(":
            oc+=1
        elif i==")":
            oc-=1

        if oc==-1:
            break

    if oc==0:
        print("YES")
    else:
        print("NO")
