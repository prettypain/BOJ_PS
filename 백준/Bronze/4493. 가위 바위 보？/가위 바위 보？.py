f=input
for i in range(int(f())):
    ac,bc = 0,0
    for j in range(int(f())):
        a,b = f().split()
        if (a=='R' and b=='S') or (a=='S' and b=='P') or (a=='P' and b=='R'):
            ac += 1
        elif a==b:pass
        else:
            bc += 1
    print('Player 2' if ac<bc else 'Player 1' if ac>bc else 'TIE')
