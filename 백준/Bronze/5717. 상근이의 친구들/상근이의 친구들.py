while True:
    a = input().split()
    if a[0] == '0': break
    print(sum(map(int, a)))