import sys
I = sys.stdin.readline
for _ in range(int(I())):
    t=I().strip()
    print(t,'is','NEUTRAL'if(g:=t.lower().count('g'))==(b:=t.lower().count('b'))else'GOOD'if g>b else'A BADDY')