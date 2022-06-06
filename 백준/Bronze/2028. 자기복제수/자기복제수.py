for _ in range(int(input())):
    n = input()
    t = str(int(n)**2)
    pb = True
    for i in range(len(n)):
        if n[-1-i] != t[-1-i]:
            pb = False
            break
    print("YES" if pb else "NO")