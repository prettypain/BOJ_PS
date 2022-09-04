n, m = map(int, input().split())
lst = [0]
for i in list(map(int ,input().split())): lst.append(lst[-1] + i)
for _ in range(m):
    i, j = map(int ,input().split())
    print(lst[j] - lst[i-1])