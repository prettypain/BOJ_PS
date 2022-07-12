import sys
I, start, end = sys.stdin.readline,0,1
n, s = map(int,I().split())
lst = [0]*(n+1)
for idx, val in enumerate(list(map(int,I().split()))):
    lst[idx+1] = lst[idx] + val
ans = 1000001
while start!=n:
    t = lst[end] - lst[start]
    if t >= s:
        if end-start < ans: ans = end-start
        start+=1 #end를 늘 리면 값이 늘어남 start를 늘려서 값과 범위를 줄임
    else:
        if end!=n: end+=1
        else: start+=1
print(ans if ans!=1000001 else 0)