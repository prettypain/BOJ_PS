n = int(input())
lst = [0] + list(map(int, input().split()))
for i in range(1, n+1): lst[i] += lst[i-1]
for _ in range(int(input())):
    s, e = map(int ,input().split())
    print(lst[e+1] - lst[s])