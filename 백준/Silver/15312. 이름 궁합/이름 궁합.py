import sys
input = sys.stdin.readline
lst = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a = input().strip()
b = input().strip()
t = ""
for i in range(len(a)): t += a[i]+b[i]
arr = [lst[ord(i)-65] for i in t]
while len(arr)!=2:
    t = []
    for i in range(len(arr)-1):
        t.append((arr[i]+arr[i+1])%10)
    arr = t
print("".join(map(str,arr)))