while True:
    n, m = map(int, input().split())
    if n==0 and m==0: break
    lst = list(map(int, input().split()))
    c = 0
    for i in set(lst):
        if lst.count(i) > 1: c += 1
    print(c)
    
