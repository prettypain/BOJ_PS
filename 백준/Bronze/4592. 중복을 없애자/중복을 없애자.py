while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0: break
    arr, bf = [], 0
    for i in lst[1:]:
        if i != bf: arr.append(i)
        bf = i
    print(*arr,"$")