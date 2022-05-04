import sys
input = sys.stdin.readline
n, m = map(int, input().split())
List = list(map(int, input().split()))
arr = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i==j or i==k or j==k: continue
            if sum([List[i], List[j], List[k]])<=m:
                arr.append(sum([List[i], List[j], List[k]]))
print(max(arr))
            
