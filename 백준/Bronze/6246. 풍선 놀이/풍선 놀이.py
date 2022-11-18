n, q = map(int, input().split())
lst = [1]*n
for _ in range(q):
    l, i = map(int, input().split())
    for j in range(l-1, n, i): lst[j] = 0
print(sum(lst))