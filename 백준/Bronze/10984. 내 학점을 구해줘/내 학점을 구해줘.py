for _ in range(int(input())):
    s = 0
    c = 0
    for i in range(int(input())):
        a,b = map(float, input().split())
        s += a*b
        c += a
    print(f'{int(c)} {s/c:.1f}')