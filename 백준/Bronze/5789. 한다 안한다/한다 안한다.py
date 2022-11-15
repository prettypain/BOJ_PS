for _ in range(int(input())):
    n = input()
    a,b = n[len(n)//2-1], n[len(n)//2]
    print("Do-it" if a==b else "Do-it-Not")