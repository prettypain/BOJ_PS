for i in range(int(input())):
    r,e,c=map(int, input().split())
    print('advertise'if r<e-c else'does not matter'if r==e-c else'do not advertise')