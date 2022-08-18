for i in range(int(input())):
    s = 0
    a,b,c = map(int, input().split())
    print(f'Scenario #{i+1}:')
    print("yes" if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2 else "no","\n")