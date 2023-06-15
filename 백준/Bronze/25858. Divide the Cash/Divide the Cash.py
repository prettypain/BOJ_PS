n,d = map(int, input().split())
lst = [int(input()) for _ in range(n)]
s = sum(lst)
for i in lst:print(int(d*(i/s)))