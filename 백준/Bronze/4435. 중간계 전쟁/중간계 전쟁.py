import sys
I=sys.stdin.readline
for i in range(int(I())):
    g,s = list(map(int,I().split())),list(map(int,I().split()))
    for x,v in enumerate([1,2,3,3,4,10]):g[x]*=v
    for x,v in enumerate([1,2,2,2,3,5,10]):s[x]*=v
    g,s=sum(g),sum(s)
    print(f'Battle {i+1}:',"No victor on this battle field"if g==s else("Good triumphs over Evil"if g>s else"Evil eradicates all trace of Good"))