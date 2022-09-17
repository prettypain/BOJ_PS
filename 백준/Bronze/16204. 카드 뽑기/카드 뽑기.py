n, m, k = map(int, input().split())
now_o = m
now_x = n-m


o = k
x = n-k
print(min(now_o, o) + min(now_x, x))