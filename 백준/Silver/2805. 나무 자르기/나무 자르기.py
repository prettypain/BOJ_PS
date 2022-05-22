import sys
input = sys.stdin.readline
n,k = map(int, input().split())
List = list(map(int, input().split()))

start = 0
end = max(List)
arr = []
while start+1 < end:
    mid = int((start + end)/2)
    s = 0
    for i in List:
        s+= 0 if i-mid<0 else i-mid
    if k <= s: start = mid
    else: end = mid
print(start)