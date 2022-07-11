for i in range(int(input())):
    n = input()
    s = int(n)
    for i in range(len(n)):
        s = round(s+0.1,-i)
    print(int(s))