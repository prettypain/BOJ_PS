val = list(map(int, input().split()))
cnt = list(map(lambda x : val.count(x), val))
print(val[cnt.index(max(cnt))])