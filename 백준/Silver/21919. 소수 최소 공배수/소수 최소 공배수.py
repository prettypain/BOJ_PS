def seive(n):
    lst = list(range(n+1))
    lst[1] = 0
    for i in range(2, int(n**0.5)+1):
        if lst[i] == 0: continue
        for j in range(i+i, n+1, i): lst[j] = 0
    return lst

n = int(input())
lst = seive(1000000)
arr = []
for i in list(map(int, input().split())):
    if lst[i]:
        arr.append(i)
if len(arr)==0:
    print(-1)
else:
    res = 1
    for i in set(arr): res *= i
    print(res)