while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0: break
    arr = []
    lst.pop(0)
    bf = 0
    for i in lst:
        if i != bf: arr.append(i)
        bf = i
    print(*arr,"$")